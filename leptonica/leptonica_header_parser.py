# -*- coding: utf-8 -*-
    
    
    # "pyleptonica" is a Python wrapper to Leptonica Library
    # Copyright (C) 2010 João Sebastião de Oliveira Bueno <jsbueno@python.org.br>
    
    #This program is free software: you can redistribute it and/or modify
    #it under the terms of the Lesser GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the Lesser GNU General Public License
    #along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
This file is responsible to parse the Leptonica library
C structures, as defined in the source code header files
and generate corresponding c_types python classes
to interoperate with them.

You may not need to run this to get pyleptonica running - 
check if your leptonica_structures work for your version
of leptonica
"""

import sys
from config import leptonica_home

lepton_source_dir = leptonica_home + "/src/"
target_file = "leptonica_structures.py"

# I am feeling quite intimidated by "parsers"
# at this time. let's do it by hand.

# from the "environ.h" file in leptonica source
lepton_types = {
    "l_int8": "ctypes.c_byte", 
    "l_uint8": "ctypes.c_ubyte",
    "l_int16": "ctypes.c_int16",
    "l_uint16": "ctypes.c_uint16",
    "l_int32": "ctypes.c_int32",
    "l_uint32": "ctypes.c_uint32",
    "l_float32": "ctypes.c_float",
    "l_float64": "ctypes.c_double",
    "char": "ctypes.c_char",
    "void": "ctypes.c_void_p",
    "size_t": "ctypes.c_size_t",
    "FILE": "ctypes.c_void_p"
    }


def get_file_contents(file_name):
      infile = open(file_name)
      text = infile.readlines()
      infile.close()
      return text
      
def separate_comments(in_list):
    """
    >>> t1 = ''' /* "alo mundo" */ Feliz "/* Natal " /*para*/ "//todos" //mesmo '''
    >>> print separate_comments( [t1])
    (['  Feliz "/* Natal "  "//todos" \n'], ['/* "alo mundo" *//*para*///mesmo \n'])
    """
    comments = []
    code = []
    cl_token = "//"
    cs_token = "/*"
    ce_token = "*/"
    str_token = '"'
    line_comment = False
    multiline_comment = False
    inside_string = False
    for line in in_list:
        multi_start_index = -2 # avoid "/*/" corner case
        code_line = ""
        comment_line = ""
        line_comment = False
        spare = 0
        for index, char in enumerate(line.strip("\n")):
            spare -= 1 
            inside_comment = line_comment or multiline_comment
            if char == str_token and not inside_comment:
                inside_string = not inside_string
            twochar = line[index:index+2]
            if (twochar == cs_token and
                not inside_string and not line_comment):
                multiline_comment = True
                multi_start_index = index
            elif (twochar == ce_token and multiline_comment and
                index - multi_start_index > 1):
                multiline_comment = False
                spare = 2
            elif (twochar == cl_token and not inside_string
                and not multiline_comment):
                line_comment = True
            inside_comment = line_comment or multiline_comment
            if not inside_comment and spare <= 0:
                code_line += char
            else:
                comment_line += char
        comments.append(comment_line + "\n")
        code.append(code_line + "\n")
    return code, comments


def parse_structs(code):
    """
    This can't parse generic C structs - it depends of a 
    specifc formating as the one found on leptonica 1.6
    source files:
    no nested structs are allowed
    structs are always named
    structs are not instantiated on declaration (and more)
    """
    tokens = "".join(code).split()
    struct_level = 0
    kwd = "struct"
    
    bracket_level = 0
    structs = {}
    fwd = 1
    sequence = enumerate(tokens)
    while True:
        try:
            for _ in xrange(fwd):
                index, token = sequence.next()
            fwd = 1
        except StopIteration:
            break
        if (token == kwd and struct_level == 0 and
            tokens[index + 2] == "{"):
            bracket_level += 1
            struct_name = tokens[index + 1]
            struct_level = 1
            struct_body = []
            pre_reqs = set()
            decl_line = []
            fwd = 3
            continue
        if token == "{":
            bracket_level += 1
        elif token[0] == "}":
            bracket_level -= 1
        if struct_level  and bracket_level == 0:
            # use uppercase name: matching names used 
            # in leptonica's typedefs
            structs[struct_name.upper()] = (struct_body, pre_reqs)
            struct_level = 0
            continue
        if struct_level:
            decl_line.append(token)
        if struct_level and token[-1] in (";", ","):
            sep = token[-1]
            if len(token) == 1: #avoid need for the 
                                #separator to be joined to var_name
                decl_line.pop()
            var_name = decl_line[-1].strip(";").strip(",")
            if decl_line[0] == kwd:
                # Convert inner structs  to typedefed names
                var_type = decl_line[1].upper()
            else:
                var_type = " ".join(decl_line[:-1])
            if not var_type in lepton_types:
                pre_reqs.add(var_type)
            struct_body.append((var_name, var_type))
            if sep == ";":
                decl_line = []
            else:
                decl_line = [var_type]
    return structs    

# TODO: Parse the structures comments and add then as docstrings here.
class_template = '''\
class _%(name)s(ctypes.Structure):
    """%(comments)s
    """
    _fields_ = [
        %(rendered_fields)s
    ]

class %(name)s(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _%(name)s

'''
#If a  structure contains pointers to themselves, we need
# to declare the class, and set the fields afterwards

class_recurse_template = '''\
class _%(name)s(ctypes.Structure):
    """%(comments)s
    """
    pass

_%(name)s._fields_ = [
        %(rendered_fields)s
    ]

class %(name)s(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _%(name)s
'''

field_template = """("%(name)s", %(data_type)s)"""
def render_class(struct_name, body, recursive=False):
    template = class_template
    if recursive:
        template = class_recurse_template
    fields = []
    for field_name, data_type in body:
        if data_type in lepton_types:
            data_type = lepton_types[data_type]
            is_native_type = True
        else:
            is_native_type = False
        indirections = 0
        while field_name.startswith("*"):
            indirections += 1
            field_name = field_name[1:].strip()
            if data_type !=  lepton_types["void"] or indirections > 1:
                # FIXME: Maybe make the structures members also be our advanced
                # hybrid type? I think it is not needed
                if is_native_type:
                    data_type = "ctypes.POINTER(%s)" % data_type
                else:
                    data_type = "ctypes.POINTER(_%s)" % data_type
                    is_native_type = True
        rendered = field_template % {"name": field_name, 
            "data_type": ("_" if not is_native_type else "") + data_type}
        fields.append(rendered)
    rendered_fields = ",\n        ".join(fields)
    text = template % {"name": struct_name, 
        "comments": "Comments not generated",
        "rendered_fields": rendered_fields}
    return text

def parse_file(file_name):
    text = get_file_contents(file_name)
    code, comments = separate_comments(text)
    structs = parse_structs(code)
    return structs

file_template = """
# coding: utf-8
# Author: João S. O. Bueno
# This is a generated file - do not edit!

import ctypes
import weakref

class LeptonObject(object):
    def __new__(cls, *args):
        data = None
        if len(args) != 1:
            from leptonica_functions import functions
            if hasattr(functions, cls.__name__.lower() + "Create"):
                constructor = getattr(functions, cls.__name__.lower() +
                    "Create")
                return constructor(*args)
            data = cls._type_(*args)
            address = ctypes.addressof(data)
        else:
            address = args[0]
            if isinstance (address, ctypes.c_void_p):
                address = address.value
        if address in cls._instances_:
            return cls._instances_[address]()
        self = object.__new__(cls)
        self._address_ = ctypes.c_void_p(address)
        cls._instances_[address] = weakref.ref(self)
        if data:
            self._data_ = data
        return self

    def __repr__(self):
        repr_ = "Leptonica %%s object\\n" %% self.__class__.__name__
        if self._address_:
            for field in self._type_._fields_:
                repr_ += "    %%s: %%s,\\n" %% (field[0], getattr(self, field[0]))
        else:
            repr_ += "Not initiated or destroyed\\n"
        return repr_
    def __hash__(self):
        return self._address_.value
    
    def __del__(self):
        cls = self.__class__
        del cls._instances_[self._address_.value]
        from leptonica_functions import functions
        if hasattr(functions, cls.__name__.lower() + "Destroy"):
            destrutor = getattr(functions, cls.__name__.lower() + "Destroy")
            destrutor(ctypes.c_void_p(ctypes.addressof(self._address_)))

def property_factory(raw_structure, field_name):
    return  property(lambda s: getattr(
                        raw_structure.from_address(s._address_.value),
                        field_name),
                     lambda s, val: setattr(
                        raw_structure.from_address(s._address_.value),
                        field_name, val)
                    )

class MetaPointer(type): 
    def __new__(cls, name, bases, dic):
        base_struct = dic["_type_"]
        for field, type_ in base_struct._fields_:
            pr = property_factory(base_struct, field)
            dic[field] = pr
        dic["_instances_"] = {}
        return type(name, bases, dic)



%(classes)s

%(aliases)s

"""
def render_file(class_list, alias_list):
    aliases = "\n".join("%s = %s" % alias_pair 
        for alias_pair in alias_list)
    with open(target_file, "wt") as outfile:
        outfile.write(file_template % {"classes": "\n".join(class_list),
            "aliases": aliases} )
    
    

def order_classes(structs):
    class_list = []
    rendered = set()
    count = 0
    while True:
        if not structs:
            break
        # copy keys to a real list for p3k compatibility
        for struct in structs.keys()[:]:
            recursive = False
            pre_reqs = structs[struct][1]
            if struct in pre_reqs:
                pre_reqs = pre_reqs.copy()
                pre_reqs.remove(struct)
                recursive = True
            if not rendered.issuperset(pre_reqs) :
                if count > 100:
                    sys.stderr.write(str(pre_reqs) + "\n\n")
                    sys.stderr.write(str(rendered) + "\n")
                    raise Exception(
                        "Could not get Struct classes in order")
                continue
            class_list.append(render_class(struct, structs[struct][0],
                recursive))
            rendered.add(struct)
            del structs[struct]
        count += 1
    return class_list

def main(file_names):
    structs = {}
    for file_name in file_names:
        structs.update(parse_file(lepton_source_dir + file_name))
    # we are not reading the typedefs, just  ifering the tytpedsf from
    # the strcuture name, and there are  a few exceptions:
    irregular_names = (("BBUFFER", "BYTEBUFFER"), 
        ("DLLIST", "DOUBLELINKEDLIST"), 
        ("PIXCMAP", "DOUBLELINKEDLIST"),
        ("PIXAC", "PIXACOMP"), ("PIXC", "PIXCOMP")
    )
    class_list = order_classes(structs)
    render_file(class_list, irregular_names)


all_headers = ['bbuffer.h', 'dewarp.h', 'gplot.h', 'pix.h',
'regutils.h', 'bmf.h', 'heap.h', 'ptra.h', 'stack.h', 'bmp.h',
'list.h', 'queue.h', 'sudoku.h', 'array.h', 'ccbord.h', 'jbclass.h',
'morph.h', 'watershed.h']


if __name__ == "__main__":
    main(all_headers)
