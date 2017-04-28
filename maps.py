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

#24 room names for random use

def roomnameChoice(array):
    choice = random.choice(array)
    array.remove(choice)
    return choice

roomNames = ["Creepy Room", "Decrepit Room", "Stygian Room","Old Armory","Long Forgotten Room","Unremembered Room","Monster Den","Cramped Space",
                "Unstable Room","Dusty Room","Clamy Room","Unpleasant Room","Disturbing Room","Rotting Room","Liminal Space","Former Hideout",
                "Ancient Room","Mystifying Room","Irrelevant Room","Unremarkable Room","Pointless Room","Strange Room","Unsettling Room","Virulent Room"]
