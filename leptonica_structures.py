
#coding: utf-8
# Author: João S. O. Bueno
# This is a generated file - do not edit!

import ctypes


class BOX(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("x", ctypes.c_int32),
        ("y", ctypes.c_int32),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("refcount", ctypes.c_uint32)
    ]



class SARRAY(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("refcount", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.POINTER(ctypes.c_char)))
    ]



class PIXCOLORMAP(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("array", ctypes.c_void_p),
        ("depth", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32)
    ]



class BYTEBUFFER(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("nwritten", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_ubyte))
    ]



class FPIX(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("wpl", ctypes.c_int32),
        ("refcount", ctypes.c_int32),
        ("xres", ctypes.c_int32),
        ("yres", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.c_float))
    ]



class RGBA_QUAD(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("blue", ctypes.c_ubyte),
        ("green", ctypes.c_ubyte),
        ("red", ctypes.c_ubyte),
        ("reserved", ctypes.c_ubyte)
    ]



class PTA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("refcount", ctypes.c_int32),
        ("x", ctypes.POINTER(ctypes.c_float)),
        ("y", ctypes.POINTER(ctypes.c_float))
    ]



class L_HEAP(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_void_p)),
        ("direction", ctypes.c_int32)
    ]



class PIX(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("w", ctypes.c_uint32),
        ("h", ctypes.c_uint32),
        ("d", ctypes.c_uint32),
        ("wpl", ctypes.c_uint32),
        ("refcount", ctypes.c_uint32),
        ("xres", ctypes.c_uint32),
        ("yres", ctypes.c_uint32),
        ("informat", ctypes.c_int32),
        ("text", ctypes.POINTER(ctypes.c_char)),
        ("colormap", ctypes.POINTER(PIXCOLORMAP)),
        ("data", ctypes.POINTER(ctypes.c_uint32))
    ]



class SEL(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("sy", ctypes.c_int32),
        ("sx", ctypes.c_int32),
        ("cy", ctypes.c_int32),
        ("cx", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.POINTER(ctypes.c_int32))),
        ("name", ctypes.POINTER(ctypes.c_char))
    ]



class L_REGPARAMS(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("fp", ctypes.c_void_p),
        ("argv", ctypes.POINTER(ctypes.POINTER(ctypes.c_char))),
        ("success", ctypes.c_int32),
        ("display", ctypes.c_int32)
    ]



class BOXA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("refcount", ctypes.c_uint32),
        ("box", ctypes.POINTER(ctypes.POINTER(BOX)))
    ]



class DPIX(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("wpl", ctypes.c_int32),
        ("refcount", ctypes.c_int32),
        ("xres", ctypes.c_int32),
        ("yres", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.c_double))
    ]



class DOUBLELINKEDLIST(ctypes.Structure):
    """Comments not generated
    """
    pass

DOUBLELINKEDLIST._fields_ = [
        ("prev", ctypes.POINTER(DOUBLELINKEDLIST)),
        ("next", ctypes.POINTER(DOUBLELINKEDLIST)),
        ("data", ctypes.c_void_p)
    ]


class L_SUDOKU(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("num", ctypes.c_int32),
        ("locs", ctypes.POINTER(ctypes.c_int32)),
        ("current", ctypes.c_int32),
        ("init", ctypes.POINTER(ctypes.c_int32)),
        ("state", ctypes.POINTER(ctypes.c_int32)),
        ("nguess", ctypes.c_int32),
        ("finished", ctypes.c_int32),
        ("failure", ctypes.c_int32)
    ]



class NUMA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("refcount", ctypes.c_int32),
        ("startx", ctypes.c_float),
        ("delx", ctypes.c_float),
        ("array", ctypes.POINTER(ctypes.c_float))
    ]



class BOXAA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("boxa", ctypes.POINTER(ctypes.POINTER(BOXA)))
    ]



class L_STACK(ctypes.Structure):
    """Comments not generated
    """
    pass

L_STACK._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_void_p)),
        ("auxstack", ctypes.POINTER(L_STACK))
    ]


class L_PTRA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("imax", ctypes.c_int32),
        ("nactual", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_void_p))
    ]



class L_KERNEL(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("sy", ctypes.c_int32),
        ("sx", ctypes.c_int32),
        ("cy", ctypes.c_int32),
        ("cx", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.POINTER(ctypes.c_float)))
    ]



class BMP_FILEHEADER(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("bfType", ctypes.c_int16),
        ("bfSize", ctypes.c_int16),
        ("bfFill1", ctypes.c_int16),
        ("bfReserved1", ctypes.c_int16),
        ("bfReserved2", ctypes.c_int16),
        ("bfOffBits", ctypes.c_int16),
        ("bfFill2", ctypes.c_int16)
    ]



class L_PTRAA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("ptra", ctypes.POINTER(ctypes.POINTER(L_PTRA)))
    ]



class SELA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("sel", ctypes.POINTER(ctypes.POINTER(SEL)))
    ]



class BMP_INFOHEADER(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("biSize", ctypes.c_int32),
        ("biWidth", ctypes.c_int32),
        ("biHeight", ctypes.c_int32),
        ("biPlanes", ctypes.c_int16),
        ("biBitCount", ctypes.c_int16),
        ("biCompression", ctypes.c_int32),
        ("biSizeImage", ctypes.c_int32),
        ("biXPelsPerMeter", ctypes.c_int32),
        ("biYPelsPerMeter", ctypes.c_int32),
        ("biClrUsed", ctypes.c_int32),
        ("biClrImportant", ctypes.c_int32)
    ]



class NUMAA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("numa", ctypes.POINTER(ctypes.POINTER(NUMA)))
    ]



class L_DEWARP(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pixs", ctypes.POINTER(PIX)),
        ("pixd", ctypes.POINTER(PIX)),
        ("sampvdispar", ctypes.POINTER(FPIX)),
        ("samphdispar", ctypes.POINTER(FPIX)),
        ("fullvdispar", ctypes.POINTER(FPIX)),
        ("fullhdispar", ctypes.POINTER(FPIX)),
        ("naflats", ctypes.POINTER(NUMA)),
        ("nacurves", ctypes.POINTER(NUMA)),
        ("pageno", ctypes.c_int32),
        ("sampling", ctypes.c_int32),
        ("minlines", ctypes.c_int32),
        ("applyhoriz", ctypes.c_int32),
        ("nx", ctypes.c_int32),
        ("ny", ctypes.c_int32),
        ("extraw", ctypes.c_int32),
        ("success", ctypes.c_int32)
    ]



class PIXCOMP(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("d", ctypes.c_int32),
        ("xres", ctypes.c_uint32),
        ("yres", ctypes.c_uint32),
        ("comptype", ctypes.c_int32),
        ("text", ctypes.POINTER(ctypes.c_char)),
        ("cmapflag", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.c_ubyte)),
        ("size", ctypes.c_int32)
    ]



class PTAA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("pta", ctypes.POINTER(ctypes.POINTER(PTA)))
    ]



class GPLOT(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("rootname", ctypes.POINTER(ctypes.c_char)),
        ("cmdname", ctypes.POINTER(ctypes.c_char)),
        ("cmddata", ctypes.POINTER(SARRAY)),
        ("datanames", ctypes.POINTER(SARRAY)),
        ("plotdata", ctypes.POINTER(SARRAY)),
        ("plottitles", ctypes.POINTER(SARRAY)),
        ("plotstyles", ctypes.POINTER(NUMA)),
        ("nplots", ctypes.c_int32),
        ("outname", ctypes.POINTER(ctypes.c_char)),
        ("outformat", ctypes.c_int32),
        ("scaling", ctypes.c_int32),
        ("title", ctypes.POINTER(ctypes.c_char)),
        ("xlabel", ctypes.POINTER(ctypes.c_char)),
        ("ylabel", ctypes.POINTER(ctypes.c_char))
    ]



class NUMA2D(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nrows", ctypes.c_int32),
        ("ncols", ctypes.c_int32),
        ("initsize", ctypes.c_int32),
        ("numa", ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(NUMA))))
    ]



class NUMAHASH(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nbuckets", ctypes.c_int32),
        ("initsize", ctypes.c_int32),
        ("numa", ctypes.POINTER(ctypes.POINTER(NUMA)))
    ]



class PIXTILING(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pix", ctypes.POINTER(PIX)),
        ("nx", ctypes.c_int32),
        ("ny", ctypes.c_int32),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("xoverlap", ctypes.c_int32),
        ("yoverlap", ctypes.c_int32),
        ("strip", ctypes.c_int32)
    ]



class PIXA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("refcount", ctypes.c_uint32),
        ("pix", ctypes.POINTER(ctypes.POINTER(PIX))),
        ("boxa", ctypes.POINTER(BOXA))
    ]



class PIXACC(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("offset", ctypes.c_int32),
        ("pix", ctypes.POINTER(PIX))
    ]



class CCBORD(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pix", ctypes.POINTER(PIX)),
        ("boxa", ctypes.POINTER(BOXA)),
        ("start", ctypes.POINTER(PTA)),
        ("refcount", ctypes.c_int32),
        ("local", ctypes.POINTER(PTAA)),
        ("global", ctypes.POINTER(PTAA)),
        ("step", ctypes.POINTER(NUMAA)),
        ("splocal", ctypes.POINTER(PTA)),
        ("spglobal", ctypes.POINTER(PTA))
    ]



class PIXACOMP(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("pixc", ctypes.POINTER(ctypes.POINTER(PIXCOMP))),
        ("boxa", ctypes.POINTER(BOXA))
    ]



class JBDATA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pix", ctypes.POINTER(PIX)),
        ("npages", ctypes.c_int32),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("nclass", ctypes.c_int32),
        ("latticew", ctypes.c_int32),
        ("latticeh", ctypes.c_int32),
        ("naclass", ctypes.POINTER(NUMA)),
        ("napage", ctypes.POINTER(NUMA)),
        ("ptaul", ctypes.POINTER(PTA))
    ]



class L_QUEUE(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("nhead", ctypes.c_int32),
        ("nelem", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_void_p)),
        ("stack", ctypes.POINTER(L_STACK))
    ]



class CCBORDA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pix", ctypes.POINTER(PIX)),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("ccb", ctypes.POINTER(ctypes.POINTER(CCBORD)))
    ]



class L_BMF(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pixa", ctypes.POINTER(PIXA)),
        ("size", ctypes.c_int32),
        ("directory", ctypes.POINTER(ctypes.c_char)),
        ("baseline1", ctypes.c_int32),
        ("baseline2", ctypes.c_int32),
        ("baseline3", ctypes.c_int32),
        ("lineheight", ctypes.c_int32),
        ("kernwidth", ctypes.c_int32),
        ("spacewidth", ctypes.c_int32),
        ("vertlinesep", ctypes.c_int32),
        ("fonttab", ctypes.POINTER(ctypes.c_int32)),
        ("baselinetab", ctypes.POINTER(ctypes.c_int32)),
        ("widthtab", ctypes.POINTER(ctypes.c_int32))
    ]



class PIXAA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("pixa", ctypes.POINTER(ctypes.POINTER(PIXA))),
        ("boxa", ctypes.POINTER(BOXA))
    ]



class L_WSHED(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pixs", ctypes.POINTER(PIX)),
        ("pixm", ctypes.POINTER(PIX)),
        ("mindepth", ctypes.c_int32),
        ("pixlab", ctypes.POINTER(PIX)),
        ("pixt", ctypes.POINTER(PIX)),
        ("lines8", ctypes.POINTER(ctypes.c_void_p)),
        ("linem1", ctypes.POINTER(ctypes.c_void_p)),
        ("linelab32", ctypes.POINTER(ctypes.c_void_p)),
        ("linet1", ctypes.POINTER(ctypes.c_void_p)),
        ("pixad", ctypes.POINTER(PIXA)),
        ("ptas", ctypes.POINTER(PTA)),
        ("nasi", ctypes.POINTER(NUMA)),
        ("nash", ctypes.POINTER(NUMA)),
        ("namh", ctypes.POINTER(NUMA)),
        ("nalevels", ctypes.POINTER(NUMA)),
        ("nseeds", ctypes.c_int32),
        ("nother", ctypes.c_int32),
        ("lut", ctypes.POINTER(ctypes.c_int32)),
        ("links", ctypes.POINTER(ctypes.POINTER(NUMA))),
        ("arraysize", ctypes.c_int32),
        ("debug", ctypes.c_int32)
    ]



class JBCLASSER(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("safiles", ctypes.POINTER(SARRAY)),
        ("method", ctypes.c_int32),
        ("components", ctypes.c_int32),
        ("maxwidth", ctypes.c_int32),
        ("maxheight", ctypes.c_int32),
        ("npages", ctypes.c_int32),
        ("baseindex", ctypes.c_int32),
        ("nacomps", ctypes.POINTER(NUMA)),
        ("sizehaus", ctypes.c_int32),
        ("rankhaus", ctypes.c_float),
        ("thresh", ctypes.c_float),
        ("weightfactor", ctypes.c_float),
        ("naarea", ctypes.POINTER(NUMA)),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("nclass", ctypes.c_int32),
        ("keep_pixaa", ctypes.c_int32),
        ("pixaa", ctypes.POINTER(PIXAA)),
        ("pixat", ctypes.POINTER(PIXA)),
        ("pixatd", ctypes.POINTER(PIXA)),
        ("nahash", ctypes.POINTER(NUMAHASH)),
        ("nafgt", ctypes.POINTER(NUMA)),
        ("ptac", ctypes.POINTER(PTA)),
        ("ptact", ctypes.POINTER(PTA)),
        ("naclass", ctypes.POINTER(NUMA)),
        ("napage", ctypes.POINTER(NUMA)),
        ("ptaul", ctypes.POINTER(PTA)),
        ("ptall", ctypes.POINTER(PTA))
    ]



BBUFFER = BYTEBUFFER
DLLIST = DOUBLELINKEDLIST
PIXCMAP = DOUBLELINKEDLIST
PIXAC = PIXACOMP
PIXC = PIXCOMP

