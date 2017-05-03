# Code Listing #6

"""

Example with collections.deque for rotating sequences

"""

from collections import deque

def rotate_seq1(seq1, n):
    """ Rotate a sequence left by n """
    # E.g: rotate([1,2,3,4,5], 2) => [4,5,1,2,3]

    k = len(seq1) - n
    return seq1[k:] + seq1[:k]

def rotate_seq2(seq1, n):
    """ Rotate a sequence left by n using deque """
    
    d = deque(seq1)
    d.rotate(n)
    return d
