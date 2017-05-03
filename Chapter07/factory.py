# Code Listing #6

"""

Implementation of the Factory/Factory Method Design Pattern

"""

from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    """ An Employee class """

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_role(self):
        pass
    
    def __str__(self):
        return "{} - {}, {} years old {}".format(self.__class__.__name__,
                                                 self.name,
                                                 self.age,
                                                 self.gender)

class Engineer(Employee):
    """ An Engineer Employee """
    
    def get_role(self):
        return "engineering"

class Accountant(Employee):
    """ An Accountant Employee """
    
    def get_role(self):
        return "accountant"    

class Admin(Employee):
    """ An Admin Employee """

    def get_role(self):
        return "administration"

class EmployeeFactory(object):
    """ An Employee factory class """

    @classmethod
    def create(cls, name, *args):
        """ Factory method for creating an Employee instance """

        name = name.lower().strip()
        
        if name == 'engineer':
            return Engineer(*args)
        elif name == 'software engineer':
            return SoftwareEngineer(*args)
        elif name == 'admin':
            return Admin(*args)
