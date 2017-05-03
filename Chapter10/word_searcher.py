# Code Listing #5

"""

Word searcher program - search for a word in a list of files
and return list of lines containing the word.

"""

# word_searcher.py

import os
import sys
import glob

def grep_word(word, filenames):
    """ Open the given files and look for a specific word.
    Append lines containing word to a list and
    return it """

    lines, words = [], []
    
    for filename in filenames:
        print('Processing',filename)
        lines += open(filename).readlines()


    # Debugging steps
    # 1. sys.exit
    # sys.exit('Exiting after first loop')
    
    word = word.lower()
    for line in lines:
        if word in line.lower():
            # 2. continue statement in a loop
            # continue          
            words.append(line.strip())
            # The bug can be reproduced by commenting
            # above line and uncommenting below line
            # lines.append(line.strip())

    # Now sort the list according to length of lines
    return sorted(words, key=len)
    
if __name__ == "__main__":
    print('Lines => ', grep_word('lines', glob.glob('*.py')))

    
