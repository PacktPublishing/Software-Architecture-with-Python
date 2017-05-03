# Code listing #28

""" Module metrictest.py - testing static quality metrics of Python code """

# Note: This is the final version of metrictest.py so called just metrictest.py

import random

def sum_fn(xnum, ynum):
    """ A function which performs a sum """

    return xnum + ynum

def find_optimal_route(start_time,
                       expected_time,
                       favorite_route='SBS1K',
                       favorite_option='bus'):
    """ Find optimal route for me to go from home to office.
    First two inputs should be datetime instances.
    
    """
    
    # Convert to minutes
    tdiff = (expected_time - start_time).total_seconds()/60.0

    options = {range(0, 30): 'car',
               range(30, 45): ('car', 'metro'),
               range(45, 60): ('bus:335E', 'bus:connector')}


    if tdiff < 80:
        # Pick the range it falls into
        for drange in options:
            if tdiff in drange:
                return drange[tdiff]
            
    # Might as well go by normal bus
    return random.choice(('bus:330', 'bus:331',':'.join((favorite_option,
                                                         favorite_route))))

    
class MiscClassC(object):
    """ A class which does almost nothing """

    def __init__(self, xnum, ynum):
        self.xnum = xnum
        self.ynum = ynum
        
    def compare_and_sum(self, xnum=0, ynum=0):
        """ Compare local and argument variables
        and perform some sums """
        
        if self.xnum > xnum:
            return self.xnum + self.ynum
        else:
            return xnum + self.ynum

class MiscClassD(MiscClassC):
    """ Sub-class of MiscClassC """

    def __init__(self, xnum, ynum=0):
        super(MiscClassD, self).__init__(xnum, ynum)

    def some_func(self, xnum,ynum):
        """ A function which does summing """
        
        if xnum > ynum:
            return xnum - ynum
        else:
            return xnum + ynum

    def compare_and_sum(self, xnum=0, ynum=0):
        """ Compare local and argument variables
        and perform some sums """

        if self.xnum > ynum:
            return self.xnum + ynum
        else: 
            return ynum - self.xnum
