import random
import updater
from player import *
from item import *

currentMonsters = []

class Monster:
    #monsterCounter = 0
    def __init__(self, name, health, room, regeneration=0):
        self.name = name #+ 
        #str(monsterCounter)
        #Monster.monsterCounter += 1
        self.health = health
        self.maxHealth = health
        self.room = room
        self.damaged = False
        currentMonsters.append(self)
        #This is a variable that tracks if the monster was damaged last turn
        room.addMonster(self)
        updater.register(self)

        self.damage = 0
        #The bonus damage a monster has
        
        self.damageRange = 10
        #The damage dice a monster uses

        self.defense = 0
        self.level = 1
        self.regeneration = regeneration
        #self.monsterType = monsterType



    def update(self):
        # if self.room != player.location:
        if random.random() < .5 and self.damaged == False:
            self.moveTo(self.room.randomNeighbor())
            if self.monsterType == "Velociraptor":
                self.moveTo(self.room.randomNeighbor())
                #Velociraptor moves 2 rooms each turn instead of 1
            #Monsters only move if the player is not in their room

        if self.health < self.maxHealth:
            if self.health + self.regeneration < self.maxHealth:
                self.health += self.regeneration
            elif self.health < self.maxHealth:
                self.health = self.maxHealth
            #If a monster has taken damage, they will regenerate (if they have regeneration)
            #Monsters can't go over their maximum health, obviously
        self.damaged = False

    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)

    def die(self,player):
        self.room.removeMonster(self)
        currentMonsters.remove(self)
        updater.deregister(self)

        goldGain = random.randint(1,self.level+3)*15
        player.xp += int((self.level * 50) * (1 + .1*player.intelligence))
        #Monsters give 50 xp per level they are, and 15*(1 to 3+their level) gp
        #Players get 10% more XP per point of int they have


        player.gp += goldGain
        print("You killed "+self.name+". You gain "+str(self.level*50)+" xp and "+str(goldGain)+" gp.")
        player.checkXP()
        print("You are now "+str((player.level*200)-player.xp)+" xp from leveling up")

        #Monsters have a 1/3 chance of dropping a random item
        if random.randint(1,3) == 2:
            monsterLoot = random.choice(totalItemList)
            print("The monster drops a "+str(monsterLoot))
            monsterLoot = makeItem(monsterLoot)
            self.room.addItem(monsterLoot)


    def attackPlayer(self,player):
        attackDamage = random.randint(1,self.damageRange) + self.damage
        print(str(self.name)+" attacks you for "+str(attackDamage)+" damage.")
        print("Your defense reduces that damage by "+str(player.defense))
        attackDamage -= player.defense
        if(attackDamage < 0):
            attackDamage = 0
        player.health-=attackDamage
        self.poison(player)
        if player.poisonTimeLeft > 0:
            print("The monster has poisoned you!")
        #If the monster can poison the player, they will do so on hit


        print("Your health is " + str(player.health) + ".")
        if (player.health <= 0):
            print("You are dead.")
            player.alive = False


    def poison(self,player):
        return None
        #Monsters don't by default have any poison, but some subclasses do

    def levelUp(self):
        #If levelUp is called, the monster's level (and xp bounty) increases, as does its health and base damage
        self.level += 1
        self.health += 3
        self.damage += 1




#Balance notes:
#Players deal 5.5 damage + half their strength + bonus weapons
#Players have 50 HP + 4* their constitution
#Players don't default to having any defense

class Troll(Monster):
    def __init__(self, name, room):
        Monster.__init__(self, name, 20, room, 2)
        self.monsterType = "Troll"
        self.damage = 3
        self.damageRange = 3
        self.level = 2
    
    #Trolls deal 4-6 damage each hit, dealing aproximately 5 damage
    #Trolls are unique because they regenerate each turn, heavily punishing low damage players


class GiantRat(Monster):
    def __init__(self, name, room):
        Monster.__init__(self, name, 15, room, 0)
        self.monsterType = "Rat"
        self.damage = 0
        self.damageRange = 4
        self.level = 1

    #Rats deal 1-4 damage each hit, dealing 2.5 damage each hit
    #Rats are unique because they're cute


class Spider(Monster):
    def __init__(self, name, room):
        Monster.__init__(self, name, 10, room, 0)
        self.monsterType = "Spider"
        self.damage = 0
        self.damageRange = 4
        self.level = 1
    def poison(self,player):
        player.poisonRegenLoss = 1 + self.level//2
        player.poisonTimeLeft = 4
    #Spider deal 1-4 damage each hit, dealing 2.5 damage each hit (+1 damage from poison, +3 after they die(poison lasts))
    #Spiders are unique because they poison the player

class Velociraptor(Monster):
    def __init__(self, name, room):
        Monster.__init__(self, name, 13, room, 0)
        self.monsterType = "Velociraptor"
        self.damage = 4
        self.damageRange = 6
        self.defense = 1
        self.level = 2
    #Velociraptors deal 5-10 damage a hit, dealing an average of 5 damage a hit
    #Velociraptors are unique because they move 2 rooms per movement

class Dragon(Monster):
    def __init__(self,name, room):
        Monster__init__(self, name, 30, Endroom, 1)
        self.monsterType = "Dragon"
        self.damage = 6
        self.damageRange = 8
        self.defense = 4
        self.level = 5

    def die(self, player):
        self.room.removeMonster(self)
        currentMonsters.remove(monster)
        updater.deregister(self)
        player.xp += self.level * 50
        print("You killed "+self.name+". You gain "+str(self.level*50)+" xp.")
        print("Congratulations, "+player.name+", you won!!!")
        print("you made it to level "+str(player.level)+"and earned "+str(player.xp)+"xp.")
        print("Thanks for playing!")
        input("Press any key to continue...")
        playing = False


trollNames = ["Karkat", "Olaf", "Scrag", "Grendel", "Ulik","Geirrodur","Shrek","Trantor", "Shine","Tethys"]
ratNames = ["Vincent","Remy", "Templeton", "Ralph", "Stuart","Jerry","Splinter","Rizzo","Emile", "Nicodemus"]
spiderNames = ["Arachnea", "Nerub", "Brood", "Skitter", "Khepri", "Weaver", "Arachnus","Ishkanah"]
raptorNames = ["Lacey", "Blue", "Charlie", "Delta", "Echo", "Owen", "Scraw", "Turner", "Norell"]