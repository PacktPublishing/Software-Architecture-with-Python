# Code Listing - #12

"""
Module palindrome - Returns whether an input string is palindrome or not
"""

# Note - this is the first version of palindrome, so called palindrome1.py

def is_palindrome(in_string):
    """ Returns True whether in_string is palindrome, False otherwise """

    # Case insensitive
    in_string = in_string.lower()
    # Check if string is same as in reverse
    return in_string == in_string[-1::-1]
