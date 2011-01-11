
# coding: utf-8
# Author: João S. O. Bueno
# This is a generated file - do not edit!


class Const(int):
    "Parent class to all constants"
    def __new__(cls, name, value, doc=""):
        self = int.__new__(cls, value)
        self.name = name
        self.doc = doc
        self.value = value 
        return self
    def __repr__(self):
        return self.name
    def __str__(self):
        return "%s = %s%s" % (self.name,self.value, ("  # " + self.doc) if self.doc else "")

def find_siblings(const, as_string=False):
    '''Helper function to locate blocks of related constants:
       i.e. the constants that used to live in the same "enum" in leptonica's C source files
    '''
    cls = const.__class__
    all_consts = [this_const for this_const in globals().values() if this_const.__class__ == cls]
    all_consts.sort()
    if not as_string:
        return all_consts
    return "\n".join(str(const) for const in all_consts)
    


class ConstType(Const):
    '''
       ------------------------------------------------------------------------* 
                              Array flags                               *
------------------------------------------------------------------------*/

 Flags for interpolation in Numa */
enum {
    L_LINEAR_INTERP = 1,        /* linear     */
    L_QUADRATIC_INTERP = 2      /* quadratic  */
}
    '''

ConstType.__name__ = "array_flags"

L_LINEAR_INTERP = ConstType("L_LINEAR_INTERP", 1, '''linear ''')
L_QUADRATIC_INTERP = ConstType("L_QUADRATIC_INTERP", 2, '''quadratic ''')


del ConstType



class ConstType(Const):
    '''
        Flags for added borders in Numa */
enum {
    L_EXTENDED_BORDER = 1,      /* extended with same value           */
    L_MIRRORED_BORDER = 2       /* mirrored                           */
}
    '''

ConstType.__name__ = "flags_for_added_borders_in_numa"

L_EXTENDED_BORDER = ConstType("L_EXTENDED_BORDER", 1, '''extended with same value ''')
L_MIRRORED_BORDER = ConstType("L_MIRRORED_BORDER", 2, '''mirrored ''')


del ConstType



class ConstType(Const):
    '''
        
  bmf.h
     Simple data structure to hold bitmap fonts and related data
/

 Constants for deciding when text block is divided into paragraphs */
enum {
    SPLIT_ON_LEADING_WHITE = 1,    /* tab or space at beginning of line   */
    SPLIT_ON_BLANK_LINE    = 2,    /* newline with optional white space   */
    SPLIT_ON_BOTH          = 3     /* leading white space or newline      */
}
    '''

ConstType.__name__ = "bmf.h"

SPLIT_ON_LEADING_WHITE = ConstType("SPLIT_ON_LEADING_WHITE", 1, '''tab or space at beginning of line ''')
SPLIT_ON_BLANK_LINE = ConstType("SPLIT_ON_BLANK_LINE", 2, '''newline with optional white space ''')
SPLIT_ON_BOTH = ConstType("SPLIT_ON_BOTH", 3, '''leading white space or newline ''')


del ConstType



class ConstType(Const):
    '''
         ccbord.h
           CCBord:   represents a single connected component
           CCBorda:  an array of CCBord
/

 Use in ccbaStepChainsToPixCoords() */
enum {
      CCB_LOCAL_COORDS = 1,
      CCB_GLOBAL_COORDS = 2
}
    '''

ConstType.__name__ = "ccbord.h"

CCB_LOCAL_COORDS = ConstType("CCB_LOCAL_COORDS", 1, ''' ''')
CCB_GLOBAL_COORDS = ConstType("CCB_GLOBAL_COORDS", 2, ''' ''')


del ConstType



class ConstType(Const):
    '''
        Use in ccbaGenerateSPGlobalLocs() */
enum {
      CCB_SAVE_ALL_PTS = 1,
      CCB_SAVE_TURNING_PTS = 2
}
    '''

ConstType.__name__ = "use_in_ccbageneratespgloballocs()"

CCB_SAVE_ALL_PTS = ConstType("CCB_SAVE_ALL_PTS", 1, ''' ''')
CCB_SAVE_TURNING_PTS = ConstType("CCB_SAVE_TURNING_PTS", 2, ''' ''')


del ConstType



class ConstType(Const):
    '''
         To control conditional compilation, one of two variables
       L_LITTLE_ENDIAN  (e.g., for Intel X86)
       L_BIG_ENDIAN     (e.g., for Sun SPARC, Mac Power PC)
  is defined when the GCC compiler is invoked.
  All code should compile properly for both hardware architectures.
/

------------------------------------------------------------------------*
                   Simple search state variables                        *
------------------------------------------------------------------------*/
enum {
    L_NOT_FOUND = 0,
    L_FOUND = 1
}
    '''

ConstType.__name__ = "to_control_conditional_compilation,_one_of_two_variables"

L_NOT_FOUND = ConstType("L_NOT_FOUND", 0, ''' ''')
L_FOUND = ConstType("L_FOUND", 1, ''' ''')


del ConstType



class ConstType(Const):
    '''
       enum GPLOT_STYLE {
    GPLOT_LINES       = 0,
    GPLOT_POINTS      = 1,
    GPLOT_IMPULSES    = 2,
    GPLOT_LINESPOINTS = 3,
    GPLOT_DOTS        = 4
}
    '''

ConstType.__name__ = "generated_constants"

GPLOT_LINES = ConstType("GPLOT_LINES", 0, ''' ''')
GPLOT_POINTS = ConstType("GPLOT_POINTS", 1, ''' ''')
GPLOT_IMPULSES = ConstType("GPLOT_IMPULSES", 2, ''' ''')
GPLOT_LINESPOINTS = ConstType("GPLOT_LINESPOINTS", 3, ''' ''')
GPLOT_DOTS = ConstType("GPLOT_DOTS", 4, ''' ''')


del ConstType



class ConstType(Const):
    '''
       enum GPLOT_OUTPUT {
    GPLOT_NONE  = 0,
    GPLOT_PNG   = 1,
    GPLOT_PS    = 2,
    GPLOT_EPS   = 3,
    GPLOT_X11   = 4,
    GPLOT_LATEX = 5
}
    '''

ConstType.__name__ = "generated_constants"

GPLOT_NONE = ConstType("GPLOT_NONE", 0, ''' ''')
GPLOT_PNG = ConstType("GPLOT_PNG", 1, ''' ''')
GPLOT_PS = ConstType("GPLOT_PS", 2, ''' ''')
GPLOT_EPS = ConstType("GPLOT_EPS", 3, ''' ''')
GPLOT_X11 = ConstType("GPLOT_X11", 4, ''' ''')
GPLOT_LATEX = ConstType("GPLOT_LATEX", 5, ''' ''')


del ConstType



class ConstType(Const):
    '''
       enum GPLOT_SCALING {
    GPLOT_LINEAR_SCALE  = 0,   /* default */
    GPLOT_LOG_SCALE_X   = 1,
    GPLOT_LOG_SCALE_Y   = 2,
    GPLOT_LOG_SCALE_X_Y = 3
}
    '''

ConstType.__name__ = "generated_constants"

GPLOT_LINEAR_SCALE = ConstType("GPLOT_LINEAR_SCALE", 0, '''default ''')
GPLOT_LOG_SCALE_X = ConstType("GPLOT_LOG_SCALE_X", 1, ''' ''')
GPLOT_LOG_SCALE_Y = ConstType("GPLOT_LOG_SCALE_Y", 2, ''' ''')
GPLOT_LOG_SCALE_X_Y = ConstType("GPLOT_LOG_SCALE_X_Y", 3, ''' ''')


del ConstType



class ConstType(Const):
    '''
        ------------------ Image file format types -------------- */

  
  The IFF_DEFAULT flag is used to write the file out in the
  same (input) file format that the pix was read from.  If the pix
  was not read from file, the input format field will be
  IFF_UNKNOWN and the output file format will be chosen to
  be compressed and lossless; namely, IFF_TIFF_G4 for d = 1
  and IFF_PNG for everything else.   IFF_JP2 is for jpeg2000, which
  is not supported in leptonica.
  In the future, new format types that have defined extensions
  will be added before IFF_DEFAULT, and will be kept in sync with
  the file format extensions in writefile.c.  The positions of
  file formats before IFF_DEFAULT will remain invariant.
/
enum {
    IFF_UNKNOWN        = 0,
    IFF_BMP            = 1,
    IFF_JFIF_JPEG      = 2,
    IFF_PNG            = 3,
    IFF_TIFF           = 4,
    IFF_TIFF_PACKBITS  = 5,
    IFF_TIFF_RLE       = 6,
    IFF_TIFF_G3        = 7,
    IFF_TIFF_G4        = 8,
    IFF_TIFF_LZW       = 9,
    IFF_TIFF_ZIP       = 10,
    IFF_PNM            = 11,
    IFF_PS             = 12,
    IFF_GIF            = 13,
    IFF_JP2            = 14,
    IFF_WEBP           = 15,
    IFF_DEFAULT        = 16,
    IFF_SPIX           = 17
}
    '''

ConstType.__name__ = "image_file_format_types"

IFF_UNKNOWN = ConstType("IFF_UNKNOWN", 0, ''' ''')
IFF_BMP = ConstType("IFF_BMP", 1, ''' ''')
IFF_JFIF_JPEG = ConstType("IFF_JFIF_JPEG", 2, ''' ''')
IFF_PNG = ConstType("IFF_PNG", 3, ''' ''')
IFF_TIFF = ConstType("IFF_TIFF", 4, ''' ''')
IFF_TIFF_PACKBITS = ConstType("IFF_TIFF_PACKBITS", 5, ''' ''')
IFF_TIFF_RLE = ConstType("IFF_TIFF_RLE", 6, ''' ''')
IFF_TIFF_G3 = ConstType("IFF_TIFF_G3", 7, ''' ''')
IFF_TIFF_G4 = ConstType("IFF_TIFF_G4", 8, ''' ''')
IFF_TIFF_LZW = ConstType("IFF_TIFF_LZW", 9, ''' ''')
IFF_TIFF_ZIP = ConstType("IFF_TIFF_ZIP", 10, ''' ''')
IFF_PNM = ConstType("IFF_PNM", 11, ''' ''')
IFF_PS = ConstType("IFF_PS", 12, ''' ''')
IFF_GIF = ConstType("IFF_GIF", 13, ''' ''')
IFF_JP2 = ConstType("IFF_JP2", 14, ''' ''')
IFF_WEBP = ConstType("IFF_WEBP", 15, ''' ''')
IFF_DEFAULT = ConstType("IFF_DEFAULT", 16, ''' ''')
IFF_SPIX = ConstType("IFF_SPIX", 17, ''' ''')


del ConstType



class ConstType(Const):
    '''
        ------------------ Format header ids --------------- */
enum {
    BMP_ID             = 0x4d42,
    TIFF_BIGEND_ID     = 0x4d4d,     /* MM - for 'motorola' */
    TIFF_LITTLEEND_ID  = 0x4949      /* II - for 'intel'    */
}
    '''

ConstType.__name__ = "format_header_ids"

BMP_ID = ConstType("BMP_ID", 19778, ''' ''')
TIFF_BIGEND_ID = ConstType("TIFF_BIGEND_ID", 19789, '''MM - for 'motorola' ''')
TIFF_LITTLEEND_ID = ConstType("TIFF_LITTLEEND_ID", 18761, '''II - for 'intel' ''')


del ConstType



class ConstType(Const):
    '''
        ------------------ Gray hinting in jpeg reader --------------- */
enum {
    L_HINT_GRAY = 1,  /* only want grayscale information */
}
    '''

ConstType.__name__ = "gray_hinting_in_jpeg_reader"

L_HINT_GRAY = ConstType("L_HINT_GRAY", 1, '''only want grayscale information ''')


del ConstType



class ConstType(Const):
    '''
        Classifier methods */
enum {
   JB_RANKHAUS = 0,
   JB_CORRELATION = 1
}
    '''

ConstType.__name__ = "classifier_methods"

JB_RANKHAUS = ConstType("JB_RANKHAUS", 0, ''' ''')
JB_CORRELATION = ConstType("JB_CORRELATION", 1, ''' ''')


del ConstType



class ConstType(Const):
    '''
        For jbGetComponents(): type of component to extract from images */
enum {
   JB_CONN_COMPS = 0,
   JB_CHARACTERS = 1,
   JB_WORDS = 2
}
    '''

ConstType.__name__ = "for_jbgetcomponents():_type_of_component_to_extract_from_images"

JB_CONN_COMPS = ConstType("JB_CONN_COMPS", 0, ''' ''')
JB_CHARACTERS = ConstType("JB_CHARACTERS", 1, ''' ''')
JB_WORDS = ConstType("JB_WORDS", 2, ''' ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                 Morphological boundary condition flags                  *
  Two types of boundary condition for erosion.
  The global variable MORPH_BC takes on one of these two values.
  See notes in morph.c for usage.
-------------------------------------------------------------------------*/
enum {
    SYMMETRIC_MORPH_BC = 0,
    ASYMMETRIC_MORPH_BC = 1
}
    '''

ConstType.__name__ = "morphological_boundary_condition_flags"

SYMMETRIC_MORPH_BC = ConstType("SYMMETRIC_MORPH_BC", 0, ''' ''')
ASYMMETRIC_MORPH_BC = ConstType("ASYMMETRIC_MORPH_BC", 1, ''' ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                        Structuring element types                        *
-------------------------------------------------------------------------*/
enum {
    SEL_DONT_CARE  = 0,
    SEL_HIT        = 1,
    SEL_MISS       = 2
}
    '''

ConstType.__name__ = "structuring_element_types"

SEL_DONT_CARE = ConstType("SEL_DONT_CARE", 0, ''' ''')
SEL_HIT = ConstType("SEL_HIT", 1, ''' ''')
SEL_MISS = ConstType("SEL_MISS", 2, ''' ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                  Runlength flags for granulometry                       *
-------------------------------------------------------------------------*/
enum {
    L_RUN_OFF = 0,
    L_RUN_ON  = 1
}
    '''

ConstType.__name__ = "runlength_flags_for_granulometry"

L_RUN_OFF = ConstType("L_RUN_OFF", 0, ''' ''')
L_RUN_ON = ConstType("L_RUN_ON", 1, ''' ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
         Direction flags for grayscale morphology, granulometry,         *
                   composable Sels, and convolution                      *
-------------------------------------------------------------------------*/
enum {
    L_HORIZ            = 1,
    L_VERT             = 2,
    L_BOTH_DIRECTIONS  = 3
}
    '''

ConstType.__name__ = "direction_flags_for_grayscale_morphology,_granulometry,"

L_HORIZ = ConstType("L_HORIZ", 1, ''' ''')
L_VERT = ConstType("L_VERT", 2, ''' ''')
L_BOTH_DIRECTIONS = ConstType("L_BOTH_DIRECTIONS", 3, ''' ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                   Morphological operation flags                         *
-------------------------------------------------------------------------*/
enum {
    L_MORPH_DILATE    = 1,
    L_MORPH_ERODE     = 2,
    L_MORPH_OPEN      = 3,
    L_MORPH_CLOSE     = 4,
    L_MORPH_HMT       = 5
}
    '''

ConstType.__name__ = "morphological_operation_flags"

L_MORPH_DILATE = ConstType("L_MORPH_DILATE", 1, ''' ''')
L_MORPH_ERODE = ConstType("L_MORPH_ERODE", 2, ''' ''')
L_MORPH_OPEN = ConstType("L_MORPH_OPEN", 3, ''' ''')
L_MORPH_CLOSE = ConstType("L_MORPH_CLOSE", 4, ''' ''')
L_MORPH_HMT = ConstType("L_MORPH_HMT", 5, ''' ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                    Grayscale intensity scaling flags                    *
-------------------------------------------------------------------------*/
enum {
    L_LINEAR_SCALE  = 1,
    L_LOG_SCALE     = 2
}
    '''

ConstType.__name__ = "grayscale_intensity_scaling_flags"

L_LINEAR_SCALE = ConstType("L_LINEAR_SCALE", 1, ''' ''')
L_LOG_SCALE = ConstType("L_LOG_SCALE", 2, ''' ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                      Morphological tophat flags                         *
-------------------------------------------------------------------------*/
enum {
    L_TOPHAT_WHITE = 0,
    L_TOPHAT_BLACK = 1
}
    '''

ConstType.__name__ = "morphological_tophat_flags"

L_TOPHAT_WHITE = ConstType("L_TOPHAT_WHITE", 0, ''' ''')
L_TOPHAT_BLACK = ConstType("L_TOPHAT_BLACK", 1, ''' ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                Arithmetic and logical operator flags                    *
                 (use on grayscale images and Numas)                     *
-------------------------------------------------------------------------*/
enum {
    L_ARITH_ADD       = 1,
    L_ARITH_SUBTRACT  = 2,
    L_ARITH_MULTIPLY  = 3,   /* on numas only */
    L_ARITH_DIVIDE    = 4,   /* on numas only */
    L_UNION           = 5,   /* on numas only */
    L_INTERSECTION    = 6,   /* on numas only */
    L_SUBTRACTION     = 7,   /* on numas only */
    L_EXCLUSIVE_OR    = 8    /* on numas only */
}
    '''

ConstType.__name__ = "arithmetic_and_logical_operator_flags"

L_ARITH_ADD = ConstType("L_ARITH_ADD", 1, ''' ''')
L_ARITH_SUBTRACT = ConstType("L_ARITH_SUBTRACT", 2, ''' ''')
L_ARITH_MULTIPLY = ConstType("L_ARITH_MULTIPLY", 3, '''on numas only ''')
L_ARITH_DIVIDE = ConstType("L_ARITH_DIVIDE", 4, '''on numas only ''')
L_UNION = ConstType("L_UNION", 5, '''on numas only ''')
L_INTERSECTION = ConstType("L_INTERSECTION", 6, '''on numas only ''')
L_SUBTRACTION = ConstType("L_SUBTRACTION", 7, '''on numas only ''')
L_EXCLUSIVE_OR = ConstType("L_EXCLUSIVE_OR", 8, '''on numas only ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                        Min/max selection flags                          *
-------------------------------------------------------------------------*/
enum {
    L_CHOOSE_MIN = 1,           /* useful in a downscaling "erosion"  */
    L_CHOOSE_MAX = 2,           /* useful in a downscaling "dilation" */
    L_CHOOSE_MAX_MIN_DIFF = 3   /* useful in a downscaling contrast   */
}
    '''

ConstType.__name__ = "min/max_selection_flags"

L_CHOOSE_MIN = ConstType("L_CHOOSE_MIN", 1, '''useful in a downscaling "erosion" ''')
L_CHOOSE_MAX = ConstType("L_CHOOSE_MAX", 2, '''useful in a downscaling "dilation" ''')
L_CHOOSE_MAX_MIN_DIFF = ConstType("L_CHOOSE_MAX_MIN_DIFF", 3, '''useful in a downscaling contrast ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                    Distance function b.c. flags                         *
-------------------------------------------------------------------------*/
enum {
    L_BOUNDARY_BG = 1,  /* assume bg outside image */
    L_BOUNDARY_FG = 2   /* assume fg outside image */
}
    '''

ConstType.__name__ = "distance_function_b.c._flags"

L_BOUNDARY_BG = ConstType("L_BOUNDARY_BG", 1, '''assume bg outside image ''')
L_BOUNDARY_FG = ConstType("L_BOUNDARY_FG", 2, '''assume fg outside image ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                         Image comparison flags                          *
-------------------------------------------------------------------------*/
enum {
    L_COMPARE_XOR = 1,
    L_COMPARE_SUBTRACT = 2,
    L_COMPARE_ABS_DIFF = 3
}
    '''

ConstType.__name__ = "image_comparison_flags"

L_COMPARE_XOR = ConstType("L_COMPARE_XOR", 1, ''' ''')
L_COMPARE_SUBTRACT = ConstType("L_COMPARE_SUBTRACT", 2, ''' ''')
L_COMPARE_ABS_DIFF = ConstType("L_COMPARE_ABS_DIFF", 3, ''' ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                          Color content flags                            *
-------------------------------------------------------------------------*/
enum {
    L_MAX_DIFF_FROM_AVERAGE_2 = 1,
    L_MAX_MIN_DIFF_FROM_2 = 2,
    L_MAX_DIFF = 3
}
    '''

ConstType.__name__ = "color_content_flags"

L_MAX_DIFF_FROM_AVERAGE_2 = ConstType("L_MAX_DIFF_FROM_AVERAGE_2", 1, ''' ''')
L_MAX_MIN_DIFF_FROM_2 = ConstType("L_MAX_MIN_DIFF_FROM_2", 2, ''' ''')
L_MAX_DIFF = ConstType("L_MAX_DIFF", 3, ''' ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                             Colors for 32 bpp                           *
-------------------------------------------------------------------------*/

  Notes:
      (1) These are the byte indices for colors in 32 bpp images.
          They are used through the GET/SET_DATA_BYTE accessors.
          The 4th byte, typically known as the "alpha channel" and used
          for blending, is not explicitly used in leptonica.
      (2) If you redefine these values, functions that have the shifts
          hardcoded (instead of using the constants below) will break.
          These functions are labelled with "***" next to their names
          at the top of the files in which they are defined.
          Advice: Do not change these values!
      (3) The shifts to extract the red, green and blue components
          from a 32 bit pixel are defined in terms of these colors.
/
enum {
    COLOR_RED = 0,
    COLOR_GREEN = 1,
    COLOR_BLUE = 2,
    L_ALPHA_CHANNEL = 3
}
    '''

ConstType.__name__ = "colors_for_32_bpp"

COLOR_RED = ConstType("COLOR_RED", 0, ''' ''')
COLOR_GREEN = ConstType("COLOR_GREEN", 1, ''' ''')
COLOR_BLUE = ConstType("COLOR_BLUE", 2, ''' ''')
L_ALPHA_CHANNEL = ConstType("L_ALPHA_CHANNEL", 3, ''' ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                        Flags for colormap conversion                    *
-------------------------------------------------------------------------*/
enum {
    REMOVE_CMAP_TO_BINARY = 0,
    REMOVE_CMAP_TO_GRAYSCALE = 1,
    REMOVE_CMAP_TO_FULL_COLOR = 2,
    REMOVE_CMAP_BASED_ON_SRC = 3
}
    '''

ConstType.__name__ = "flags_for_colormap_conversion"

REMOVE_CMAP_TO_BINARY = ConstType("REMOVE_CMAP_TO_BINARY", 0, ''' ''')
REMOVE_CMAP_TO_GRAYSCALE = ConstType("REMOVE_CMAP_TO_GRAYSCALE", 1, ''' ''')
REMOVE_CMAP_TO_FULL_COLOR = ConstType("REMOVE_CMAP_TO_FULL_COLOR", 2, ''' ''')
REMOVE_CMAP_BASED_ON_SRC = ConstType("REMOVE_CMAP_BASED_ON_SRC", 3, ''' ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                         Access and storage flags                        *
-------------------------------------------------------------------------*/

  For Pix, Box, Pta and Numa, there are 3 standard methods for handling
  the retrieval or insertion of a struct:
     (1) direct insertion (Don't do this if there is another handle
                           somewhere to this same struct!)
     (2) copy (Always safe, sets up a refcount of 1 on the new object.
               Can be undesirable if very large, such as an image or
               an array of images.)
     (3) clone (Makes another handle to the same struct, and bumps the
                refcount up by 1.  Safe to do unless you're changing
                data through one of the handles but don't want those
                changes to be seen by the other handle.)
  For Pixa and Boxa, which are structs that hold an array of clonable
  structs, there is an additional method:
     (4) copy-clone (Makes a new higher-level struct with a refcount
                     of 1, but clones all the structs in the array.)
  Unlike the other structs, when retrieving a string from an Sarray,
  you are allowed to get a handle without a copy or clone (i.e., that
  you don't own!).  You must not free or insert such a string!
  Specifically, for an Sarray, the copyflag for retrieval is either:
         TRUE (or 1 or L_COPY)
  or
         FALSE (or 0 or L_NOCOPY)
  For insertion, the copyflag is either:
         TRUE (or 1 or L_COPY)
  or
         FALSE (or 0 or L_INSERT)
  Note that L_COPY is always 1, and L_INSERT and L_NOCOPY are always 0.
/
enum {
    L_INSERT = 0,     /* stuff it in; no copy, clone or copy-clone    */
    L_COPY = 1,       /* make/use a copy of the object                */
    L_CLONE = 2,      /* make/use clone (ref count) of the object     */
    L_COPY_CLONE = 3  /* make a new object and fill with with clones  */
                      /* of each object in the array(s)               */
}
    '''

ConstType.__name__ = "access_and_storage_flags"

L_INSERT = ConstType("L_INSERT", 0, '''stuff it in; no copy, clone or copy-clone ''')
L_COPY = ConstType("L_COPY", 1, '''make/use a copy of the object ''')
L_CLONE = ConstType("L_CLONE", 2, '''make/use clone (ref count) of the object ''')
L_COPY_CLONE = ConstType("L_COPY_CLONE", 3, '''make a new object and fill with with clones ''')


del ConstType



class ConstType(Const):
    '''
        copyflag value in sarrayGetString() */

--------------------------------------------------------------------------*
                              Sort flags                                  *
--------------------------------------------------------------------------*/
enum {
    L_SORT_INCREASING = 1,        /* sort in increasing order               */
    L_SORT_DECREASING = 2         /* sort in decreasing order               */
}
    '''

ConstType.__name__ = "copyflag_value_in_sarraygetstring()"

L_SORT_INCREASING = ConstType("L_SORT_INCREASING", 1, '''sort in increasing order ''')
L_SORT_DECREASING = ConstType("L_SORT_DECREASING", 2, '''sort in decreasing order ''')


del ConstType



class ConstType(Const):
    '''
       enum {
    L_SORT_BY_X = 3,              /* sort box or c.c. by horiz location     */
    L_SORT_BY_Y = 4,              /* sort box or c.c. by vert location      */
    L_SORT_BY_WIDTH = 5,          /* sort box or c.c. by width              */
    L_SORT_BY_HEIGHT = 6,         /* sort box or c.c. by height             */
    L_SORT_BY_MIN_DIMENSION = 7,  /* sort box or c.c. by min dimension      */
    L_SORT_BY_MAX_DIMENSION = 8,  /* sort box or c.c. by max dimension      */
    L_SORT_BY_PERIMETER = 9,      /* sort box or c.c. by perimeter          */
    L_SORT_BY_AREA = 10,          /* sort box or c.c. by area               */
    L_SORT_BY_ASPECT_RATIO = 11   /* sort box or c.c. by width/height ratio */
}
    '''

ConstType.__name__ = "generated_constants"

L_SORT_BY_X = ConstType("L_SORT_BY_X", 3, '''sort box or c.c. by horiz location ''')
L_SORT_BY_Y = ConstType("L_SORT_BY_Y", 4, '''sort box or c.c. by vert location ''')
L_SORT_BY_WIDTH = ConstType("L_SORT_BY_WIDTH", 5, '''sort box or c.c. by width ''')
L_SORT_BY_HEIGHT = ConstType("L_SORT_BY_HEIGHT", 6, '''sort box or c.c. by height ''')
L_SORT_BY_MIN_DIMENSION = ConstType("L_SORT_BY_MIN_DIMENSION", 7, '''sort box or c.c. by min dimension ''')
L_SORT_BY_MAX_DIMENSION = ConstType("L_SORT_BY_MAX_DIMENSION", 8, '''sort box or c.c. by max dimension ''')
L_SORT_BY_PERIMETER = ConstType("L_SORT_BY_PERIMETER", 9, '''sort box or c.c. by perimeter ''')
L_SORT_BY_AREA = ConstType("L_SORT_BY_AREA", 10, '''sort box or c.c. by area ''')
L_SORT_BY_ASPECT_RATIO = ConstType("L_SORT_BY_ASPECT_RATIO", 11, '''sort box or c.c. by width/height ratio ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                             Blend flags                                 *
-------------------------------------------------------------------------*/
enum {
    L_BLEND_WITH_INVERSE = 1,     /* add some of src inverse to itself     */
    L_BLEND_TO_WHITE = 2,         /* shift src colors towards white        */
    L_BLEND_TO_BLACK = 3,         /* shift src colors towards black        */
    L_BLEND_GRAY = 4,             /* blend src directly with blender       */
    L_BLEND_GRAY_WITH_INVERSE = 5 /* add amount of src inverse to itself,  */
                                  /* based on blender pix value            */
}
    '''

ConstType.__name__ = "blend_flags"

L_BLEND_WITH_INVERSE = ConstType("L_BLEND_WITH_INVERSE", 1, '''add some of src inverse to itself ''')
L_BLEND_TO_WHITE = ConstType("L_BLEND_TO_WHITE", 2, '''shift src colors towards white ''')
L_BLEND_TO_BLACK = ConstType("L_BLEND_TO_BLACK", 3, '''shift src colors towards black ''')
L_BLEND_GRAY = ConstType("L_BLEND_GRAY", 4, '''blend src directly with blender ''')
L_BLEND_GRAY_WITH_INVERSE = ConstType("L_BLEND_GRAY_WITH_INVERSE", 5, '''add amount of src inverse to itself, ''')


del ConstType



class ConstType(Const):
    '''
       enum {
    L_PAINT_LIGHT = 1,            /* colorize non-black pixels             */
    L_PAINT_DARK = 2              /* colorize non-white pixels             */
}
    '''

ConstType.__name__ = "generated_constants"

L_PAINT_LIGHT = ConstType("L_PAINT_LIGHT", 1, '''colorize non-black pixels ''')
L_PAINT_DARK = ConstType("L_PAINT_DARK", 2, '''colorize non-white pixels ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                        Graphics pixel setting                           *
-------------------------------------------------------------------------*/
enum {
    L_SET_PIXELS = 1,             /* set all bits in each pixel to 1       */
    L_CLEAR_PIXELS = 2,           /* set all bits in each pixel to 0       */
    L_FLIP_PIXELS = 3             /* flip all bits in each pixel           */
}
    '''

ConstType.__name__ = "graphics_pixel_setting"

L_SET_PIXELS = ConstType("L_SET_PIXELS", 1, '''set all bits in each pixel to 1 ''')
L_CLEAR_PIXELS = ConstType("L_CLEAR_PIXELS", 2, '''set all bits in each pixel to 0 ''')
L_FLIP_PIXELS = ConstType("L_FLIP_PIXELS", 3, '''flip all bits in each pixel ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                           Size filter flags                             *
-------------------------------------------------------------------------*/
enum {
    L_SELECT_WIDTH = 1,           /* width must satisfy constraint         */
    L_SELECT_HEIGHT = 2,          /* height must satisfy constraint        */
    L_SELECT_IF_EITHER = 3,       /* either width or height can satisfy    */
    L_SELECT_IF_BOTH = 4          /* both width and height must satisfy    */
}
    '''

ConstType.__name__ = "size_filter_flags"

L_SELECT_WIDTH = ConstType("L_SELECT_WIDTH", 1, '''width must satisfy constraint ''')
L_SELECT_HEIGHT = ConstType("L_SELECT_HEIGHT", 2, '''height must satisfy constraint ''')
L_SELECT_IF_EITHER = ConstType("L_SELECT_IF_EITHER", 3, '''either width or height can satisfy ''')
L_SELECT_IF_BOTH = ConstType("L_SELECT_IF_BOTH", 4, '''both width and height must satisfy ''')


del ConstType



class ConstType(Const):
    '''
       enum {
    L_SELECT_IF_LT = 1,           /* save if value is less than threshold  */
    L_SELECT_IF_GT = 2,           /* save if value is more than threshold  */
    L_SELECT_IF_LTE = 3,          /* save if value is <= to the threshold  */
    L_SELECT_IF_GTE = 4           /* save if value is >= to the threshold  */
}
    '''

ConstType.__name__ = "generated_constants"

L_SELECT_IF_LT = ConstType("L_SELECT_IF_LT", 1, '''save if value is less than threshold ''')
L_SELECT_IF_GT = ConstType("L_SELECT_IF_GT", 2, '''save if value is more than threshold ''')
L_SELECT_IF_LTE = ConstType("L_SELECT_IF_LTE", 3, '''save if value is <= to the threshold ''')
L_SELECT_IF_GTE = ConstType("L_SELECT_IF_GTE", 4, '''save if value is >= to the threshold ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                     Color component selection flags                     *
-------------------------------------------------------------------------*/
enum {
    L_SELECT_RED = 1,             /* use red component                     */
    L_SELECT_GREEN = 2,           /* use green component                   */
    L_SELECT_BLUE = 3,            /* use blue component                    */
    L_SELECT_MIN = 4,             /* use min color component               */
    L_SELECT_MAX = 5              /* use max color component               */
}
    '''

ConstType.__name__ = "color_component_selection_flags"

L_SELECT_RED = ConstType("L_SELECT_RED", 1, '''use red component ''')
L_SELECT_GREEN = ConstType("L_SELECT_GREEN", 2, '''use green component ''')
L_SELECT_BLUE = ConstType("L_SELECT_BLUE", 3, '''use blue component ''')
L_SELECT_MIN = ConstType("L_SELECT_MIN", 4, '''use min color component ''')
L_SELECT_MAX = ConstType("L_SELECT_MAX", 5, '''use max color component ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                        Rotate and shear flags                           *
-------------------------------------------------------------------------*/
enum {
    L_ROTATE_AREA_MAP = 1,       /* use area map rotation, if possible     */
    L_ROTATE_SHEAR = 2,          /* use shear rotation                     */
    L_ROTATE_SAMPLING = 3        /* use sampling                           */
}
    '''

ConstType.__name__ = "rotate_and_shear_flags"

L_ROTATE_AREA_MAP = ConstType("L_ROTATE_AREA_MAP", 1, '''use area map rotation, if possible ''')
L_ROTATE_SHEAR = ConstType("L_ROTATE_SHEAR", 2, '''use shear rotation ''')
L_ROTATE_SAMPLING = ConstType("L_ROTATE_SAMPLING", 3, '''use sampling ''')


del ConstType



class ConstType(Const):
    '''
       enum {
    L_BRING_IN_WHITE = 1,        /* bring in white pixels from the outside */
    L_BRING_IN_BLACK = 2         /* bring in black pixels from the outside */
}
    '''

ConstType.__name__ = "generated_constants"

L_BRING_IN_WHITE = ConstType("L_BRING_IN_WHITE", 1, '''bring in white pixels from the outside ''')
L_BRING_IN_BLACK = ConstType("L_BRING_IN_BLACK", 2, '''bring in black pixels from the outside ''')


del ConstType



class ConstType(Const):
    '''
       enum {
    L_SHEAR_ABOUT_CORNER = 1,    /* shear image about UL corner            */
    L_SHEAR_ABOUT_CENTER = 2     /* shear image about center               */
}
    '''

ConstType.__name__ = "generated_constants"

L_SHEAR_ABOUT_CORNER = ConstType("L_SHEAR_ABOUT_CORNER", 1, '''shear image about UL corner ''')
L_SHEAR_ABOUT_CENTER = ConstType("L_SHEAR_ABOUT_CENTER", 2, '''shear image about center ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                     Affine transform order flags                        *
-------------------------------------------------------------------------*/
enum {
    L_TR_SC_RO = 1,              /* translate, scale, rotate               */
    L_SC_RO_TR = 2,              /* scale, rotate, translate               */
    L_RO_TR_SC = 3,              /* rotate, translate, scale               */
    L_TR_RO_SC = 4,              /* translate, rotate, scale               */
    L_RO_SC_TR = 5,              /* rotate, scale, translate               */
    L_SC_TR_RO = 6               /* scale, translate, rotate               */
}
    '''

ConstType.__name__ = "affine_transform_order_flags"

L_TR_SC_RO = ConstType("L_TR_SC_RO", 1, '''translate, scale, rotate ''')
L_SC_RO_TR = ConstType("L_SC_RO_TR", 2, '''scale, rotate, translate ''')
L_RO_TR_SC = ConstType("L_RO_TR_SC", 3, '''rotate, translate, scale ''')
L_TR_RO_SC = ConstType("L_TR_RO_SC", 4, '''translate, rotate, scale ''')
L_RO_SC_TR = ConstType("L_RO_SC_TR", 5, '''rotate, scale, translate ''')
L_SC_TR_RO = ConstType("L_SC_TR_RO", 6, '''scale, translate, rotate ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                         Grayscale fill flags                            *
-------------------------------------------------------------------------*/
enum {
    L_FILL_WHITE = 1,           /* fill white pixels (e.g, in fg map)      */
    L_FILL_BLACK = 2            /* fill black pixels (e.g., in bg map)     */
}
    '''

ConstType.__name__ = "grayscale_fill_flags"

L_FILL_WHITE = ConstType("L_FILL_WHITE", 1, '''fill white pixels (e.g, in fg map) ''')
L_FILL_BLACK = ConstType("L_FILL_BLACK", 2, '''fill black pixels (e.g., in bg map) ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                           Dither parameters                             *
         If within this grayscale distance from black or white,          *
         do not propagate excess or deficit to neighboring pixels.       *
-------------------------------------------------------------------------*/
enum {
    DEFAULT_CLIP_LOWER_1 = 10,   /* dist to black with no prop; 1 bpp      */
    DEFAULT_CLIP_UPPER_1 = 10,   /* dist to black with no prop; 1 bpp      */
    DEFAULT_CLIP_LOWER_2 = 5,    /* dist to black with no prop; 2 bpp      */
    DEFAULT_CLIP_UPPER_2 = 5     /* dist to black with no prop; 2 bpp      */
}
    '''

ConstType.__name__ = "dither_parameters"

DEFAULT_CLIP_LOWER_1 = ConstType("DEFAULT_CLIP_LOWER_1", 10, '''dist to black with no prop; 1 bpp ''')
DEFAULT_CLIP_UPPER_1 = ConstType("DEFAULT_CLIP_UPPER_1", 10, '''dist to black with no prop; 1 bpp ''')
DEFAULT_CLIP_LOWER_2 = ConstType("DEFAULT_CLIP_LOWER_2", 5, '''dist to black with no prop; 2 bpp ''')
DEFAULT_CLIP_UPPER_2 = ConstType("DEFAULT_CLIP_UPPER_2", 5, '''dist to black with no prop; 2 bpp ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                             Distance flags                              *
-------------------------------------------------------------------------*/
enum {
    L_MANHATTAN_DISTANCE = 1,    /* L1 distance (e.g., in color space)     */
    L_EUCLIDEAN_DISTANCE = 2     /* L2 distance                            */
}
    '''

ConstType.__name__ = "distance_flags"

L_MANHATTAN_DISTANCE = ConstType("L_MANHATTAN_DISTANCE", 1, '''L1 distance (e.g., in color space) ''')
L_EUCLIDEAN_DISTANCE = ConstType("L_EUCLIDEAN_DISTANCE", 2, '''L2 distance ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                         Statistical measures                            *
-------------------------------------------------------------------------*/
enum {
    L_MEAN_ABSVAL = 1,           /* average of abs values                  */
    L_MEDIAN_VAL = 2,            /* median value of set                    */
    L_MODE_VAL = 3,              /* mode value of set                      */
    L_MODE_COUNT = 4,            /* mode count of set                      */
    L_ROOT_MEAN_SQUARE = 5,      /* rms of values                          */
    L_STANDARD_DEVIATION = 6,    /* standard deviation from mean           */
    L_VARIANCE = 7               /* variance of values                     */
}
    '''

ConstType.__name__ = "statistical_measures"

L_MEAN_ABSVAL = ConstType("L_MEAN_ABSVAL", 1, '''average of abs values ''')
L_MEDIAN_VAL = ConstType("L_MEDIAN_VAL", 2, '''median value of set ''')
L_MODE_VAL = ConstType("L_MODE_VAL", 3, '''mode value of set ''')
L_MODE_COUNT = ConstType("L_MODE_COUNT", 4, '''mode count of set ''')
L_ROOT_MEAN_SQUARE = ConstType("L_ROOT_MEAN_SQUARE", 5, '''rms of values ''')
L_STANDARD_DEVIATION = ConstType("L_STANDARD_DEVIATION", 6, '''standard deviation from mean ''')
L_VARIANCE = ConstType("L_VARIANCE", 7, '''variance of values ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                          Set selection flags                            *
-------------------------------------------------------------------------*/
enum {
    L_CHOOSE_CONSECUTIVE = 1,    /* select 'n' consecutive                 */
    L_CHOOSE_SKIP_BY = 2         /* select at intervals of 'n'             */
}
    '''

ConstType.__name__ = "set_selection_flags"

L_CHOOSE_CONSECUTIVE = ConstType("L_CHOOSE_CONSECUTIVE", 1, '''select 'n' consecutive ''')
L_CHOOSE_SKIP_BY = ConstType("L_CHOOSE_SKIP_BY", 2, '''select at intervals of 'n' ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                         Text orientation flags                          *
-------------------------------------------------------------------------*/
enum {
    L_TEXT_ORIENT_UNKNOWN = 0,   /* low confidence on text orientation     */
    L_TEXT_ORIENT_UP = 1,        /* portrait, text rightside-up            */
    L_TEXT_ORIENT_LEFT = 2,      /* landscape, text up to left             */
    L_TEXT_ORIENT_DOWN = 3,      /* portrait, text upside-down             */
    L_TEXT_ORIENT_RIGHT = 4      /* landscape, text up to right            */
}
    '''

ConstType.__name__ = "text_orientation_flags"

L_TEXT_ORIENT_UNKNOWN = ConstType("L_TEXT_ORIENT_UNKNOWN", 0, '''low confidence on text orientation ''')
L_TEXT_ORIENT_UP = ConstType("L_TEXT_ORIENT_UP", 1, '''portrait, text rightside-up ''')
L_TEXT_ORIENT_LEFT = ConstType("L_TEXT_ORIENT_LEFT", 2, '''landscape, text up to left ''')
L_TEXT_ORIENT_DOWN = ConstType("L_TEXT_ORIENT_DOWN", 3, '''portrait, text upside-down ''')
L_TEXT_ORIENT_RIGHT = ConstType("L_TEXT_ORIENT_RIGHT", 4, '''landscape, text up to right ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                         Edge orientation flags                          *
-------------------------------------------------------------------------*/
enum {
    L_HORIZONTAL_EDGES = 0,     /* filters for horizontal edges            */
    L_VERTICAL_EDGES = 1,       /* filters for vertical edges              */
    L_ALL_EDGES = 2             /* filters for all edges                   */
}
    '''

ConstType.__name__ = "edge_orientation_flags"

L_HORIZONTAL_EDGES = ConstType("L_HORIZONTAL_EDGES", 0, '''filters for horizontal edges ''')
L_VERTICAL_EDGES = ConstType("L_VERTICAL_EDGES", 1, '''filters for vertical edges ''')
L_ALL_EDGES = ConstType("L_ALL_EDGES", 2, '''filters for all edges ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                         Line orientation flags                          *
-------------------------------------------------------------------------*/
enum {
    L_HORIZONTAL_LINE = 0,     /* horizontal line                          */
    L_POS_SLOPE_LINE = 1,      /* 45 degree line with positive slope       */
    L_VERTICAL_LINE = 2,       /* vertical line                            */
    L_NEG_SLOPE_LINE = 3,      /* 45 degree line with negative slope       */
    L_OBLIQUE_LINE = 4         /* neither horizontal nor vertical */
}
    '''

ConstType.__name__ = "line_orientation_flags"

L_HORIZONTAL_LINE = ConstType("L_HORIZONTAL_LINE", 0, '''horizontal line ''')
L_POS_SLOPE_LINE = ConstType("L_POS_SLOPE_LINE", 1, '''45 degree line with positive slope ''')
L_VERTICAL_LINE = ConstType("L_VERTICAL_LINE", 2, '''vertical line ''')
L_NEG_SLOPE_LINE = ConstType("L_NEG_SLOPE_LINE", 3, '''45 degree line with negative slope ''')
L_OBLIQUE_LINE = ConstType("L_OBLIQUE_LINE", 4, '''neither horizontal nor vertical ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                           Scan direction flags                          *
-------------------------------------------------------------------------*/
enum {
    L_FROM_LEFT = 0,           /* scan from left                           */
    L_FROM_RIGHT = 1,          /* scan from right                          */
    L_FROM_TOP = 2,            /* scan from top                            */
    L_FROM_BOTTOM = 3          /* scan from bottom                         */
}
    '''

ConstType.__name__ = "scan_direction_flags"

L_FROM_LEFT = ConstType("L_FROM_LEFT", 0, '''scan from left ''')
L_FROM_RIGHT = ConstType("L_FROM_RIGHT", 1, '''scan from right ''')
L_FROM_TOP = ConstType("L_FROM_TOP", 2, '''scan from top ''')
L_FROM_BOTTOM = ConstType("L_FROM_BOTTOM", 3, '''scan from bottom ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                            Horizontal warp                              *
-------------------------------------------------------------------------*/
enum {
    L_WARP_TO_LEFT = 1,      /* increasing stretch or contraction to left  */
    L_WARP_TO_RIGHT = 2      /* increasing stretch or contraction to right */
}
    '''

ConstType.__name__ = "horizontal_warp"

L_WARP_TO_LEFT = ConstType("L_WARP_TO_LEFT", 1, '''increasing stretch or contraction to left ''')
L_WARP_TO_RIGHT = ConstType("L_WARP_TO_RIGHT", 2, '''increasing stretch or contraction to right ''')


del ConstType



class ConstType(Const):
    '''
       enum {
    L_LINEAR_WARP = 1,       /* stretch or contraction grows linearly      */
    L_QUADRATIC_WARP = 2     /* stretch or contraction grows quadratically */
}
    '''

ConstType.__name__ = "generated_constants"

L_LINEAR_WARP = ConstType("L_LINEAR_WARP", 1, '''stretch or contraction grows linearly ''')
L_QUADRATIC_WARP = ConstType("L_QUADRATIC_WARP", 2, '''stretch or contraction grows quadratically ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                      Pixel selection for resampling                     *
-------------------------------------------------------------------------*/
enum {
    L_INTERPOLATED = 1,      /* linear interpolation from src pixels       */
    L_SAMPLED = 2            /* nearest src pixel sampling only            */
}
    '''

ConstType.__name__ = "pixel_selection_for_resampling"

L_INTERPOLATED = ConstType("L_INTERPOLATED", 1, '''linear interpolation from src pixels ''')
L_SAMPLED = ConstType("L_SAMPLED", 2, '''nearest src pixel sampling only ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                             Thinning flags                              *
-------------------------------------------------------------------------*/
enum {
    L_THIN_FG = 1,               /* thin foreground of 1 bpp image         */
    L_THIN_BG = 2                /* thin background of 1 bpp image         */
}
    '''

ConstType.__name__ = "thinning_flags"

L_THIN_FG = ConstType("L_THIN_FG", 1, '''thin foreground of 1 bpp image ''')
L_THIN_BG = ConstType("L_THIN_BG", 2, '''thin background of 1 bpp image ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                            Runlength flags                              *
-------------------------------------------------------------------------*/
enum {
    L_HORIZONTAL_RUNS = 0,     /* determine runlengths of horizontal runs  */
    L_VERTICAL_RUNS = 1        /* determine runlengths of vertical runs    */
}
    '''

ConstType.__name__ = "runlength_flags"

L_HORIZONTAL_RUNS = ConstType("L_HORIZONTAL_RUNS", 0, '''determine runlengths of horizontal runs ''')
L_VERTICAL_RUNS = ConstType("L_VERTICAL_RUNS", 1, '''determine runlengths of vertical runs ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                          Edge filter flags                              *
-------------------------------------------------------------------------*/
enum {
    L_SOBEL_EDGE = 1,          /* Sobel edge filter                        */
    L_TWO_SIDED_EDGE = 2       /* Two-sided edge filter                    */
}
    '''

ConstType.__name__ = "edge_filter_flags"

L_SOBEL_EDGE = ConstType("L_SOBEL_EDGE", 1, '''Sobel edge filter ''')
L_TWO_SIDED_EDGE = ConstType("L_TWO_SIDED_EDGE", 2, '''Two-sided edge filter ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
          Handling negative values in conversion to unsigned int         *
-------------------------------------------------------------------------*/
enum {
    L_CLIP_TO_ZERO = 1,        /* Clip negative values to 0                */
    L_TAKE_ABSVAL = 2          /* Convert to positive using L_ABS()        */
}
    '''

ConstType.__name__ = "handling_negative_values_in_conversion_to_unsigned_int"

L_CLIP_TO_ZERO = ConstType("L_CLIP_TO_ZERO", 1, '''Clip negative values to 0 ''')
L_TAKE_ABSVAL = ConstType("L_TAKE_ABSVAL", 2, '''Convert to positive using L_ABS() ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
             Subpixel color component ordering in LCD display            *
-------------------------------------------------------------------------*/
enum {
    L_SUBPIXEL_ORDER_RGB = 1,   /* sensor order left-to-right RGB          */
    L_SUBPIXEL_ORDER_BGR = 2,   /* sensor order left-to-right BGR          */
    L_SUBPIXEL_ORDER_VRGB = 3,  /* sensor order top-to-bottom RGB          */
    L_SUBPIXEL_ORDER_VBGR = 4   /* sensor order top-to-bottom BGR          */
}
    '''

ConstType.__name__ = "subpixel_color_component_ordering_in_lcd_display"

L_SUBPIXEL_ORDER_RGB = ConstType("L_SUBPIXEL_ORDER_RGB", 1, '''sensor order left-to-right RGB ''')
L_SUBPIXEL_ORDER_BGR = ConstType("L_SUBPIXEL_ORDER_BGR", 2, '''sensor order left-to-right BGR ''')
L_SUBPIXEL_ORDER_VRGB = ConstType("L_SUBPIXEL_ORDER_VRGB", 3, '''sensor order top-to-bottom RGB ''')
L_SUBPIXEL_ORDER_VBGR = ConstType("L_SUBPIXEL_ORDER_VBGR", 4, '''sensor order top-to-bottom BGR ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                         Relative to zero flags                          *
-------------------------------------------------------------------------*/
enum {
    L_LESS_THAN_ZERO = 1,      /* Choose values less than zero             */
    L_EQUAL_TO_ZERO = 2,       /* Choose values equal to zero              */
    L_GREATER_THAN_ZERO = 3    /* Choose values greater than zero          */
}
    '''

ConstType.__name__ = "relative_to_zero_flags"

L_LESS_THAN_ZERO = ConstType("L_LESS_THAN_ZERO", 1, '''Choose values less than zero ''')
L_EQUAL_TO_ZERO = ConstType("L_EQUAL_TO_ZERO", 2, '''Choose values equal to zero ''')
L_GREATER_THAN_ZERO = ConstType("L_GREATER_THAN_ZERO", 3, '''Choose values greater than zero ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                          HSV histogram flags                            *
-------------------------------------------------------------------------*/
enum {
    L_HS_HISTO = 1,            /* Use hue-saturation histogram             */
    L_HV_HISTO = 2,            /* Use hue-value histogram                  */
    L_SV_HISTO = 3             /* Use saturation-value histogram           */
}
    '''

ConstType.__name__ = "hsv_histogram_flags"

L_HS_HISTO = ConstType("L_HS_HISTO", 1, '''Use hue-saturation histogram ''')
L_HV_HISTO = ConstType("L_HV_HISTO", 2, '''Use hue-value histogram ''')
L_SV_HISTO = ConstType("L_SV_HISTO", 3, '''Use saturation-value histogram ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                    Region flags (inclusion, exclusion)                  *
-------------------------------------------------------------------------*/
enum {
    L_INCLUDE_REGION = 1,      /* Use hue-saturation histogram             */
    L_EXCLUDE_REGION = 2       /* Use hue-value histogram                  */
}
    '''

ConstType.__name__ = "region_flags_(inclusion,_exclusion)"

L_INCLUDE_REGION = ConstType("L_INCLUDE_REGION", 1, '''Use hue-saturation histogram ''')
L_EXCLUDE_REGION = ConstType("L_EXCLUDE_REGION", 2, '''Use hue-value histogram ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                    Flags for adding text to a pix                       *
-------------------------------------------------------------------------*/
enum {
    L_ADD_ABOVE = 1,           /* Add text above the image                 */
    L_ADD_AT_TOP = 2,          /* Add text over the top of the image       */
    L_ADD_AT_BOTTOM = 3,       /* Add text over the bottom of the image    */
    L_ADD_BELOW = 4            /* Add text below the image                 */
}
    '''

ConstType.__name__ = "flags_for_adding_text_to_a_pix"

L_ADD_ABOVE = ConstType("L_ADD_ABOVE", 1, '''Add text above the image ''')
L_ADD_AT_TOP = ConstType("L_ADD_AT_TOP", 2, '''Add text over the top of the image ''')
L_ADD_AT_BOTTOM = ConstType("L_ADD_AT_BOTTOM", 3, '''Add text over the bottom of the image ''')
L_ADD_BELOW = ConstType("L_ADD_BELOW", 4, '''Add text below the image ''')


del ConstType



class ConstType(Const):
    '''
       -------------------------------------------------------------------------*
                   Flags for selecting display program                   *
-------------------------------------------------------------------------*/
enum {
    L_DISPLAY_WITH_XV = 1,      /* Use xv with pixDisplay()                */
    L_DISPLAY_WITH_XLI = 2,     /* Use xli with pixDisplay()               */
    L_DISPLAY_WITH_XZGV = 3,    /* Use xzgv with pixDisplay()              */
    L_DISPLAY_WITH_IV = 4       /* Use irfvanview with pixDisplay()        */
}
    '''

ConstType.__name__ = "flags_for_selecting_display_program"

L_DISPLAY_WITH_XV = ConstType("L_DISPLAY_WITH_XV", 1, '''Use xv with pixDisplay() ''')
L_DISPLAY_WITH_XLI = ConstType("L_DISPLAY_WITH_XLI", 2, '''Use xli with pixDisplay() ''')
L_DISPLAY_WITH_XZGV = ConstType("L_DISPLAY_WITH_XZGV", 3, '''Use xzgv with pixDisplay() ''')
L_DISPLAY_WITH_IV = ConstType("L_DISPLAY_WITH_IV", 4, '''Use irfvanview with pixDisplay() ''')


del ConstType



class ConstType(Const):
    '''
       ------------------------------------------------------------------------* 
                              Array flags                               *
------------------------------------------------------------------------*/

 Flags for removal from L_Ptra */
enum {
    L_NO_COMPACTION = 1,        /* null the pointer only  */
    L_COMPACTION = 2            /* compact the array      */
}
    '''

ConstType.__name__ = "array_flags"

L_NO_COMPACTION = ConstType("L_NO_COMPACTION", 1, '''null the pointer only ''')
L_COMPACTION = ConstType("L_COMPACTION", 2, '''compact the array ''')


del ConstType



class ConstType(Const):
    '''
        Flags for insertion into L_Ptra */
enum {
    L_AUTO_DOWNSHIFT = 0,       /* choose based on number of holes        */
    L_MIN_DOWNSHIFT = 1,        /* downshifts min # of ptrs below insert  */
    L_FULL_DOWNSHIFT = 2        /* downshifts all ptrs below insert       */
}
    '''

ConstType.__name__ = "flags_for_insertion_into_l_ptra"

L_AUTO_DOWNSHIFT = ConstType("L_AUTO_DOWNSHIFT", 0, '''choose based on number of holes ''')
L_MIN_DOWNSHIFT = ConstType("L_MIN_DOWNSHIFT", 1, '''downshifts min # of ptrs below insert ''')
L_FULL_DOWNSHIFT = ConstType("L_FULL_DOWNSHIFT", 2, '''downshifts all ptrs below insert ''')


del ConstType



class ConstType(Const):
    '''
        Accessor flags for L_Ptraa */
enum {
    L_HANDLE_ONLY = 0,          /* ptr to L_Ptra; caller can inspect only    */
    L_REMOVE = 1                /* caller owns; destroy or save in L_Ptraa   */
}
    '''

ConstType.__name__ = "accessor_flags_for_l_ptraa"

L_HANDLE_ONLY = ConstType("L_HANDLE_ONLY", 0, '''ptr to L_Ptra; caller can inspect only ''')
L_REMOVE = ConstType("L_REMOVE", 1, '''caller owns; destroy or save in L_Ptraa ''')


del ConstType



class ConstType(Const):
    '''
        ----------------------------------------------------------------- *
   *            Flags for method of extracting barcode widths          *
   * ----------------------------------------------------------------- */
enum {
    L_USE_WIDTHS = 1,           /* use histogram of barcode widths           */
    L_USE_WINDOWS = 2           /* find best window for decoding transitions */
}
    '''

ConstType.__name__ = "flags_for_method_of_extracting_barcode_widths"

L_USE_WIDTHS = ConstType("L_USE_WIDTHS", 1, '''use histogram of barcode widths ''')
L_USE_WINDOWS = ConstType("L_USE_WINDOWS", 2, '''find best window for decoding transitions ''')


del ConstType



class ConstType(Const):
    '''
        ----------------------------------------------------------------- *
   *                     Flags for barcode formats                     *
   * These are used both to identify a barcode format and to identify  *
   * the decoding method to use on a barcode.                          *
   * ----------------------------------------------------------------- */
enum {
    L_BF_UNKNOWN = 0,           /* unknown format                            */
    L_BF_ANY = 1,               /* try decoding with all known formats       */
    L_BF_CODE128 = 2,           /* decode with Code128 format                */
    L_BF_EAN8 = 3,              /* decode with EAN8 format                   */
    L_BF_EAN13 = 4,             /* decode with EAN13 format                  */
    L_BF_CODE2OF5 = 5,          /* decode with Code 2 of 5 format            */
    L_BF_CODEI2OF5 = 6,         /* decode with Interleaved 2 of 5 format     */
    L_BF_CODE39 = 7,            /* decode with Code39 format                 */
    L_BF_CODE93 = 8,            /* decode with Code93 format                 */
    L_BF_CODABAR = 9,           /* decode with Code93 format                 */
    L_BF_UPCA = 10              /* decode with UPC A format                  */
}
    '''

ConstType.__name__ = "flags_for_barcode_formats"

L_BF_UNKNOWN = ConstType("L_BF_UNKNOWN", 0, '''unknown format ''')
L_BF_ANY = ConstType("L_BF_ANY", 1, '''try decoding with all known formats ''')
L_BF_CODE128 = ConstType("L_BF_CODE128", 2, '''decode with Code128 format ''')
L_BF_EAN8 = ConstType("L_BF_EAN8", 3, '''decode with EAN8 format ''')
L_BF_EAN13 = ConstType("L_BF_EAN13", 4, '''decode with EAN13 format ''')
L_BF_CODE2OF5 = ConstType("L_BF_CODE2OF5", 5, '''decode with Code 2 of 5 format ''')
L_BF_CODEI2OF5 = ConstType("L_BF_CODEI2OF5", 6, '''decode with Interleaved 2 of 5 format ''')
L_BF_CODE39 = ConstType("L_BF_CODE39", 7, '''decode with Code39 format ''')
L_BF_CODE93 = ConstType("L_BF_CODE93", 8, '''decode with Code93 format ''')
L_BF_CODABAR = ConstType("L_BF_CODABAR", 9, '''decode with Code93 format ''')
L_BF_UPCA = ConstType("L_BF_UPCA", 10, '''decode with UPC A format ''')


del ConstType



class ConstType(Const):
    '''
        For printing out array data */
enum {
    L_SUDOKU_INIT = 0,
    L_SUDOKU_STATE = 1
}
    '''

ConstType.__name__ = "for_printing_out_array_data"

L_SUDOKU_INIT = ConstType("L_SUDOKU_INIT", 0, ''' ''')
L_SUDOKU_STATE = ConstType("L_SUDOKU_STATE", 1, ''' ''')


del ConstType



globals_copy = globals().copy()
__all__ = [const for const in globals_copy if isinstance(const, Const)] + [find_siblings]

del const, globals_copy
