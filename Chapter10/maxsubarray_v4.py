# Code Listing #4

"""

Maximum subarray problem - final version

"""

from contextlib import contextmanager
import random
import time

@contextmanager
def timer():
    """ Measure real-time execution of a block of code """
    
    try:
        start = time.time()
        yield
    finally:
        end = (time.time() - start)*1000
        print('time taken=> %.2f ms' % end)

def num_array(size):
    """ Return a list of numbers in a fixed random range
    of given size """

    nums = []
    for i in range(size):
        nums.append(random.randrange(-25, 30))
    return nums
        
def max_subarray1(sequence):
    """ Find sub-sequence in sequence having maximum sum """

    # this is the version before the final version for testing purposes
    
    max_sum, max_sub = 0, []
    
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            sub_seq = sequence[i:j+1]
            sum_s = sum(sub_seq)
            if sum_s > max_sum:
                max_sum, max_sub = sum_s, sub_seq

    return max_sum, max_sub

def max_subarray(sequence):
    """ Maximum subarray - optimized version """

    max_ending_here = max_so_far = 0
    for x in sequence:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

if __name__ == "__main__":

    #with timer():
    #    max_subarray1(num_array(10000))
    
    print(max_subarray([-5, 20, -10, 30, 15]))
