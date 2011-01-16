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
import ctypes

# SARRAY

def __getitem__(self, item):
    if isinstance(item, slice):
        lst = []
        for index in xrange(*item.indices(self.n)):
            lst.append(self[index])
        return lst
    if not (-self.n <= item < self.n):
        raise IndexError
    if item < 0:
        item += self.n
    return ctypes.string_at(ctypes.cast(self.array[item], ctypes.c_char_p))

def __len__(self):
    return self.n

structures.SARRAY.__getitem__ = __getitem__
structures.SARRAY.__len__ = __len__

del __getitem__, __len__