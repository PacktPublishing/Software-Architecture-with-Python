# Code listing #25

"""
Module metrictest.py

Metric example - Module which is used as a testbed for static checkers.
This is a mix of different functions and classes doing different things.

"""

# Note: This version is written for testing with pyflakes and called metrictest2.py

import sys

def fn(x, y):
    """ A function which performs a sum """
    return x + y

def find_optimal_route_to_my_office_from_home(start_time,
                                    expected_time,
                                    favorite_route='SBS1K',
                                    favorite_option='bus'):

    # If I am very late, always drive.
    d = expected_time - start_time

    if d<=30:
        return 'car'

    # If d>30 but <45, first drive then take metro
    if d>30 and d<45:
        return ('car', 'metro')

    # If d>45 there are a combination of options
    if d>45:
        if d<60:
            # First volvo,then connecting bus
            return ('bus:335E','bus:connector')
        elif d>80:
            # Might as well go by normal bus
            return random.choice(('bus:330','bus:331',':'.join((favorite_option,
                                                                favorite_route))))
        elif d>90:
            # Relax and choose favorite route
            return ':'.join((favorite_option,
                             favorite_route))


class C(object):
    """ A class which does almost nothing """

    def __init__(self, x,y):
        self.x = x
        self.y = y

    def f(self):
        pass

    def g(self, x, y):

        if self.x>x:
            return self.x+self.y
        elif x>self.x:
            return x+ self.y

class D(C):
    """ D class """

    def __init__(self, x):
        self.x = x

    def f(self, x,y):
        if x>y:
            return x-y
        else:
            return x+y

    def g(self, y):

        if self.x>y:
            return self.x+y
        else:
            return y-self.x

def myfunc(a, b):
    if a>b:
        return c
    else:
        return a
