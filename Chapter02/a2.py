# Code listing #12

""" Module A (a.py) - Implement functions that operate on series of numbers """

# Note - this is rewritten version of a1, so called a2.py

def squares(narray):
    """ Return array of squares of numbers """
    return pow_n(array, 2)

def cubes(narray):
    """ Return array of cubes of numbers """
    return pow_n(narray, 3)

def pow_n(narray, n):
    """ Return array of numbers raised to arbitrary power n each """
    return [pow(x, n) for x in narray]
