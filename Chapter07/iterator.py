# Code Listing #13

"""

The iterator pattern - A prime number iterator

"""

import itertools

class Prime(object):
    """ An iterator for prime numbers """

    def __init__(self, initial, final=0):
        """ Initializer - accepts a number """
        # This may or may not be prime
        self.current = initial
        self.final = final
        
    def __iter__(self):
        return self

    def __next__(self):
        """ Return next item in iterator """
        return self._compute()

    def _compute(self):
        """ Compute the next prime number """

        num = self.current
        
        while True:
            is_prime = True
            
            # Check this number
            for x in range(2, int(pow(self.current, 0.5)+1)):
                if self.current%x==0:
                    is_prime = False
                    break


            num = self.current
            self.current += 1

            if is_prime:
                return num
            
            # If there is an end range, look for it
            if self.final>0 and self.current>self.final:
                raise StopIteration
            
if __name__ == "__main__":
    print(list(Prime(2,50)))
    # First 100 primes
    print(list(itertools.islice(Prime(2), 100)))
    # First 10 primes ending with 1
    print(list(itertools.islice(itertools.filterfalse(lambda x: x % 10 != 1, Prime(2)), 10)))
    # First 10 palindromic primes
    print(list(itertools.islice(itertools.filterfalse(lambda x: str(x)!=str(x)[-1::-1], Prime(10)), 10)))
