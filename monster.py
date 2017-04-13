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
        attackDamage = random.randint(1,10) + self.damage
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


