import updater
import random
from monster import *
from player import *
from item import *

#list of current Rooms (for pickling)
currentRooms = []
#list of rooms in base map
coreRooms = []

#Rooms!
class Room:
    def __init__(self, name, description, x, y):
        self.name = name
        self.desc = description
        self.monsters = []
        self.exits = []
        self.items = []
        self.characters = []
        updater.register(self)
        self.x = x
        self.y = y
        currentRooms.append(self)
        if self.name == "Old Armory":
            brokenSword.putInRoom(self)

    #Adds an exit to a room
    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])

    #returns room in a direction from current room
    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]

    #connects two rooms together
    def connectRooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)

    #An improved version of connecting rooms that utilizes the grid system we're using
    def simpleConnectRooms(room1,room2):
        connection = []
        if(room1.x == room2.x):
            if(room1.y -1 == room2.y):
                dir1 = "north"
                dir2 = "south"
            elif(room1.y +1 == room2.y):
                dir1 = "south"
                dir2 = "north"
            else:
                print("Rooms not adjacent")
                return None
        elif(room1.y == room2.y):
            if(room1.x -1 == room2.x):
                dir1 = "west"
                dir2 = "east"
            elif(room1.x +1 == room2.x):
                dir1 = "east"
                dir2 = "west"
            else:
                print("Rooms not adjacent")
                return None
        else:
            print("Rooms not adjacent")
            return None
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)

    #randomly adds various monsters to the dungeon 
    def update(self):
        # if player.location != self:
        monsterAddChance = random.randint(1,21)
        if self.name == "Monster Den":
            monsterAddChance = random.randint(1,10)
        if monsterAddChance == 7:
            monsterChoice = random.randint(1,5)
            if monsterChoice == 1:
                newSpider = Spider(random.choice(spiderNames),self)
            elif monsterChoice == 2:
                newTroll = Troll(random.choice(trollNames),self)
            elif monsterChoice == 3:
                newGiantRat = GiantRat(random.choice(ratNames),self)
            elif monsterChoice == 4:
                newVelociraptor = Velociraptor(random.choice(raptorNames),self)

        eventAddChance = random.randint(1,80)
        #This is broken, the player.location ends up None....not great
        # if eventAddChance == 6:
        #     room1 = random.choice(currentRooms)
        #     room2 = random.choice(currentRooms)
        #     Room.connectRooms(room1,"cobwebby tunnel", room2, "cobwebby tunnel")
        #     print("A secret passageway appears somewhere in the dungeon")

        #This is currently broken since the rooms don't know anything about the player
        # elif eventAddChance == 19:
        #     player.health -= 5
        #     print("You are attacked by a swarm of radioactive bees; you lose 5 health")
        # elif eventAddChance == 24:
        #     player.health += 6
        #     print("a healing mist descends; you gain 6 health")


        #elif eventAddChance = 27:
        #33

    #returns names of exits
    def exitNames(self):
        return [x[0] for x in self.exits]

    #returns a random neighboring room
    def randomNeighbor(self):
        return random.choice(self.exits)[1]
        
    #These ones are all really self-explanatory :)
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def addCharacter(self,character):
        self.characters.append(character)
    def removeCharacter(self,character):
        self.characters.remove(character)
    def addMonster(self, monster):
        self.monsters.append(monster)
    def removeMonster(self, monster):
        self.monsters.remove(monster)
    def hasItems(self):
        return self.items != []
    def getItemByName(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasCharacters(self):
        return self.characters != []
    def getCharacterByName(self, name):
        for i in self.characters:
            if i.name.lower() == name.lower():
                return i
        return False
    def hasMonsters(self):
        return self.monsters != []
    def getMonsterByName(self, name):
        for i in self.monsters:
            if i.name.lower() == name.lower():
                return i
        return False

                
