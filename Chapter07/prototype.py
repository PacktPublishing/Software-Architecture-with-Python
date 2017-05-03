# Code Listing #7

"""

Protype design pattern and related classes

"""


import copy
from abc import ABCMeta
from borg import Borg

class MetaPrototype(type):
    """ A metaclass for Prototypes """

    def __init__(cls, *args):
        type.__init__(cls, *args)
        cls.clone = lambda self: copy.deepcopy(self)            

class MetaSingletonPrototype(type):
    """ A metaclass for Singleton & Prototype patterns """
    
    def __init__(cls, *args):
        print(cls,"__init__ method called with args", args)
        type.__init__(cls, *args)
        cls.instance = None
        cls.clone = lambda self: copy.deepcopy(cls.instance)

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls,"creating prototypical instance", args, kwargs)
            cls.instance = type.__call__(cls,*args, **kwargs)
        return cls.instance
    
class PrototypeM(metaclass=MetaSingletonPrototype):
    """ Top-level prototype class using MetaSingletonPrototype """
    pass

class ItemCollection(PrototypeM):
    """ An item collection class """

    def __init__(self, items=[]):
        self.items = items

class Prototype(object):
    """ A prototype base class """

    def clone(self):
        """ Return a clone of self """
        return copy.deepcopy(self)

class Register(Prototype):
    """ A student Register class  """
    
    def __init__(self, names=[]):
        self.names = names
        
class SPrototype(object):
    """ A prototype base class using shallow copy """

    def clone(self):
        """ Return a clone of self """
        return copy.copy(self)
    

class SRegister(SPrototype):
    """ Sub-class of SPrototype """
    
    def __init__(self, stuff=(), names=[]):
        self.stuff = stuff
        self.names = names

class Name(SPrototype):
    """ A class representing a person's name """
    
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __str__(self):
        return ' '.join((self.first, self.second))
                             

class Animal(SPrototype):
    """ A class representing an animal """

    def __init__(self, name, type='Wild'):
        self.name = name
        self.type = type

    def __str__(self):
        return ' '.join((str(self.type), self.name))

class Address(SPrototype):
    """ An address class """

    def __init__(self, building, street, city, zip, country):
        self.building = building
        self.street = street
        self. city = city
        self.zip = zip
        self.country = country

    def __str__(self):
        return ', '.join((map(str, (self.building, self.street, self.city, self.zip, self.country))))
        
class PrototypeFactory(Borg):
    """ A Prototype factory/registry class """
    
    def __init__(self):
        """ Initializer """

        self._registry = {}

    def register(self, instance):
        """ Register a given instance """

        self._registry[instance.__class__] = instance

    def clone(self, klass):
        """ Return cloned instance of given class """

        instance = self._registry.get(klass)
        if instance == None:
            print('Error:',klass,'not registered')
        else:
            return instance.clone()

if __name__ == "__main__":
    r1 = Register(names=['amy','stu','jack'])
    r2 = r1.clone()
    print(r1)
    print(r2)
    print(r1==r2)

    r1 = SRegister(names=['amy','stu','jack'])
    r2 = r1.clone()

    r1.names.append('bob')
    print('r1.names==r2.names',r1.names==r2.names)
    print('r1.names is r2.names',r1.names is r2.names)  
            
    
    i1 = ItemCollection(items=['apples','grapes','oranges'])
    print(i1)
    # Invokes the Prototype API
    i2 = i1.clone()
    print('i1.items is i2.items',i1.items is i2.items)
    # Invokes the Singleton API
    i3 = ItemCollection(items=['apples','grapes','oranges'])
    print('i1 is i3',i1 is i3)

    # Illustrating factory
    name = Name('Bill', 'Bryson')
    animal = Animal('Elephant')
    factory = PrototypeFactory()

    factory.register(animal)
    factory.register(name)

    # Clone them

    name2 = factory.clone(Name)
    animal2 = factory.clone(Animal)

    print(name, name2)
    print(animal, animal2)

    print('name is not name2',name is not name2)
    print('animal is not animal2',animal is not animal2)    

    class C: pass

    factory.clone(C)
