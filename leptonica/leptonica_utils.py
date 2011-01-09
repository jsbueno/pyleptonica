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

from PIL import Image
import leptonica_functions as lep
import ctypes
import struct

def pixToPILImage(lep_img, has_alpha=False):
    if not has_alpha:
        a = "\xff"
    if lep_img.d != 32:
        raise NotImplementedError ("Can only promote RGB or" 
            " RGBA images to PIL")
    buf = ctypes.create_string_buffer(lep_img.wpl * lep_img.h * 4)
    ctypes.memmove(buf, lep_img.data, lep_img.wpl * lep_img.h * 4)
    # And after this alwesomely fast byte copying...
    # we have to _reorder_ the bytes because lpetonica
    # uses the reversed order for them.--
    # moreover if the image uses no Alpha, all alpha bytes have
    # value 0 - while we want them to have 255 for PIL
    # FIXME: 
    # I don't want to add C parts to this module,
    # but maybe we should have a numpy dependent alternative
    # for this? Other ideas? Corepy? 
    for i in xrange(0,len(buf),4):
        if has_alpha:
            a = buf[i]
        r = buf[i + 3]
        g = buf[i + 2]
        b = buf[i + 1]
        buf[i] = r
        buf[i + 1] = g
        buf[i + 2] = b
        buf[i + 3] = a
    pil_img = Image.frombuffer( "RGBA", (lep_img.w, lep_img.h), buf,
        "raw", "RGBA", 0, 1)
    return pil_img
    

def PILImageToPix(pil_img):
    if pil_img.mode != "RGBA":
        raise NotImplementedError ("Can only promote RGBA" 
            " images to Leptonica")
    w, h = pil_img.size
    depth = 32
    lep_img = lep.PIX(w, h, depth)
    size = w * h
    img_data = pil_img.tostring()
    for i in xrange(0, len(img_data), 4):
        lep_img.data[i // 4] = struct.unpack(">I", img_data[i:i+4])[0]
    return lep_img

    
    