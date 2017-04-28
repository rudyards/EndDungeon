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
        if secondroll == 4:
            keyword = "the souls of long-lost adventurers"
        if secondroll == 5:
            keyword = "ominous pools of ink (or is it ink?)"
        description = "This room is filled with "+keyword


    elif roll == 2:
        
        if secondroll == 1:
            keyword = "slept in, judging by the dust covered cots"
        if secondroll == 2:
            keyword = "used as storage, but it has since been looted"
        if secondroll == 3:
            keyword = "the site of a gory battle, and faint blood stains remain"
        if secondroll == 4:
            keyword = "well-furnished, and a dilapidated armchair remains"
        if secondroll == 5:
            keyword = "once once used for torturing prisoners"
        description = "This room was once "+keyword


    elif roll == 3:
        
        if secondroll == 1:
            keyword = "and the floor has a strange red mark on it"
        if secondroll == 2:
            keyword = "and there are concerning scratchmarks on the ceiling"
        if secondroll == 3:
            keyword = "and is that a pair of eyes peering out at you?"
        if secondroll == 4:
            keyword = "and there are mysterious symbols on the walls"
        if secondroll == 5:
            keyword = "and scorched skulls litter the floor"
        description = "Thick cobwebs clutter the corners of the room "+keyword

    else:
        
        if secondroll == 1:
            keyword = "of ancient things and mildew"
        if secondroll == 2:
            keyword = "of the unmistakable iron scent of blood"
        if secondroll == 3:
            keyword = "fear"
        if secondroll == 4:
            keyword = "faintly of murder"
        if seconroll == 5:
            keyword = "inexplicably of cinnamon"
        description = "The room smells "+keyword

    return description

#24 room names for random use

def roomnameChoice(array):
    choice = random.choice(array)
    array.remove(choice)
    return choice

roomNames = ["Creepy Room", "Decrepit Room", "Stygian Room","Old Armory","Long Forgotten Room","Unremembered Room","Monster Den","Cramped Space",
                "Unstable Room","Dusty Room","Clamy Room","Unpleasant Room","Disturbing Room","Rotting Room","Liminal Space","Former Hideout",
                "Ancient Room","Mystifying Room","Irrelevant Room","Unremarkable Room","Pointless Room","Strange Room","Unsettling Room","Virulent Room"]
