# -*- coding: utf-8 -*-

"""
This file is used as a laboratory to experiment with the 
generated classes that represent leptonica's structures.

Once the concepts tried for a single class are made
to work here, these contents should be updated in the
class and file templates in leptonica/leptonica_header_parser.py

The idea is to have classes that behave as pointer to structures
when passed to C functions, and behave as Python objects
on the Python side, without danger of a null pointer
exception.
"""



import ctypes

def property_factory(field_name):
    return  property(lambda s: getattr(s.contents, field_name),
                     lambda s, val: setattr(s.contents, field_name, val)
                    )

PointerType = type(ctypes.POINTER(ctypes.c_int))

class Meta(PointerType): 
    def __new__(cls, name, bases, dic):
        def __init__(self, *args):
            if not args:
                args = (_DPIX(),)
            return bases[0].__init__(self, *args)
        if not "__init__" in dic:
            dic["__init__"] = __init__
        for field, type_ in dic["_type_"]._fields_:
            if field == "contents":
                raise TypeError("Can't create an hybrid pointer/function with"
                                 "a 'contents' named attribute")
            pr = property_factory(field)
            dic[field] = pr
        return PointerType(name, bases, dic)

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

pointer = ctypes.POINTER(_DPIX)

class DPIX(pointer):
    __metaclass__ = Meta
    _type_ = _DPIX
