# Code Listing #4
"""

Memory profiler example

"""

@profile
def squares(n):
    return [x*x for x in range(1, n+1)]

squares(1000000)
