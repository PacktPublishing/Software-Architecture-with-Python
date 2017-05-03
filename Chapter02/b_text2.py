# Code listing #16

""" Module B (b.py) - Provides text processing functions to user """

# Note: This is the rewritten version of b_text.py so called b_text2.py

import a_text2 as a

def common_words(filename1, filename2):
    """ Return common words across two input files """
    
    lines1 = open(filename1).read()
    lines2 = open(filename2).read()
    
    return a.common_words(lines1, lines2)
