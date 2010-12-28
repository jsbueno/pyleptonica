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


import ctypes
import struct
#from leptonica_structures import PIX
import leptonica_functions as lep

# from ctypes import c_* #invalid python, so we do this:
globals().update((name, getattr(ctypes, name)) for name in dir(ctypes) if name.startswith("c_"))

#lep = ctypes.cdll.LoadLibrary("liblept.so")



#def getPix(pointer):
    #if pointer is None:
        #raise TypeError("Failed to obtain image")
    #return PIX.from_address(pointer)

#lep.pixRead.argtypes=[ctypes.c_char_p]
#lep.pixRead.restype = getPix

if __name__ == "__main__":
    import sys
    import pygame
    if len(sys.argv) < 2:
        sys.stderr.write ("Pass an image filename for testing")
        sys.exit(1)
    img = lep.readfile.pixRead(sys.argv[1]) #("/home/gwidion/teste3.png")
    sc = pygame.display.set_mode((img.w, img.h))
    for y in xrange(img.h):
      for x in xrange(img.w):
         color_int = img.data[y * img.wpl + x]
         # Fake big endian, to retrieve the data in the order needed for pygame
         color_str = struct.pack(">I", color_int)
         color_tup = struct.unpack("BBBB", color_str)
         sc.set_at((x,y), color_tup)
   
    pygame.display.flip()
    raw_input()
    pygame.quit()

