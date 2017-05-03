# Code Listing - #3

"""

StreamHasher - Class providing hashing of data from an input stream
using pluggable algorithms

"""

# NOTE: This combines the two methods provided in the book into one class.

class StreamHasher(object):
    """ Stream hasher class with configurable algorithm """
    
    def __init__(self, algorithm, chunk_size=4096):
        self.chunk_size = chunk_size
        self.hash = algorithm()

    def get_hash(self, stream):
        """ Return the hash digest """
        
        for chunk in iter(lambda: stream.read(self.chunk_size), ''):
            self.hash.update(chunk.encode('utf-8'))

        return self.hash.hexdigest()
    
    def __call__(self, stream):

        return self.get_hash(stream)

if __name__ == "__main__":
    from hashlib import md5, sha1
    
    md5h = StreamHasher(algorithm=md5)
    # Both works
    print(md5h(open('hasher.py')))  
    shah_h = StreamHasher(algorithm=sha1)
    print(shah_h(open('hasher.py')))
    
