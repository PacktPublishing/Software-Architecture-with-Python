# Code Listing #8

"""

Examples of using OrderedDict

"""

from collections import OrderedDict

cities = ['Jakarta','Delhi','Newyork','Bonn','Kolkata','Bangalore','Seoul']
# Dictionary
cities_dict = dict.fromkeys(cities)
print(cities_dict)
# Ordered dictionary
ocities_dict = OrderedDict.fromkeys(cities)
print(ocities_dict)

# Dropping duplicates while preserving order with Ordered dictionary
cities = ['Jakarta','Delhi','Newyork','Bonn','Kolkata','Bangalore','Bonn','Seoul','Delhi','Jakarta','Mumbai']
cities_odict = OrderedDict.fromkeys(cities)
print(cities_odict.keys())
print(cities_odict.popitem())
print(cities_odict.popitem(last=False))

# class LRU
class LRU(OrderedDict):
    """ Least recently used cache (LRU) dictionary
    using OrderedDict
    
    """
    
    def __init__(self, size=10):
        self.size = size

    def set(self, key):
        # If key is there delete and reinsert so
        # it moves to end.
        if key in self:
            del self[key]

        self[key] = 1
        if len(self)>self.size:
            # Pop from left
            self.popitem(last=False)

if __name__ == "__main__":
     d=LRU(size=5)
     d.set('bangalore')
     d.set('chennai')
     d.set('mumbai')
     # Bangalore is set again - moves to right
     d.set('bangalore')
     d.set('kolkata')
     d.set('delhi')
     # Chennai is set again - so moves to right
     d.set('chennai')
    
     print('Length=>',len(d))
     print(d)
     # Kochi is appended and mumbai drops off
     d.set('kochi')
     print(d)
