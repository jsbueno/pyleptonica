
# coding: utf-8
# Author: João S. O. Bueno
# This is a generated file - do not edit!

import ctypes
#import weakref

class LeptonObject(object):
    def __new__(cls, *args, **kw):
        """
        Constructor for structure types.
        Call with named argument "from_address" to
        point it to an existing structure in memory, 
        else it will try to automatically call Leptonica's
        constructor for this structure
        """
        data = None
        if not kw or not "from_address" in kw:
            from leptonica_functions import functions
            if hasattr(functions, cls.__name__.lower() + "Create"):
                constructor = getattr(functions, cls.__name__.lower() +
                    "Create")
                return constructor(*args)
            data = cls._type_(*args)
            address = ctypes.addressof(data)
        else:
            address = kw["from_address"]
            if isinstance (address, ctypes.c_void_p):
                address = address.value
        #if address in cls._instances_:
        #    return cls._instances_[address]()
        self = object.__new__(cls)
        self._needs_del = True
        self._address_ = ctypes.c_void_p(address)
        #cls._instances_[address] = weakref.ref(self)
        if data:
            self._data_ = data
        return self
    def __getattribute__(self, attr):
        if attr in ("_address_", "refcount"):
            return object.__getattribute__(self, attr)
        if not self._address_:
            raise ValueError("Object no longer exists")
        if self.refcount < 1:
            self._address_ = ctypes.c_void_p(None)
            raise ValueError("Object no longer exists")
        return object.__getattribute__(self, attr)

    def __repr__(self):
        repr_ = "Leptonica %s object\n" % self.__class__.__name__
        if self._address_:
            for field in self._type_._fields_:
                repr_ += "    %s: %s,\n" % (field[0], getattr(self, field[0]))
        else:
            repr_ += "Not initiated or destroyed\n"
        return repr_
    def __hash__(self):
        return self._address_.value
    
    def __del__(self):
        cls = self.__class__
        #if self._address_:
        #    del cls._instances_[self._address_.value]
        from leptonica_functions import functions
        if self._needs_del and hasattr(functions, cls.__name__.lower() + "Destroy"):
            destrutor = getattr(functions, cls.__name__.lower() + "Destroy")
            destrutor(ctypes.c_void_p(ctypes.addressof(self._address_)))

def property_factory(raw_structure, field_name):
    return  property(lambda s: getattr(
                        raw_structure.from_address(s._address_.value),
                        field_name),
                     lambda s, val: setattr(
                        raw_structure.from_address(s._address_.value),
                        field_name, val)
                    )

class MetaPointer(type): 
    def __new__(cls, name, bases, dic):
        base_struct = dic["_type_"]
        for field, type_ in base_struct._fields_:
            pr = property_factory(base_struct, field)
            dic[field] = pr
        #dic["_instances_"] = {}
        return type(name, bases, dic)



class _BOX(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("x", ctypes.c_int32),
        ("y", ctypes.c_int32),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("refcount", ctypes.c_uint32)
    ]

class BOX(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _BOX


class _SARRAY(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("refcount", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.POINTER(ctypes.c_char)))
    ]

class SARRAY(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _SARRAY


class _PIXCOLORMAP(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("array", ctypes.c_void_p),
        ("depth", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32)
    ]

class PIXCOLORMAP(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _PIXCOLORMAP


class _BYTEBUFFER(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("nwritten", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_ubyte))
    ]

class BYTEBUFFER(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _BYTEBUFFER


class _FPIX(ctypes.Structure):
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

class FPIX(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _FPIX


class _RGBA_QUAD(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("blue", ctypes.c_ubyte),
        ("green", ctypes.c_ubyte),
        ("red", ctypes.c_ubyte),
        ("reserved", ctypes.c_ubyte)
    ]

class RGBA_QUAD(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _RGBA_QUAD


class _PTA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("refcount", ctypes.c_int32),
        ("x", ctypes.POINTER(ctypes.c_float)),
        ("y", ctypes.POINTER(ctypes.c_float))
    ]

class PTA(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _PTA


class _L_HEAP(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_void_p)),
        ("direction", ctypes.c_int32)
    ]

class L_HEAP(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _L_HEAP


class _PIX(ctypes.Structure):
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
        ("colormap", ctypes.POINTER(_PIXCOLORMAP)),
        ("data", ctypes.POINTER(ctypes.c_uint32))
    ]

class PIX(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _PIX


class _SEL(ctypes.Structure):
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

class SEL(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _SEL


class _L_REGPARAMS(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("fp", ctypes.c_void_p),
        ("argv", ctypes.POINTER(ctypes.POINTER(ctypes.c_char))),
        ("success", ctypes.c_int32),
        ("display", ctypes.c_int32)
    ]

class L_REGPARAMS(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _L_REGPARAMS


class _BOXA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("refcount", ctypes.c_uint32),
        ("box", ctypes.POINTER(ctypes.POINTER(_BOX)))
    ]

class BOXA(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _BOXA


class _DPIX(ctypes.Structure):
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

class DPIX(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _DPIX


class _DOUBLELINKEDLIST(ctypes.Structure):
    """Comments not generated
    """
    pass

_DOUBLELINKEDLIST._fields_ = [
        ("prev", ctypes.POINTER(_DOUBLELINKEDLIST)),
        ("next", ctypes.POINTER(_DOUBLELINKEDLIST)),
        ("data", ctypes.c_void_p)
    ]

class DOUBLELINKEDLIST(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _DOUBLELINKEDLIST

class _L_SUDOKU(ctypes.Structure):
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

class L_SUDOKU(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _L_SUDOKU


class _NUMA(ctypes.Structure):
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

class NUMA(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _NUMA


class _BOXAA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("boxa", ctypes.POINTER(ctypes.POINTER(_BOXA)))
    ]

class BOXAA(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _BOXAA


class _L_STACK(ctypes.Structure):
    """Comments not generated
    """
    pass

_L_STACK._fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_void_p)),
        ("auxstack", ctypes.POINTER(_L_STACK))
    ]

class L_STACK(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _L_STACK

class _L_PTRA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("imax", ctypes.c_int32),
        ("nactual", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_void_p))
    ]

class L_PTRA(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _L_PTRA


class _L_KERNEL(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("sy", ctypes.c_int32),
        ("sx", ctypes.c_int32),
        ("cy", ctypes.c_int32),
        ("cx", ctypes.c_int32),
        ("data", ctypes.POINTER(ctypes.POINTER(ctypes.c_float)))
    ]

class L_KERNEL(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _L_KERNEL


class _BMP_FILEHEADER(ctypes.Structure):
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

class BMP_FILEHEADER(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _BMP_FILEHEADER


class _L_PTRAA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("ptra", ctypes.POINTER(ctypes.POINTER(_L_PTRA)))
    ]

class L_PTRAA(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _L_PTRAA


class _SELA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("sel", ctypes.POINTER(ctypes.POINTER(_SEL)))
    ]

class SELA(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _SELA


class _BMP_INFOHEADER(ctypes.Structure):
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

class BMP_INFOHEADER(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _BMP_INFOHEADER


class _NUMAA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("numa", ctypes.POINTER(ctypes.POINTER(_NUMA)))
    ]

class NUMAA(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _NUMAA


class _L_DEWARP(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pixs", ctypes.POINTER(_PIX)),
        ("pixd", ctypes.POINTER(_PIX)),
        ("sampvdispar", ctypes.POINTER(_FPIX)),
        ("samphdispar", ctypes.POINTER(_FPIX)),
        ("fullvdispar", ctypes.POINTER(_FPIX)),
        ("fullhdispar", ctypes.POINTER(_FPIX)),
        ("naflats", ctypes.POINTER(_NUMA)),
        ("nacurves", ctypes.POINTER(_NUMA)),
        ("pageno", ctypes.c_int32),
        ("sampling", ctypes.c_int32),
        ("minlines", ctypes.c_int32),
        ("applyhoriz", ctypes.c_int32),
        ("nx", ctypes.c_int32),
        ("ny", ctypes.c_int32),
        ("extraw", ctypes.c_int32),
        ("success", ctypes.c_int32)
    ]

class L_DEWARP(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _L_DEWARP


class _PIXCOMP(ctypes.Structure):
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

class PIXCOMP(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _PIXCOMP


class _PTAA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("pta", ctypes.POINTER(ctypes.POINTER(_PTA)))
    ]

class PTAA(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _PTAA


class _GPLOT(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("rootname", ctypes.POINTER(ctypes.c_char)),
        ("cmdname", ctypes.POINTER(ctypes.c_char)),
        ("cmddata", ctypes.POINTER(_SARRAY)),
        ("datanames", ctypes.POINTER(_SARRAY)),
        ("plotdata", ctypes.POINTER(_SARRAY)),
        ("plottitles", ctypes.POINTER(_SARRAY)),
        ("plotstyles", ctypes.POINTER(_NUMA)),
        ("nplots", ctypes.c_int32),
        ("outname", ctypes.POINTER(ctypes.c_char)),
        ("outformat", ctypes.c_int32),
        ("scaling", ctypes.c_int32),
        ("title", ctypes.POINTER(ctypes.c_char)),
        ("xlabel", ctypes.POINTER(ctypes.c_char)),
        ("ylabel", ctypes.POINTER(ctypes.c_char))
    ]

class GPLOT(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _GPLOT


class _NUMA2D(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nrows", ctypes.c_int32),
        ("ncols", ctypes.c_int32),
        ("initsize", ctypes.c_int32),
        ("numa", ctypes.POINTER(ctypes.POINTER(ctypes.POINTER(_NUMA))))
    ]

class NUMA2D(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _NUMA2D


class _NUMAHASH(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nbuckets", ctypes.c_int32),
        ("initsize", ctypes.c_int32),
        ("numa", ctypes.POINTER(ctypes.POINTER(_NUMA)))
    ]

class NUMAHASH(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _NUMAHASH


class _PIXTILING(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pix", ctypes.POINTER(_PIX)),
        ("nx", ctypes.c_int32),
        ("ny", ctypes.c_int32),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("xoverlap", ctypes.c_int32),
        ("yoverlap", ctypes.c_int32),
        ("strip", ctypes.c_int32)
    ]

class PIXTILING(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _PIXTILING


class _PIXA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("refcount", ctypes.c_uint32),
        ("pix", ctypes.POINTER(ctypes.POINTER(_PIX))),
        ("boxa", ctypes.POINTER(_BOXA))
    ]

class PIXA(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _PIXA


class _PIXACC(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("offset", ctypes.c_int32),
        ("pix", ctypes.POINTER(_PIX))
    ]

class PIXACC(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _PIXACC


class _CCBORD(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pix", ctypes.POINTER(_PIX)),
        ("boxa", ctypes.POINTER(_BOXA)),
        ("start", ctypes.POINTER(_PTA)),
        ("refcount", ctypes.c_int32),
        ("local", ctypes.POINTER(_PTAA)),
        ("global", ctypes.POINTER(_PTAA)),
        ("step", ctypes.POINTER(_NUMAA)),
        ("splocal", ctypes.POINTER(_PTA)),
        ("spglobal", ctypes.POINTER(_PTA))
    ]

class CCBORD(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _CCBORD


class _PIXACOMP(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("pixc", ctypes.POINTER(ctypes.POINTER(_PIXCOMP))),
        ("boxa", ctypes.POINTER(_BOXA))
    ]

class PIXACOMP(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _PIXACOMP


class _JBDATA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pix", ctypes.POINTER(_PIX)),
        ("npages", ctypes.c_int32),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("nclass", ctypes.c_int32),
        ("latticew", ctypes.c_int32),
        ("latticeh", ctypes.c_int32),
        ("naclass", ctypes.POINTER(_NUMA)),
        ("napage", ctypes.POINTER(_NUMA)),
        ("ptaul", ctypes.POINTER(_PTA))
    ]

class JBDATA(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _JBDATA


class _L_QUEUE(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("nalloc", ctypes.c_int32),
        ("nhead", ctypes.c_int32),
        ("nelem", ctypes.c_int32),
        ("array", ctypes.POINTER(ctypes.c_void_p)),
        ("stack", ctypes.POINTER(_L_STACK))
    ]

class L_QUEUE(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _L_QUEUE


class _CCBORDA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pix", ctypes.POINTER(_PIX)),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("ccb", ctypes.POINTER(ctypes.POINTER(_CCBORD)))
    ]

class CCBORDA(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _CCBORDA


class _L_BMF(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pixa", ctypes.POINTER(_PIXA)),
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

class L_BMF(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _L_BMF


class _PIXAA(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("n", ctypes.c_int32),
        ("nalloc", ctypes.c_int32),
        ("pixa", ctypes.POINTER(ctypes.POINTER(_PIXA))),
        ("boxa", ctypes.POINTER(_BOXA))
    ]

class PIXAA(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _PIXAA


class _L_WSHED(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("pixs", ctypes.POINTER(_PIX)),
        ("pixm", ctypes.POINTER(_PIX)),
        ("mindepth", ctypes.c_int32),
        ("pixlab", ctypes.POINTER(_PIX)),
        ("pixt", ctypes.POINTER(_PIX)),
        ("lines8", ctypes.POINTER(ctypes.c_void_p)),
        ("linem1", ctypes.POINTER(ctypes.c_void_p)),
        ("linelab32", ctypes.POINTER(ctypes.c_void_p)),
        ("linet1", ctypes.POINTER(ctypes.c_void_p)),
        ("pixad", ctypes.POINTER(_PIXA)),
        ("ptas", ctypes.POINTER(_PTA)),
        ("nasi", ctypes.POINTER(_NUMA)),
        ("nash", ctypes.POINTER(_NUMA)),
        ("namh", ctypes.POINTER(_NUMA)),
        ("nalevels", ctypes.POINTER(_NUMA)),
        ("nseeds", ctypes.c_int32),
        ("nother", ctypes.c_int32),
        ("lut", ctypes.POINTER(ctypes.c_int32)),
        ("links", ctypes.POINTER(ctypes.POINTER(_NUMA))),
        ("arraysize", ctypes.c_int32),
        ("debug", ctypes.c_int32)
    ]

class L_WSHED(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _L_WSHED


class _JBCLASSER(ctypes.Structure):
    """Comments not generated
    """
    _fields_ = [
        ("safiles", ctypes.POINTER(_SARRAY)),
        ("method", ctypes.c_int32),
        ("components", ctypes.c_int32),
        ("maxwidth", ctypes.c_int32),
        ("maxheight", ctypes.c_int32),
        ("npages", ctypes.c_int32),
        ("baseindex", ctypes.c_int32),
        ("nacomps", ctypes.POINTER(_NUMA)),
        ("sizehaus", ctypes.c_int32),
        ("rankhaus", ctypes.c_float),
        ("thresh", ctypes.c_float),
        ("weightfactor", ctypes.c_float),
        ("naarea", ctypes.POINTER(_NUMA)),
        ("w", ctypes.c_int32),
        ("h", ctypes.c_int32),
        ("nclass", ctypes.c_int32),
        ("keep_pixaa", ctypes.c_int32),
        ("pixaa", ctypes.POINTER(_PIXAA)),
        ("pixat", ctypes.POINTER(_PIXA)),
        ("pixatd", ctypes.POINTER(_PIXA)),
        ("nahash", ctypes.POINTER(_NUMAHASH)),
        ("nafgt", ctypes.POINTER(_NUMA)),
        ("ptac", ctypes.POINTER(_PTA)),
        ("ptact", ctypes.POINTER(_PTA)),
        ("naclass", ctypes.POINTER(_NUMA)),
        ("napage", ctypes.POINTER(_NUMA)),
        ("ptaul", ctypes.POINTER(_PTA)),
        ("ptall", ctypes.POINTER(_PTA))
    ]

class JBCLASSER(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _JBCLASSER



BBUFFER = BYTEBUFFER
DLLIST = DOUBLELINKEDLIST
PIXCMAP = DOUBLELINKEDLIST
PIXAC = PIXACOMP
PIXC = PIXCOMP

