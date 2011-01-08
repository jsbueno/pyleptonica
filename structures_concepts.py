# -*- coding: utf-8 -*-

"""
This file is used as a laboratory to experiment with the 
generated classes that represent leptonica's structures.

Once the concepts tried for a single class are made
to work here, these contents should be manually updated in the
class and file templates in leptonica/leptonica_header_parser.py

The idea is to have classes that behave as pointer to structures
when passed to C functions, and behave as Python objects
on the Python side, without danger of a null pointer
exception.
"""



import ctypes
lp = ctypes.cdll.LoadLibrary("liblept.so")

#mechanism to avoid circular importing:
import sys
try:
    lep = sys.modules["leptonica.leptonica_functions"]
except KeyError:
    from leptonica import leptonica_functions as lep


def property_factory(raw_structure, field_name):
    return  property(lambda s: getattr(
                        raw_structure.from_address(s._address_.value),
                        field_name),
                     lambda s, val: setattr(
                        raw_structure.from_address(s._address_.value),
                        field_name, val)
                    )
class LeptonObject(object):
    def __new__(cls, *args):
        data = None
        if len(args) != 1:
            from leptonica_functions import functions
            if hasattr(functions, cls.__name__.lower() + "Create"):
                constructor = getattr(functions, cls.__name__.lower() + "Create")
                return constructor(*args)
            data = cls._type_(*args)
            address = ctypes.addressof(data)
        else:
            address = args[0]
            if isinstance (address, ctypes.c_void_p):
                address = address.value
        if address in cls._instances_:
            return cls._instances_[address]()
        self = object.__new__(cls)
        self._address_ = ctypes.c_void_p(address)
        cls._instances_[address] = weakref.ref(self)
        if data:
            self._data_ = data
        return self

class MetaPointer(type): 
    def __new__(cls, name, bases, dic):
        base_struct = dic["_type_"]
        for field, type_ in base_struct._fields_:
            pr = property_factory(base_struct, field)
            dic[field] = pr
        return type(name, bases, dic)


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
        ("colormap", ctypes.c_void_p), #ctypes.POINTER(_PIXCOLORMAP)),
        ("data", ctypes.POINTER(ctypes.c_uint32))
    ]


class PIX(LeptonObject):
    __metaclass__ = MetaPointer
    _type_ = _PIX
        
    def __init__(self, *args):
        self._address_ = ctypes.c_void_p(lp.pixCreate(*args))
        #self._address_ = lep.functions.pixCreate(*args)
    def destroy(self):
        lp.pixDestroy(ctypes.c_void_p(ctypes.addressof(self._address_ )))

