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
   Structures Patcher: 
        This file is loaded after the automatically generated structures file
        and manually (monkey) patches some of them so that  they behave in
        a more pythonic way, in ways that would not be possible
        to do authomatically.

        Subject to grow with time
"""

import leptonica_structures as structures
from leptonica_functions import functions, pix3
import ctypes

def _getitem(getter, obj, index):
    if isinstance(index, slice):
        lst = []
        for n_index in xrange(*index.indices(obj.n)):
            lst.append(obj[n_index])
        return lst
    if not (-obj.n <= index < obj.n):
        raise IndexError
    if index < 0:
        index += obj.n
    return getter(obj, index)

def _len(self):
    return self.n

#FIXME: this  maybe can be automatized

def get_cloner_destrutor(type_):
    name = type.__name__.lower()
    cloner_name = name + "Clone"
    destrutor_name = name + "Destroy"
    return getattr(functions, cloner_name, None), getattr(functions, destrutor_name, None)

def property_wrapper_factory(old_property, ref_type):
    """Wraps a previous object property - (that used
       to access a value through the structure field pointed
       by the _adress_ member ) with a new one
       that effectvely yields a Python leptonica object out of 
       the pointer recorded there, keeping track of the  reference counts
       
       ATM there is no setter - we will come to that when needed. 
       (probably PIXCMAP in PIX objects)
    """
    cloner, destrutor = get_cloner_destrutor(ref_type)
    def new_getter(self):
        b_ = old_property.__get__(self, self.__class__)
        obj = ref_type(from_address=ctypes.cast(b_, ctypes.c_void_p))
        if not cloner:
            if hasattr(obj, "refcount"):
                obj.refcount += 1
            return obj
        obj._needs_del = False
        new_obj = cloner(obj)    
        return new_obj
    def new_setter(self, value):
        if not isinstance(value, ref_type):
            raise TypeError("This attribute must be of type %s " % ref_type)
        raw_type = getattr(structures, "_" + ref_type.__name__)
        #raw_structure = raw_type.from_address(self._address_.value)
        #del previous instance:
        b_ = old_property.__get__(self, self.__class__)
        # When instancing a Python object with "from address"
        # refcount is not increased
        obj = ref_type(from_address=ctypes.cast(b_, ctypes.c_void_p))
        del obj
        if cloner:
            new_obj = cloner(value)
            new_obj._needs_del = False
        else:
            # Python won't call "__del__"  on new_obj just aliased to value
            # (cpython 2.6) 
            new_obj = value
            if hasattr(value, "refcount"):
                value.refcount += 1
        pointer = ctypes.cast(new_obj._address_, ctypes.POINTER(raw_type))
        old_property.__set__(self, pointer)
        
    return property(new_getter, new_setter)

# TODO: 
# build these wrappers straight into the genrated classes
def rewrap_leptonica_fields():
    """This function looks into all Python objects defined in 
    leptonica structures, and for each field (atttribute) that
    holds a referene to another leptonica object (in the original C,
    a simple pointer), rewrapps the access to this field on
    the high level class so that an actual Python instance
    of the equivalent object can be used to get/set the field
    
    These higher level acessors also take care of the reference counting
    """
    for cls_name in structures.__dict__.keys():
        #Filter only the pairs for low level/high level structures:
        if cls_name.startswith("_") or ("_" + cls_name) not in structures.__dict__:
            continue
        
        hi_cls = structures.__dict__[cls_name]
        lo_cls = structures.__dict__["_" + cls_name]
        for f_name, f_type in lo_cls._fields_:
            type_name = f_type.__name__
            if not type_name.startswith("LP_"):
                continue
            if not type_name[3:] in structures.__dict__:
                continue
            #now, this field 
            # which is already a generated property
            #should be wrapped with a new property fot the high level access
            prop_cls = structures.__dict__[type_name[4:]]
            setattr(hi_cls, f_name,
                property_wrapper_factory(getattr(hi_cls, f_name), prop_cls))

rewrap_leptonica_fields()


# Classes that reference an array of other object type
# and have to be customized to deal with it:

#
#['PIXACOMP', 'SARRAY', 'BOXA', 'PIXCOLORMAP', 'BYTEBUFFER', 'PTA', 'CCBORDA', 'L_HEAP', 'PTAA', 'PIXAA', 'PIXA', 'L_STACK', 'L_PTRA', 'L_PTRAA', 'L_QUEUE', 'NUMA', 'BOXAA', 'SELA', 'NUMAA']
#


# SARRAY
sarray_getter = lambda obj, index: ctypes.string_at(ctypes.cast(obj.array[index],
                                    ctypes.c_char_p))


structures.SARRAY.__getitem__ = lambda self, index: _getitem(sarray_getter, self, index)
structures.SARRAY.__len__ = _len

# Others:

def make_sequence(cls, field_name):
    cls_name = cls.__name__
    cloner, destrutor = get_cloner_destrutor(cls)
    elem_type_name = dict(getattr(getattr(structures, "_" + cls_name),
        "_fields_"))[field_name].__name__[len("LP_LP__"):]
    elem_type = getattr(structures, elem_type_name)
    raw_elem_type = getattr(structures, "_" + elem_type_name)
    
    def _real_set_item(self, index, value):
        if not isinstance(value, elem_type):
            raise TypeError("Element of %s must be a %s " % (field_name, elem_type))
        if cloner:
            clone = cloner(value)
            clone._needs_del = False
        else:
            clone = value
            if hasattr(value, "refcount"):
                value.refcount += 1
        pointer = ctypes.cast(clone._address_, ctypes.POINTER(raw_elem_type))
        getattr(self, field_name)[index] = pointer

    def __setitem__(self, index, value):
        if not (-self.n < index <= self.n):
            raise IndexError
        if index < 0:
            index += self.n
        old_value = elem_type(from_address=ctypes.cast(
                                getattr(self,field_name)[index], 
                                ctypes.c_void_p))
        #Important - if C's leptonica destructor is called on
        # an object that has one ctypes.POINTER object
        # referencing it (the objects with "LP_" in their names)
        # we get a segmentation fault:
        getattr(self, field_name)[index] = None
        del old_value
        #non local function:
        _real_set_item(self, index, value)

    def append(self, value):
        if self.n >= self.nalloc:
            raise IndexError("%s Object at maximum capacity (%d) " %
                                (cls_name ,self.nalloc))
        self.n += 1
        _real_set_item(self, self.n - 1, value)

    def getter(self, index):
        value = elem_type(from_address=ctypes.cast(getattr(self,field_name)[index],
                ctypes.c_void_p))
        if cloner:
            value._needs_del = False
            return cloner(value)
        if hasattr(value, "refcount"):
            value.refcount += 1
        return value

    setattr(cls, "__getitem__", lambda s, index: _getitem(getter, s, index))
    setattr(cls, "append", append)
    setattr(cls,"__setitem__", __setitem__)
    setattr(cls, "__len__", _len)

# Exceptions (some of these just happen to have non-leptonica types
# as their elements:
#( PIXCOLORMAP ( BYTEBUFFER ( PTA ( L_HEAP ( ( L_STACK ( L_PTRA ( L_QUEUE ( NUMA (

all_classes = [
( "PIXACOMP" , "pixc" ), # LP_LP__PIXCOMP
( "BOXA" , "box" ), # LP_LP__BOX
( "CCBORDA" , "ccb" ), # LP_LP__CCBORD
( "PTAA" , "pta" ), # LP_LP__PTA
( "PIXAA" , "pixa" ), # LP_LP__PIXA
( "PIXA" , "pix" ), # LP_LP__PIX
( "L_PTRAA" , "ptra" ), # LP_LP__L_PTRA
( "BOXAA" , "boxa" ), # LP_LP__BOXA
( "SELA" , "sel" ), # LP_LP__SEL
( "NUMAA" , "numa" ), # LP_LP__NUMA
]

for cls, field in all_classes:
    make_sequence(getattr(structures, cls), field)

#FIXME: move to function patches when that exists
# fix pixInvert
# (It is more likely pixInvert should increment the reference count)
# if there are other "inplace" functions
# that return a clone with no increase in refcount, we have
# to apply the same wrapper.
from functools import wraps
originalPixInvert = pix3.pixInvert
@staticmethod
@wraps(functions.pixInvert)
def pixInvert(pixd, pixs):
    res = originalPixInvert(pixd, pixs)
    if not pixd:
        #pixInvert returns a new PIX and everything is fine
        return res
    #pixInvert returns an instance of an already existing PIX, with no increase in refcount
    res._needs_del = False
    return functions.pixClone(res)

functions.pixInvert = pixInvert
pix3.pixInvert = pixInvert


