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
        if secondroll == 3:
            keyword = "a permeating sense of unease"
        description = "This room is filled with "+keyword


    elif roll == 2:
        
        if secondroll == 1:
            keyword = "slept in, judging by the dust covered cots"
        if secondroll == 2:
            keyword = "used as storage, but it has since been looted"
        if secondroll == 3:
            keyword = "the site of a gory battle, and faint blood stains remain"
        description = "This room was once "+keyword


    elif roll == 3:
        
        if secondroll == 1:
            keyword = "and the floor has a strange red mark on it"
        if secondroll == 2:
            keyword = "and there are concerning scratchmarks on the ceiling"
        if secondroll == 3:
            keyword = "and is that a pair of eyes peering out at you?"
        description = "Thick cobwebs clutter the corners of the room "+keyword

    else:
        
        if secondroll == 1:
            keyword = "ancient things and mildew"
        if secondroll == 2:
            keyword = "the unmistakable iron scent of blood"
        if secondroll == 3:
            keyword = "fear"
        description = "The room smells of "+keyword

    return description



