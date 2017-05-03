# Code Listing #9

"""

Return top 10 most common words from the online text of the "The Hound of Baskervilles"

"""

import requests, operator
from collections import defaultdict, Counter

print('Using defaultdict')
text=requests.get('https://www.gutenberg.org/files/2852/2852-0.txt').text
freq=defaultdict(int)

for word in text.split():
    if len(word.strip())==0: continue
    freq[word.lower()] += 1
    
print(sorted(freq.items(), key=operator.itemgetter(1), reverse=True)[:10])

print('Using Counter')
freq=Counter(filter(None, map(lambda x:x.lower().strip(), text.split())))
print(freq.most_common(10))
