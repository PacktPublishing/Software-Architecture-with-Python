# Code Listing #8

"""

Sort a number of disk files in memory - using normal list sort

"""

import sys


def sort():
    all_lists = []
    
    for i in range(int(sys.argv[1])):
        num_list = map(int, open('numbers/numbers_%d.txt' % i).readlines())
        all_lists += num_list

    print('Length of list',len(all_lists))
    print('Sorting...')
    all_lists.sort()
    open('sorted_nums.txt','w').writelines('\n'.join(map(str, all_lists)) + '\n')
    print('Sorted')

if __name__ == "__main__":
    sort()
