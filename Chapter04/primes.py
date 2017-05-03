# Code Listing #3
"""

Prime number iterator class

"""

class Prime(object):
    """ A prime number iterator for first 'n' primes """

    def __init__(self, n):
        self.n = n
        self.count = 0
        self.value = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        """ Return next item in iterator """

        if self.count == self.n:
            raise StopIteration("end of iteration")
        return self.compute()

    # Uncomment next line for profiling with line profiler
    # or memory profiler.
    # @profile
    def is_prime(self):
        """ Whether current value is prime ? """

        vroot = int(self.value ** 0.5) + 1
        for i in range(3, vroot, 2):
            if self.value % i == 0:
                return False
        return True
            
    def compute(self):
        """ Compute next prime """

        # Second time, reset value
        if self.count == 1:
            self.value = 1
            
        while True:
            self.value += 2
            
            if self.is_prime():
                self.count += 1
                break

        return self.value

if __name__ == "__main__":
    l=list(Prime(1000))
