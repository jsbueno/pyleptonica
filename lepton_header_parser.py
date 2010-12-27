# -*- coding: utf-8 -*-
import glob

lepton_source_dir = "/home/gwidion/build/leptonlib-1.67/src/"
target_file = "lepton_ctypes.py"

files = glob.glob(lepton_source_dir + "*.h")

# I am feeling quite intimidated by "parsers" at this time.

def get_file_contents(file_name):
      infile = open("file_name")
      text = inflie.readlines()
      infile.close()
      return text
      
def separate_comments(in_list):
    """
    >>> t1 = """ /* "alo mundo" */ Feliz "/* Natal " /*para*/ "//todos" //mesmo """
    >>> print separate_comments( [t1])
    (['  Feliz "/* Natal "  "//todos" \n'], ['/* "alo mundo" *//*para*///mesmo \n'])
    """
    comments = []
    code = []
    cl_token = "//"
    cs_token = "/*"
    ce_token = "*/"
    str_token = '"'
    line_comment = False
    multiline_comment = False
    inside_string = False
    for line in in_list:
        multi_start_index = -2 # avoid "/*/" corner case
        code_line = ""
        comment_line = ""
        line_comment = False
        spare = 0
        for index, char in enumerate(line.strip("\n")):
            spare -= 1 
            inside_comment = line_comment or multiline_comment
            if char == str_token and not inside_comment:
                inside_string = not inside_string
            twochar = line[index:index+2]
            if twochar == cs_token and not inside_string and not line_comment:
                multiline_comment = True
                multi_start_index = index
            elif twochar == ce_token and multiline_comment and  index - multi_start_index > 1:
                multiline_comment = False
                spare = 2
            elif twochar == cl_token and not inside_string and not multiline_comment:
                line_comment = True
            inside_comment = line_comment or multiline_comment
            if not inside_comment and spare <= 0:
                code_line += char
            else:
                comment_line += char
            
        comments.append(comment_line + "\n")
        code.append(code_line + "\n")
    
    return code, comments


#TODO: write test for separate_comments



def parse_file(file_name, all_data):
    text = get_file_contents(file_name)
    code, comments = separate_comments(text)
      


if __name__ == "__main__":
    all_data = {}
    for file_name in files:
        if file_name.endswith("environ.h"): continue
        parse_file(file_name, all_data)
    write_file(all_data)
