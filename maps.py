import random
from room import *
from player import *
from item import *
from monster import *
from maps import *
from Characters import *


def roomdescriber():
    description = ""
    keyword = ""
    roll=random.randint(1,4)
    secondroll = random.randint(1,2)
    if roll == 1:
        
        if secondroll == 1:
            keyword = "a thin mist that covers the ground"
        if secondroll == 2:
            keyword = "an unshakeable feeling of dread"
        description = "This room is filled with "+keyword


    elif roll == 2:
        
        if secondroll == 1:
            keyword = "was slept in, judging by the dust covered cots"
        if secondroll == 2:
            keyword = "was used as storage, but it has since been looted"
        description = "This room once "+keyword


    elif roll == 3:
        
        if secondroll == 1:
            keyword = "and the floor has a strange red mark on it"
        if secondroll == 2:
            keyword = "and there are concerning scratchmarks on the ceiling"
        description = "Thick cobwebs clutter the corners of the room "+keyword

    else:
        
        if secondroll == 1:
            keyword = "ancient things and mildew"
        if secondroll == 2:
            keyword = "the unmistakable iron scent of blood"
        description = "The room smells of "+keyword

    return description


def generateBaseMap():
    startingRoom = Room("The entrance to the great dungeon",2,6)
    secondRoom = Room(roomdescriber(),2,5)
    Room.connectRooms(startingRoom, "north", secondRoom, "south")
    thirdRoom = Room(roomdescriber(),2,4)
    Room.connectRooms(secondRoom, "north", thirdRoom, "south")
    fourthRoom = Room(roomdescriber(),2,3)
    Room.connectRooms(thirdRoom, "north", fourthRoom, "south")
    fifthRoom = Room(roomdescriber(),3,3)
    Room.connectRooms(fourthRoom, "west", fifthRoom, "east")
    sixthRoom = Room(roomdescriber(),4,3)
    Room.connectRooms(fifthRoom, "west", sixthRoom, "east")
    seventhRoom = Room(roomdescriber(),5,3)
    Room.connectRooms(sixthRoom, "west", seventhRoom, "east")
    eigthRoom = Room(roomdescriber(),5,4)
    Room.connectRooms(seventhRoom, "south", eigthRoom, "north")
    ninthRoom = Room(roomdescriber(),6,4)
    Room.connectRooms(eigthRoom, "west", ninthRoom, "east")
    tenthRoom = Room(roomdescriber(),7,4)
    Room.connectRooms(ninthRoom, "west", tenthRoom, "east")


    player.location = startingRoom
    merchant1 = Merchant("merchant1")
    merchant1.putInRoom(startingRoom)
    longsword.putInRoom(startingRoom)
    hideArmor.putInRoom(startingRoom)
    monster1 = Troll("bob",secondRoom)
    monster2 = Troll("ted",secondRoom)
    monster3 = Troll("cindy",secondRoom)
