# Code Listing #5

"""

Borg - Pattern which allows class instances to share state without the strict requirement
of Singletons

"""

class Borg(object):
    """ I ain't a Singleton """
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


class IBorg(Borg):
    """ I am a Borg """
    
    def __init__(self):
        Borg.__init__(self)
        self.state = 'init'

    def __str__(self):
        return self.state

class ABorg(Borg): pass
class BBorg(Borg): pass

class A1Borg(ABorg): pass

if __name__ == "__main__":
    a = ABorg()
    a1 = A1Borg()
    b = BBorg()

    a.x = 100
    print('a.x =>',a.x)
    print('a1.x =>',a1.x)
    print('b.x =>',b.x)     

    
