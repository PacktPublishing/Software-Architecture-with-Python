# Code Listing #2

"""
Take an input stream and hash it's contents and return the hash digest
- contains md5 and sha1 implementations.

"""

# hash_stream.py
from hashlib import sha1

def hash_stream_sha1(stream, chunk_size=4096):
    """ Hash a stream of data using sha1 """
    
    shash = sha1()
    
    for chunk in iter(lambda: stream.read(chunk_size), ''):
        shash.update(chunk)

    return shash.hexdigest()

def hash_stream_md5(stream, chunk_size=4096):
    """ Hash a stream of data using md5 """
    
    shash = md5()
    
    for chunk in iter(lambda: stream.read(chunk_size), ''):
        shash.update(chunk)

    return shash.hexdigest()
