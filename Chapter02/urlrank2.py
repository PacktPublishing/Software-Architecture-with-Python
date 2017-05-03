# Code listing #21

""" Module urlrank - Rank URLs in order of degree of a specific word frequency """

# Note: This is urlrank.py rewritten to use rankbase so called urlrank2.py

import requests
import operator

from rankbase import RankBase

class UrlRank(object):
    """ Accept URLs as inputs and rank them in
    terms of how much a word occurs in them """

    def __init__(self, word, *urls):
        self.word = word.strip().lower()
        self.urls = urls

    def rank(self):
        """ Rank the URLs. A tuple is returned with
        (url, #occur) in decreasing order of
        occurences """

        occurs = []
        
        for url in self.urls:
            data = requests.get(url).content
            words = map(lambda x: x.lower().strip(), data.split())
            # Filter empty words
            count = words.count(self.word)
            occurs.append((url, count))

        # Return in sorted order
        return sorted(occurs, key=operator.itemgetter(1), reverse=True)

class UrlRank(RankBase):
    """ Accept URLs as inputs and rank them in
    terms of how much a word occurs in them """

    def __init__(self, word, *urls):
        self.word = word.strip().lower()
        self.urls = urls

    def rank(self):
        """ Rank the URLs. A tuple is returned with
        (url, #occur) in decreasing order of
        occurences """

        texts = map(lambda x: requests.get(x).content, self.urls)
        occurs = super(UrlRank, self).rank(*texts)
        # Convert to URLs list
        occurs = [(self.urls[x],y) for x,y in occurs.items()]

        return self.sort(occurs)

if __name__ == "__main__":
    import sys
    print(UrlRank('python',*sys.argv[1:]).rank())
