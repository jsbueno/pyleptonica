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
def property_wrapper_factory(old_property, cloner = None):
    """Wraps a previous object property - (that used
       to access a value through the structure field pointed
       by the _adress_ member ) with a new one
       that effectvely yields a Python leptonica object out of 
       the pointer recorded there, keeping track of the  reference counts
       
       ATM there is no setter - we will come to that when needed. 
       (probably PIXCMAP in PIX objects)
    """
    def new_getter(self):
        b_ = old_property.__get__(self, self.__class__)
        obj = structures.BOXA(from_address=ctypes.cast(b_, ctypes.c_void_p))
        if not cloner:
            obj.refcount += 1
            return obj
        obj._needs_del = False
        new_obj = cloner(obj)    
        return new_obj
    return property(new_getter)

# SARRAY
sarray_getter = lambda obj, index: ctypes.string_at(ctypes.cast(obj.array[index],
                                    ctypes.c_char_p))


structures.SARRAY.__getitem__ = lambda self, index: _getitem(sarray_getter, self, index)
structures.SARRAY.__len__ = _len

# PIXA
def _real_pixa_set_item(self, index, value):
    if not isinstance(value, structures.PIX):
        raise TypeError
    clone = functions.pixClone(value)
    clone._needs_del = False
    pointer = ctypes.cast(clone._address_, ctypes.POINTER(structures._PIX))
    self.pix[index] = pointer

def __setitem__(self, index, value):
    if not (-self.n < index <= self.n):
        raise IndexError
    if index < 0:
        index += self.n
    old_pix = structures.PIX(from_address=ctypes.cast(self.pix[index], ctypes.c_void_p))
    self.pix[index] = None
    del old_pix
    _real_pixa_set_item(self, index, value)


def append(self, value):
    if self.n >= self.nalloc:
        raise IndexError("PIXA Object at maximum capacity (%d) " % self.nalloc)
    self.n += 1
    _real_pixa_set_item(self, self.n - 1, value)

def pixa_getter(self, index):
    value = structures.PIX(from_address=ctypes.cast(self.pix[index],
            ctypes.c_void_p) )
    value._needs_del = False
    return functions.pixClone(value)


    
structures.PIXA.__getitem__ = lambda self, index: _getitem(pixa_getter, self, index)
structures.PIXA.append = append
structures.PIXA.__setitem__ = __setitem__
structures.PIXA.boxa = property_wrapper_factory(structures.PIXA.boxa)
structures.PIXA.__len__ = _len

del __setitem__, append

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


