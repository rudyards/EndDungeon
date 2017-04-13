import random
import updater




class Monster:
    def __init__(self, name, type=None, health, regeneration = 0, room, level):
        self.name = name
        self.health = health
        self.maxHealth = health
        self.room = room
        room.addMonster(self)
        updater.register(self)

        self.damage = 0
        #The bonus damage a monster has
        
        self.damageRange = 10
        #The damage dice a monster uses

        self.defense = 0
        self.level = level
        self.regeneration = regeneration
        self.type = type

    def update(self):
        if random.random() < .5:
            self.moveTo(self.room.randomNeighbor())

        if self.health < self.maxHealth:
            if self.health + self.regeneration < self.maxHealth:
                self.health += self.regeneration
            elif self.health < self.maxHealth:
                self.health = self.maxHealth

    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)

    def die(self,player):
        self.room.removeMonster(self)
        updater.deregister(self)
        player.xp += mon.level * 50
        #Currently, monsters give 50 xp per level, regardless of what level that player is

    def attackPlayer(self,player):
        attackDamage = random.randint(1,self.damageRange) + self.damage
        print("The monster attacks you for "+str(attackDamage)+" damage.")
        print("Your defense reduces that damage by "+str(player.defense))
        attackDamage -= player.defense
        if(attackDamage < 0):
            attackDamage = 0
        player.health-=attackDamage

        print("Your health is " + str(player.health) + ".")
        if (player.health <= 0):
            print("You are dead.")
            player.alive = False


    def poison(self,player):
        self.poisoned = True
        if self.type == spider:
            self.poisonRegenLoss = 2
            self.poisonTimeLeft = 5
        elif self.type == devil:
            self.poisonRegenLoss = 1
            self.poisonTimeLeft = 3




#Balance notes:
#Players deal 5.5 damage + half their strength + bonus weapons
#Players have 50 HP + 4* their constitution
#Players don't default to having any defense

class Troll(Monster):
    self.type = "troll"
    self.health = 15
    self.regeneration = 2
    self.damage = 3
    self.damageRange = 3
    #Trolls deal 3-6 damage each hit, dealing aproximately 4.5 damage

