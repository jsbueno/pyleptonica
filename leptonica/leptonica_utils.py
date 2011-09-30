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
This file puts some utility functions, mostly for converting from
and to leptonica used types
"""

import leptonica_functions as lep
import ctypes
import struct

try:
    from PIL import Image
except ImportError:
    ok = False
else:
    ok = True
    
def pixToPILImage(pixs, has_alpha=False):
    if pixs.d != 32:
        raise TypeError("Currently this only works for 24 or 32 bit images")
    #Swap image Bytes
    le_pix = lep.functions.pixEndianByteSwapNew(pixs)
    
    # Some ctypes black magic to get the right types
    data_pointer =  ctypes.cast(le_pix.data, ctypes.POINTER(  ctypes.c_uint32 * (le_pix.w * le_pix.h)))
    # before beeing able to  create a functioning 
    # buffer object from the image data:
    img_buffer = buffer(data_pointer.contents)
    pil_img = Image.frombuffer( "RGBA", (pixs.w, pixs.h), img_buffer,
        "raw", "RGBA", 0, 1)
    # However, this buffer will be destroyed when this function ends - so
    # we must copy the data around once more, even when keeping the same (RGBA) mode
    mode = "RGBA" if has_alpha else "RGB"
    return pil_img.convert(mode)
    

def PILImageToPix(pil_img):
    if pil_img.mode != "RGBA":
        pil_img = pil_img.convert("RGBA")
    w, h = pil_img.size
    depth = 32
    lep_img = lep.PIX(w, h, depth)
    size = w * h
    img_data = pil_img.tostring()
    # ctypes miss a way to get the string buffer as  a memory read source
    interm_buffer = ctypes.c_buffer(img_data)
    ctypes.memmove(lep_img.data, interm_buffer, len(img_data))
    lep.functions.pixEndianByteSwap(lep_img)    
    # Normally in Leptonica the alpha byte is set to "zero"
    # I am betting there is no problem leaving the same value
    # that comes from PIL (255 for opaque) for non transaprency use in
    # leptonica
    return lep_img

if ok:
    __all__ = ["PILImageToPix", "pixToPILImage"]
else:
    __all__ = []
del ok


