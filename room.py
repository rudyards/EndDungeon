import updater
import random
from monster import *
from player import *

currentRooms = []
coreRooms = []
roomConnections = []

class RoomCounter:
    def __init__(self,value):
        self.value = value

    def increment(self):
        self.value += 1

    def getValue(self):
        return self.value

class Room:
    def __init__(self, description, x, y):
        self.desc = description
        self.monsters = []
        self.exits = []
        self.items = []
        self.characters = []
        updater.register(self)
        self.x = x
        self.y = y
        currentRooms.append(self)

    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])

    def update(self):
        # if player.location != self:
        monsterAddChance = random.randint(1,21)
        if monsterAddChance == 7:
            monsterChoice = random.randint(1,5)
            if monsterChoice == 1:
                newSpider = Spider("Spidey",self)
            elif monsterChoice == 2:
                newTroll = Troll("Trolley",self)
            elif monsterChoice == 3:
                newGiantRat = GiantRat("Nippy",self)
            elif monsterChoice == 4:
                newVelociraptor = Velociraptor("Rapty",self)
            print("Somewhere in the dungeon, a new monster appears")

    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]

    def connectRooms(room1, dir1, room2, dir2):
        connection = []
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)
        connection.append(room1)
        connection.append(dir1)
        connection.append(room2)
        connection.append(dir2)


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
        connection.append(room1)
        connection.append(dir1)
        connection.append(room2)
        connection.append(dir2)
        roomConnections.append(connection)



    def exitNames(self):
        return [x[0] for x in self.exits]


    def randomNeighbor(self):
        return random.choice(self.exits)[1]
        

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
    def randomNeighbor(self):
        return random.choice(self.exits)[1]

                
