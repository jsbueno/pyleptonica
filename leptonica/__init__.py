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

from leptonica_structures import *
from leptonica_functions import *
from leptonica_utils import *
import leptonica_enums as enums

#
# The leptonica_functions_parser.py and leptonica_header_parser
# are used as stand alone programs to generate the
# leptonica_functions.py and leptonica_structures.py
# In case you want to hack around this code
# or need to update to a different version of Leptonica

# the Leptonica.py file just contains a small usage example
