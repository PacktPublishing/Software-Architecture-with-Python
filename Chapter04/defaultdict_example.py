# Code Listing #7

"""

Examples of using defaultdict

"""

from collections import defaultdict

counts = {}
text="""Python is an interpreted language. Python is an object-oriented language.
Python is easy to learn. Python is an open source language. """
word="Python"

# Implementations with simple dictionary
for word in text.split():
    word = word.lower().strip() 
    try:
        counts[word] += 1
    except KeyError:
        counts[word] = 1

print("Counts of word",word,'=>',counts[word])

cities = ['Jakarta','Delhi','Newyork','Bonn','Kolkata','Bangalore','Seoul']
cities_len = {}
for city in cities:
    clen = len(city)
    # First create entry
    if clen not in cities_len:
        cities_len[clen] = []
    cities_len[clen].append(city)

print('Cities grouped by length=>',cities_len)

# Implementation using default dict
# 1. Counts
counts = defaultdict(int)
for word in text.split():
    word = word.lower().strip() 
    # Value is set to 0 and incremented by 1 in one go
    counts[word] += 1

print("Counts of word",word,'=>',counts[word])

# 2. Cities grouped by length
cities = ['Jakarta','Delhi','Newyork','Bonn','Kolkata','Bangalore','Seoul']
cities_len = defaultdict(list)

for city in cities:
    # Empty list is created as value and appended to in one go
    cities_len[len(city)].append(city)

    
print('Cities grouped by length=>',cities_len)
