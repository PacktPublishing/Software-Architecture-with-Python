# Code Listing #9

"""

Sort a number of disk files using a counter - a dictionary that keeps counts of numbers.

"""

# sort_counter.py
import sys
import collections

MAXINT = 100000

def sort():
    """ Sort files on disk by using a counter """
    
    counter = collections.defaultdict(int)
    
    for i in range(int(sys.argv[1])):
        filename = 'numbers/numbers_%d.txt' % i
        for n in open(filename):
            counter[n] += 1
    
    
    print('Sorting...')

    with open('sorted_nums.txt','w') as fp:
        for i in range(1, MAXINT+1):
            count = counter.get(str(i) + '\n', 0)
            if count>0:
                fp.write((str(i)+'\n')*count)

    print('Sorted')

if __name__ == "__main__":
    sort()
