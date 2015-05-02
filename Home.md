#Documentation Page

# Python Leptonica #

This is  a wrapepr for the Leptonica image processing Library.

Leptonica contains extensive documentation embeded in its C source files -
this project, even in the initial stages, translate all tha documentation
to Python doc strings. Therefore help on functions and constants can be obtained
by use of Python documentation tools with the module (for examle, teh help function
in interactive mode)

# Usage blurb #

As of version 0.8 there is no easy way to call functions that request
pointers to integers to writeback results - These poitners have to be manually created
using ctypes. Pointers to leptonica strcutures are authomatically created upon function calls when Python objects equivalent to the C structures (and Python objects are created when the leptonica function returns a pointer to a newly - or previously existent -
allocated data structure)

Python numbers and strigns can beused for parameters that require sclars or C nullterminated strings (char **).**

_WARNING: current version will work with leptonica 1.67 only_