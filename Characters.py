import random
from item import *

currentCharacters = []

class Character:
    #characterCounter = 0
    def __init__(self,name):
        #self.type = name + str(charcterCounter)
        #Character.characterCounter += 1
        self.name = name
        self.items = []
        self.location = None
        currentCharacters.append(self)

    def putInRoom(self, room):
        self.loc = room
        room.addCharacter(self)

    def getItemFromInventory(self,item):
        for thing in self.items:
            if thing.name.lower() == item.lower():
                return thing
        return False

class Merchant(Character):
    def __init__(self,name,items=[]):
        Character.__init__(self,name)
        self.tagLine = "Good day. I am a Merchant. You can buy items from my selection of wares or sell me your own."
        merchantListNumber = random.randint(1,3)
        if merchantListNumber == 1:
            for item in merchantList1:
                thing = makeItem(item)
                self.items.append(thing)
        elif merchantListNumber == 2:
            for item in merchantList2:
                thing = makeItem(item)
                self.items.append(thing)
        else:
            for item in merchantList3:
                thing = makeItem(item)
                self.items.append(thing)

class Blacksmith(Character):
    def __init__(self,name,items=[]):
        Character.__init__(self,name)
        self.tagLine = "Good day. I am a Blacksmith. You can buy items from my selection of wares or sell me your own."
        blacksmithListNumber = random.randint(1,3)
        if blacksmithListNumber == 1:
            for item in blacksmithList1:
                thing = makeItem(item)
                self.items.append(thing)
        elif blacksmithListNumber == 2:
            for item in blacksmithList2:
                thing = makeItem(item)
                self.items.append(thing)
        else:
            for item in blacksmithList3:
                thing = makeItem(item)
                self.items.append(thing)
