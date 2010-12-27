# -*- coding: utf-8 -*-
import ctypes

# from ctypes import c_* #invlaid python, so we do this:
globals().update((name, getattr(ctypes, name)) for name in dir(ctypes) if name.startswith("c_"))

lep = ctypes.cdll.LoadLibrary( "liblept.so")


class PIX(ctypes.Structure):
    """
    struct Pix
    {
        l_uint32             w;           /* width in pixels                   */
        l_uint32             h;           /* height in pixels                  */
        l_uint32             d;           /* depth in bits                     */
        l_uint32             wpl;         /* 32-bit words/line                 */
        l_uint32             refcount;    /* reference count (1 if no clones)  */
        l_uint32             xres;        /* image res (ppi) in x direction    */
                                          /* (use 0 if unknown)                */
        l_uint32             yres;        /* image res (ppi) in y direction    */
                                          /* (use 0 if unknown)                */
        l_int32              informat;    /* input file format, IFF_*          */
        char                *text;        /* text string associated with pix   */
        struct PixColormap  *colormap;    /* colormap (may be null)            */
        l_uint32            *data;        /* the image data                    */
    };"""
    _fields_ = [
        ("w", c_uint32),
        ("h", c_uint32),
        ("d", c_uint32),
        ("wpl", c_uint32),
        ("refcount", c_uint32),
        ("xres", c_uint32),
        ("yres", c_uint32),
        ("informat", c_uint32),
        ("text", c_char_p),
        ("colormap", c_void_p), #TODO: PixColormap struct
        ("data", ctypes.POINTER(c_ubyte))]

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
         a,b,g,r = (img.data[y * img.wpl * 4+ 4 * x + i] for i in (0,1,2,3))
         sc.set_at((x,y), (r,g,b,a))
   
    pygame.display.flip()
    raw_input()
    pygame.quit()

