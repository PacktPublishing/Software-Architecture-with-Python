# Code Listing - #11

"""
Module test_palindrome - TDD for palindrome module
"""

# Note: This is the first version of test_palindrome, so called test_palindrome1.py

import palindrome

def test_basic():
    """ Basic test for palindrome """

    # True positives
    for test in ('Rotator','bob','madam','mAlAyAlam', '1'):
        assert palindrome.is_palindrome(test)==True

    # True negatives
    for test in ('xyz','elephant', 'Country'):
        assert palindrome.is_palindrome(test)==False        

