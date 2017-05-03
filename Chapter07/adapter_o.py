# Code Listing #10

"""

Adapter design pattern - Object Adapter with an example of overriding __getattr__
for magic method routing.

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

class Triangle(object):
    """ Triangle class from Polygon using class adapter """

    def __init__(self, *sides):
        # Compose a polygon
        self.polygon = Polygon(*sides)

    def perimeter(self):
        return self.polygon.perimeter()
    
    def is_valid(f):
        """ Is the triangle valid """

        def inner(self, *args):
            # Sum of 2 sides should be > 3rd side
            perimeter = self.polygon.perimeter()
            sides = self.polygon.sides
            
            for side in sides:
                sum_two = perimeter - side
                if sum_two <= side:
                    raise InvalidPolygonError(str(self.__class__) + "is invalid!")

            result = f(self, *args)
            return result
        
        return inner

    @is_valid
    def is_equilateral(self):
        """ Is this equilateral triangle ? """
        
        return self.polygon.is_regular()

    @is_valid
    def is_isosceles(self):
        """ Is the triangle isoscles """
        
        # Check if any 2 sides are equal
        for a,b in itertools.combinations(self.polygon.sides, 2):
            if a == b:
                return True
        return False
    
    def area(self):
        """ Calculate area """
        
        # Using Heron's formula
        p = self.polygon.perimeter()/2.0
        total = p
        for side in self.polygon.sides:
            total *= abs(p-side)
            
        return pow(total, 0.5)
    

class Rectangle(object):
    """ Rectangle class from Polygon using object adapter """


    method_mapper = {'is_square': 'is_regular'}
    
    def __init__(self, *sides):
        # Compose a polygon
        self.polygon = Polygon(*sides)

    def is_valid(f):
        def inner(self, *args):
            """ Is the rectangle valid """

            sides = self.sides
            # Should have 4 sides
            if len(sides) != 4:
                return False

            # Opposite sides should be same
            for a,b in [(0,2),(1,3)]:
                if sides[a] != sides[b]:
                    return False

            result = f(self, *args)
            return result
        
        return inner

    def __getattr__(self, name):
        """ Overloaded __getattr__ to forward methods to wrapped instance """

        if name in self.method_mapper:
            # Wrapped name
            w_name = self.method_mapper[name]
            print('Forwarding to method',w_name)
            # Map the method to correct one on the instance
            return getattr(self.polygon, w_name)
        else:
            # Assume method is the same
            return getattr(self.polygon, name)
        
    @is_valid
    def area(self):
        """ Return area of rectangle """

        # Length x breadth
        sides = self.sides      
        return sides[0]*sides[1]
        
            
            
