# Code listing #8

def rms(varray=[]):
    """ RMS velocity """

    squares = map(lambda x: x*x, varray)
    return pow(sum(squares), 0.5) 
    

def rms(varray=[]):
    """ Root mean squared velocity. Returns
    square root of sum of squares of velocities """

    squares = map(lambda x: x*x, varray)
    return pow(sum(squares), 0.5) 
