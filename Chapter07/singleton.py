# Code Listing #4

"""

All code listings for Singleton pattern shown in the book

"""

class MetaSingleton(type):
    """ A type for Singleton classes (overrides __call__) """    

    def __init__(cls, *args):
        print(cls,"__init__ method called with args", args)
        type.__init__(cls, *args)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.instance:
            print(cls,"creating instance", args, kwargs)
            cls.instance = type.__call__(cls, *args, **kwargs)
        return cls.instance
    
class Singleton(object):
    """ Singleton in Python """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance == None:
            cls._instance = object.__new__(cls)
        return cls._instance

class SingletonA(Singleton):
    pass

class SingletonA1(SingletonA):
    pass

class SingletonB(Singleton):
    pass

class SingletonM(metaclass=MetaSingleton):
    pass


def test_single(cls):
    """ Test if passed class is a singleton """
    return cls() == cls()

if __name__ == "__main__":
    # Check for state sharing across hierarchies
    
    a = SingletonA()
    a1 = SingletonA1()
    b = SingletonB()

    a.x = 100
    print('a.x =>',a.x)
    print('a1.x =>',a1.x)
    # Will raise an exception
    try:
        print('b.x =>',b.x)
    except AttributeError as e:
        print('Error:',e)

    print(test_single(Singleton))
    print(test_single(SingletonM))
    print(test_single(SingletonA))
    print(test_single(SingletonB))
    print(test_single(SingletonA1))


