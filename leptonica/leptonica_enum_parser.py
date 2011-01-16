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
This file parses the various enums in Leptonica's Header files
and make them available as convenient Python objects that can
be used by name in function calls
"""
import os
import re
from config import leptonica_home

lepton_source_dir = leptonica_home + "/src/"
target_file = "leptonica_enums.py"

def get_file_contents(filename):
    with open(os.path.join(lepton_source_dir, filename), "rt") as file_:
        return file_.read()

def get_comment_before(text, index):
    comment_start = text[:index].rfind("/*") # Is this TOO difficult, RE engine? 
    comment_end = text[comment_start:].find("*/") + 2 + comment_start
    return text[comment_start: comment_end], comment_start, comment_end 

def extract_enums(text):
    # Finds each enum block and up to 2 optional
    # comment blocks preceeding it
    # I mean -- this should be the reguklar expression for it, but it is simply failing
    # (as in IT DOES NOT WORK - it keeps being too greedy to retrieve the C comments
    # before the enums)
    #expr = re.compile(r"(/\*.*?\*/){0,1}[$\s]*?(/\*.*?\*/){0,1}[$\s]*?(enum\s+{.*?};)", re.MULTILINE | re.DOTALL)
    enums = []
    index = 0
    while True:
        next_enum = text[index:].find("\nenum") 
        if next_enum == -1:
            break
        next_enum += index
        enum_end = text[next_enum:].find("}") + next_enum
        enum_text = text[next_enum + 1: enum_end + 1]
        
        comment_text, comment_start, comment_end = get_comment_before(text, next_enum)
        if text[comment_end:next_enum].strip():
            # this comment does not belong to the enum found
            comment_text = ""
            second_comment = ""
        else:
            second_comment, _, second_comment_end = get_comment_before(text, comment_start)
            if text[second_comment_end: comment_start].strip():
                # this comment does not belong to the enum found
                second_comment = ""
        enums.append((second_comment, comment_text, enum_text))
        
        index = enum_end + 1
    return enums

def normalize_title(text):
    return text.strip("/*\n- ").split("\n")[0].strip("/*\n- ").lower().replace(" ","_")

def strip_asteriscs(text):
    new_text = ""
    for line in text.split("\n"):
        if len(line) > 2:
            new_text += line[2:] + "\n"
    return new_text

def extract_comment(text):
    if not "/*" in text or not "*/" in text:
        return ""
    return text.split("/*")[1].split("*/")[0].strip()

def parse_enum(enum):
    constants = []
    for line in enum.split("\n"):
        if not "=" in line:
            continue
        const = {}
        name, remainder = line.split("=", 1)
        const["name"] = name.strip()
        number = remainder.split(",")[0].split("/")[0].strip()
        const["value"] = int(number[2:],16) if number.startswith("0x") else int(number)
        const["doc"] = extract_comment(line)
        constants.append(const)
    return constants

class_template = """

class ConstType(Const):
    '''
       %(doc)s
    '''

ConstType.__name__ = "%(name)s"

%(constants)s

del ConstType

"""

field_template = """\
%(name)s = ConstType("%(name)s", %(value)s, '''%(doc)s ''')
"""

def render_fields(field_list):
    rendered_fields = []
    for field in field_list:
        rendered_fields.append(field_template % field)
    return "".join(rendered_fields)

def render_class(enum):
    contents = parse_enum(enum[2])
    if enum[0].strip():
        name = normalize_title(enum[0])
        doc = strip_asteriscs(enum[0]) + "\n" + strip_asteriscs(enum[1])
    elif enum[1].strip():
        name = normalize_title(enum[1])
        doc = strip_asteriscs(enum[1])
    else:
        name = "generated_constants"
        doc = ""
    doc += enum[2]
    rendered_fields = render_fields(contents)
    return class_template % {"doc": doc, "name": name, "constants": rendered_fields}

def render_classes(enums):
    classes = []
    for enum in enums:
        classes.append(render_class(enum))
    return "".join(classes)

file_template = """
# coding: utf-8
# Author: João S. O. Bueno
# This is a generated file - do not edit!


class Const(int):
    "Parent class to all constants"
    def __new__(cls, name, value, doc=""):
        self = int.__new__(cls, value)
        self.name = name
        self.doc = doc
        self.value = value 
        return self
    def __repr__(self):
        return self.name
    def __str__(self):
        return "%%s = %%s%%s" %% (self.name,self.value, ("  # " + self.doc) if self.doc else "")

def find_siblings(const, as_string=False):
    '''Helper function to locate blocks of related constants:
       i.e. the constants that used to live in the same "enum" in leptonica's C source files
    '''
    cls = const.__class__
    all_consts = [this_const for this_const in globals().values() if this_const.__class__ == cls]
    all_consts.sort()
    if not as_string:
        return all_consts
    return "\\n".join(str(const) for const in all_consts)
    
%s

globals_copy = globals().copy()
__all__ = [const for const in globals_copy if isinstance(const, Const)] + [find_siblings]

del const, globals_copy
"""

def render_file(enums):
    classes = render_classes(enums)
    with open(target_file, "wt") as file_:
        file_.write(file_template % classes)
    

def main():
    enums = []
    for filename in all_headers:
        contents = get_file_contents(filename)
        enums.extend(extract_enums(contents))
    render_file(enums)
        
all_headers = ['array.h', 'bmf.h', 'ccbord.h', 'environ.h', 'gplot.h', 'imageio.h', 'jbclass.h', 'morph.h', 'pix.h', 'ptra.h', 'readbarcode.h', 'sudoku.h']

if __name__ == "__main__":
    main ()