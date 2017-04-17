import updater
import random

class Room:
    def __init__(self, description, x, y):
        self.desc = description
        self.monsters = []
        self.exits = []
        self.items = []
        self.characters = []
        #updater.register(self)
        self.x = x
        self.y = y

    def addExit(self, exitName, destination):
        self.exits.append([exitName, destination])

    def getDestination(self, direction):
        for e in self.exits:
            if e[0] == direction:
                return e[1]

    def connectRooms(room1, dir1, room2, dir2):
        #creates "dir1" exit from room1 to room2 and vice versa
        room1.addExit(dir1, room2)
        room2.addExit(dir2, room1)

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

    def update(self):
        if player.location != self:
            monsterAddChance = random.randint(1,100)
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
                    
