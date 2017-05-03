# Code listing #19

""" Module rankbase - Logic for ranking text using degree of word frequency """

import operator

class RankBase(object):
    """ Accept text data as inputs and rank them in
    terms of how much a word occurs in them """

    def __init__(self, word):
        self.word = word.strip().lower()

    def rank(self, *texts):
        """ Rank input data. A tuple is returned with
        (idx, #occur) in decreasing order of
        occurences """

        occurs = {}
        
        for idx,text in enumerate(texts):
            # print text
            words = map(lambda x: x.lower().strip(), text.split())
            count = words.count(self.word)
            occurs[idx] = count

        # Return dictionary
        return occurs

    def sort(self, occurs):
        """ Return the ranking data in sorted order """

        return sorted(occurs, key=operator.itemgetter(1), reverse=True) 

