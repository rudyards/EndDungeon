import random
import updater




class Monster:
    def __init__(self, name, type=None, health, regeneration = 0, room):
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
        self.level = 1
        self.regeneration = regeneration
        self.type = type

    def update(self):
        if player.room != self.room:
            if random.random() < .5:
                self.moveTo(self.room.randomNeighbor())
                if self.type == "Velociraptor":
                    self.moveTo(self.room.randomNeighbor())
                #Velociraptor moves 2 rooms each turn instead of 1
            #Monsters only move if the player is not in their room

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
      
        self.poison(player)
        if player.poisonTimeLeft > 0:
            print("The monster has poisoned you!")
        #If the monster can poison the player, they will do so on hit


        print("Your health is " + str(player.health) + ".")
        if (player.health <= 0):
            print("You are dead.")
            player.alive = False


    def poison(self,player):
        if self.type == "Spider":
            #The poison damage of the spider increases by 1/2 of the spiders level
            player.poisonRegenLoss = 1 + self.level//2
            player.poisonTimeLeft = 4
        # elif self.type == devil:
        #     self.poisonRegenLoss = 1
        #     self.poisonTimeLeft = 3

    def levelUp(self):
        #If levelUp is called, the monster's level (and xp bounty) increases, as does its health and base damage
        self.level += 1
        self.health += 5
        self.damage += 1




#Balance notes:
#Players deal 5.5 damage + half their strength + bonus weapons
#Players have 50 HP + 4* their constitution
#Players don't default to having any defense

class Troll(Monster):
    self.type = "Troll"
    self.health = 20
    self.regeneration = 2
    self.damage = 3
    self.damageRange = 3
    self.level = 2
    #Trolls deal 4-6 damage each hit, dealing aproximately 5 damage
    #Trolls are unique because they regenerate each turn, heavily punishing low damage players


class GiantRat(Monster):
    self.type = "Rat"
    self.health = 15
    self.damage = 0
    self.damageRange = 4
    self.level = 1
    #Rats deal 1-4 damage each hit, dealing 2.5 damage each hit
    #Rats are unique because they're cute


class Spider(Monster):
    self.type = "Spider"
    self.health = 10
    self.damage = 0
    self.damageRange = 4
    self.level = 1
    #Spider deal 1-4 damage each hit, dealing 2.5 damage each hit (+1 damage from poison, +3 after they die(poison lasts))
    #Spiders are unique because they poison the player

class Velociraptor(Monster):
    self.type = "Velociraptor"
    self.health = 13
    self.damage = 4
    self.damageRange = 6
    self.defense = 1
    self.level = 2
    #Velociraptors deal 5-10 damage a hit, dealing an average of 5 damage a hit
    #Velociraptors are unique because they move 2 rooms per movement