# Code Listing #12
"""

Example of using bloom filter

NOTE: This works only with Python2.x

"""

from pybloom import BloomFilter
import requests

# Uncomment for profiling with line profiler or memory profiler

# @profile
def hound():
    f=BloomFilter(capacity=100000, error_rate=0.01)
    text=requests.get('https://www.gutenberg.org/files/2852/2852-0.txt').text

    for word in text.split():
        word = word.lower().strip()
        f.add(word)

    print len(f)
    print len(text.split())

    for w in ('holmes','watson','hound','moor','queen'):
        print 'Found',w,w in f
    

if __name__ == "__main__":
    hound()

    

