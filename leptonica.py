# -*- coding: utf-8 -*-
import ctypes
import struct
from lepton_ctypes import PIX

# from ctypes import c_* #invlaid python, so we do this:
globals().update((name, getattr(ctypes, name)) for name in dir(ctypes) if name.startswith("c_"))

lep = ctypes.cdll.LoadLibrary( "liblept.so")



def getPix(pointer):
    if pointer is None:
        raise TypeError("Failed to obtain image")
    return PIX.from_address(pointer)

lep.pixRead.argtypes=[ctypes.c_char_p]
lep.pixRead.restype = getPix

if __name__ == "__main__":
    import sys
    import pygame
    if len(sys.argv) < 2:
        sys.stderr.write ("Pass an image filename for testing")
        sys.exit(1)
    img = lep.pixRead(sys.argv[1]) #("/home/gwidion/teste3.png")
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

