# Code Listing - #9

"""
Module factorial - Demonstrating an example of writing doctests
"""

import functools
import operator

def factorial(n):
    """ Factorial of a number.

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(10)
    3628800
    """

    # Handle 0 as a special case
    if n == 0:
        return 1
    
    return functools.reduce(operator.mul, range(1,n+1))
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
