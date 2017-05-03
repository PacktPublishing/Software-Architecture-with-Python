# Code Listing #4

"""

Code testing the 'eval' function for security holes - version #2

"""

import sys


def run_code(string):
    """ Evaluate the passed string as code """
    
    try:
        # Pass __builtins__ dictionary as empty
        eval(string, {'__builtins__':{}})
    except Exception as e:
        print(repr(e))

if __name__ == "__main__":
    run_code(sys.argv[1])
