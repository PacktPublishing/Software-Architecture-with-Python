# Code Listing - #14

"""
Module palindrome - Returns whether an input string is palindrome or not
"""
# Note - this is the second version of palindrome, so called palindrome2.py

import re

def is_palindrome(in_string):
    """ Returns True whether in_string is palindrome, False otherwise """

    # Case insensitive
    in_string = in_string.lower()
    # Purge spaces
    in_string = re.sub('\s+','', in_string)
    # Check if string is same as in reverse
    return in_string == in_string[-1::-1]
