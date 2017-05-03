# Code Listing #8

"""

Builder design pattern implemented as a house builder class example with
a few sub-classes demonstrating the power of the builder pattern.

"""

class Room(object):
    """ A class representing a Room in a house """
    
    def __init__(self, nwindows=2, direction='S'):
        self.nwindows = nwindows
        self.direction = direction

    def __str__(self):
        return "Room <facing:%s, windows=#%d>" % (self.direction,
                                                  self.nwindows)
class Porch(object):
    """ A class representing a Porch in a house """
    
    def __init__(self, ndoors=2, direction='W'):
        self.ndoors = ndoors
        self.direction = direction

    def __str__(self):
        return "Porch <facing:%s, doors=#%d>" % (self.direction,
                                                 self.ndoors)   
    
class LegoHouse(object):
    """ A lego house class """

    def __init__(self, nrooms=0, nwindows=0,nporches=0):
        # windows per room
        self.nwindows = nwindows
        self.nporches = nporches
        self.nrooms = nrooms
        self.rooms = []
        self.porches = []

    def __str__(self):
        msg="LegoHouse<rooms=#%d, porches=#%d>\n" % (self.nrooms,
                                                     self.nporches)

        for i in self.rooms:
            msg += str(i) + '\n'

        for i in self.porches:
            msg += str(i) + '\n'

        return msg

    def add_room(self,room):
        """ Add a room to the house """
        
        self.rooms.append(room)

    def add_porch(self,porch):
        """ Add a porch to the house """
        
        self.porches.append(porch)
    
class LegoHouseBuilder(object):
    """ Lego house builder class """

    def __init__(self, *args, **kwargs):
        self.house = LegoHouse(*args, **kwargs)
        
    def build(self):
        """ Build a lego house instance and return it """
        
        self.build_rooms()
        self.build_porches()
        return self.house
    
    def build_rooms(self):
        """ Method to build rooms """
        
        for i in range(self.house.nrooms):
            room = Room(self.house.nwindows)
            self.house.add_room(room)

    def build_porches(self):
        """ Method to build porches """     

        for i in range(self.house.nporches):
            porch = Porch(1)
            self.house.add_porch(porch)


    
class BudgetLegoHouseBuilder(LegoHouseBuilder):
    """ Builder building budget lego house with 1 room and no porch and rooms having 1 window """

    def __init__(self):
        self.house = LegoHouse(nrooms=1, nporches=0, nwindows=1)

class SmallLegoHouseBuilder(LegoHouseBuilder):
    """ Builder building small lego house with 1 room and 1 porch and rooms having 2 windows """

    def __init__(self):
        self.house = LegoHouse(nrooms=2, nporches=1, nwindows=2)        


class NorthFacingHouseBuilder(LegoHouseBuilder):
    """ Builder building all rooms and porches facing North """

    def build_rooms(self):

        for i in range(self.house.nrooms):
            room = Room(self.house.nwindows, direction='N')
            self.house.add_room(room)

    def build_porches(self):

        for i in range(self.house.nporches):
            porch = Porch(1, direction='N')
            self.house.add_porch(porch)

class NorthFacingSmallHouseBuilder(NorthFacingHouseBuilder, SmallLegoHouseBuilder):
    pass

if __name__ == "__main__":
    bbuilder = BudgetLegoHouseBuilder()
    print(bbuilder.build())

    sbuilder = SmallLegoHouseBuilder()
    print(sbuilder.build())

    nbuilder = NorthFacingHouseBuilder(nrooms=2, nporches=1, nwindows=1)
    print(nbuilder.build())
    
    print(NorthFacingSmallHouseBuilder().build())
