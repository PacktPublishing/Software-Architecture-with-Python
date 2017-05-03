# Code Listing #9

"""

Adapter design pattern - Class Adapter

"""

import itertools

class Polygon(object):
    """ A polygon class """
    
    def __init__(self, *sides):
        """ Initializer - accepts length of sides """
        self.sides = sides
        
    def perimeter(self):
        """ Return perimeter """
        
        return sum(self.sides)
    
    def is_valid(self):
        """ Is this a valid polygon """
        
        # Do some complex stuff - not implemented in base class
        raise NotImplementedError
    
    def is_regular(self):
        """ Is a regular polygon ? """
        
        # Yes: if all sides are equal
        side = self.sides[0]
        return all([x==side for x in self.sides[1:]])
    
    def area(self):
        """ Calculate and return area """
        
        # Not implemented in base class
        raise NotImplementedError

class InvalidPolygonError(Exception):
    pass

class Triangle(Polygon):
    """ Triangle class from Polygon using class adapter """
    
    def is_equilateral(self):
        """ Is this an equilateral triangle ? """
        
        if self.is_valid():
            return super(Triangle, self).is_regular()
    
    def is_isosceles(self):
        """ Is the triangle isosceles """
        
        if self.is_valid():
            # Check if any 2 sides are equal
            for a,b in itertools.combinations(self.sides, 2):
                if a == b:
                    return True
        return False
    
    def area(self):
        """ Calculate area """
        
        # Using Heron's formula
        p = self.perimeter()/2.0
        total = p
        for side in self.sides:
            total *= abs(p-side)
            
        return pow(total, 0.5)
    
    def is_valid(self):
        """ Is the triangle valid """
        
        # Sum of 2 sides should be > 3rd side
        perimeter = self.perimeter()
        for side in self.sides:
            sum_two = perimeter - side
            if sum_two <= side:
                raise InvalidPolygonError(str(self.__class__) + "is invalid!")
                
        return True

class Rectangle(Polygon):
    """ Rectangle class from Polygon using class adapter """

    def is_square(self):
        """ Return if I am a square """

        if self.is_valid():
            # Defaults to is_regular
            return self.is_regular()

    def is_valid(self):
        """ Is the rectangle valid """

        # Should have 4 sides
        if len(self.sides) != 4:
            return False

        # Opposite sides should be same
        for a,b in [(0,2),(1,3)]:
            if self.sides[a] != self.sides[b]:
                return False

        return True

    def area(self):
        """ Return area of rectangle """

        # Length x breadth
        if self.is_valid():
            return self.sides[0]*self.sides[1]
        
            
            
