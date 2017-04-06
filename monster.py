import random
import updater

class Monster:
    def __init__(self, name, health, room,xp):
        self.name = name
        self.health = health
        self.room = room
        room.addMonster(self)
        updater.register(self)
        self.damage = 0
        self.defense = 0
        self.xpBounty = xp

    def update(self):
        if random.random() < .5:
            self.moveTo(self.room.randomNeighbor())

    def moveTo(self, room):
        self.room.removeMonster(self)
        self.room = room
        room.addMonster(self)

    def die(self):
        self.room.removeMonster(self)
        updater.deregister(self)

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


