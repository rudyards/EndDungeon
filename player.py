import os
import item
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Player:
    def __init__(self):
        self.location = None

        #Stats
        self.strength = random.randint(-1,1) #Each 2 points in str gives you +1 damage
        self.dexterity = random.randint(-1,1) #Each 2 points in dex gives you +1 defense
        self.constitution = random.randint(-1,1) #Each point in con gives you +4 HP
        self.wisdom = random.randint(-1,1) #Wisdom gives you bonuses to resist mind control
        self.intelligence = random.randint(-1,1) #Intelligence gives you bonuses for magic
        self.charisma = random.randint(-1,1) #Charisma gives you bonuses in selling and buying


        #Equipment/inventory management
        self.hasWeapon = False
        self.hasArmor = False
        self.items = []
        self.equipped = []
        self.carryingCapacity = 6+self.strength

        #Vitality stuff
        self.maxhealth = 50 + 4*self.constitution
        self.health = maxhealth
        self.alive = True
        self.regen = self.constitution//5

        #Combat stuff
        self.damage = 0 + self.strength//2
        self.bonusDamage = 0
        self.defense = 0 + self.dexterity//2
        self.poisonRegenLoss = 0
        self.poisonTimeLeft = 0
        #Character Advancement things
        self.xp = 0
        self.gp = 100
        self.level = 1
   

    def update(self):
        if (self.health < self.maxhealth):
            #Notable problem: poison only does things if you are at less than max health
            if self.poisonTimeLeft > 0:
                self.health += (self.regen-self.poisonRegenLoss)
                self.poisonTimeLeft -= 1
                print("You are poisoned! You lose "+int(self.poisonRegenLoss)+" health.")
            else:
                self.health += self.regen
        self.checkXP()



    def showStats(self):
        clear()
        print("Your stats are")
        print("Strength: "+str(self.strength))
        print("Dexterity: "+str(self.dexterity))
        print("Constitution: "+str(self.constitution))
        print("Wisdom: "+str(self.wisdom))
        print("Intelligence: "+str(self.intelligence))
        print("Charisma: "+str(self.charisma))
        print("")
        print("You have "+str(self.xp)+" xp and "+str(self.gp)+" gold")
        print("You can carry a maximum of "+str(self.carryingCapacity)+" items")
        input("Press enter to continue...")

    def goDirection(self, direction):
        self.location = self.location.getDestination(direction)

    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.location.removeItem(item)

    def equip(self,item):
        #Weapons increase your bonus damage. You can only have 1 weapon equipped at once
        if item.type == "weapon":
            if (self.hasWeapon == False):
                self.bonusDamage += item.damage
                self.equipped.append(item)
                self.items.remove(item)
            else:
                print("You already have a weapon equipped")
        #Armor increases your defense. You can only have 1 piece of armor at once
        if item.type == "armor":
            if (self.hasArmor == False):
                self.armor += item.armor
                self.equipped.append(item)
                self.items.remove(item)
            else:
                print("You already have a weapon equipped")

    def drop(self, item):
        self.items.remove(item)
        item.loc = self.location
        self.location.addItem(item)

    def unequip(self,item):
        if item.type == "weapon":
            self.bonusDamage -= item.damage
            self.equipped.remove(item)
            self.items.append(item)
        if item.type == "armor":
            self.armor -= item.armor
            self.equipped.remove(item)
            self.items.append(item)

    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        for i in self.items:
            print(i.name)
        print()

    def showEquipped(self):
        print("Currently you have equipped:")
        print()
        for i in self.equipped:
            print(i.name)
        print()
        input("Press enter to continue...")

    def isInInventory(self, name):
        for i in self.items:
            if i.name.lower() == name.lower():
                return i
        return False

    def isEquipped(self, name):
        for i in self.equipped:
            if i.name.lower() == name.lower():
                return i
        return False

    def checkXP(self):
        if self.xp >= self.level*200:
            self.level +=1
            print("You leveled up!")
            self.strength+=random.randint(0,1)
            self.dexterity+=random.randint(0,1)
            self.constitution+=random.randint(0,1)
            self.wisdom+=random.randint(0,1)
            self.intelligence+=random.randint(0,1)
            self.charisma+=random.randint(0,1)
            print("Your stats have randomly increased.")


            self.carryingCapacity = 6+self.strength
            self.damage = 0 + self.strength//2
            self.defense = 0 + self.dexterity//2
            self.maxhealth = 50 + 4*self.constitution




    def attackMonster(self, mon):
        clear()
        print("You are attacking " + mon.name)
        print()
        print("Your health is " + str(self.health) + ".")
        print(mon.name + "'s health is " + str(mon.health) + ".")
        print()

        
        attackDamage = random.randint(1,10) + self.damage + self.bonusDamage
        print("You attack the monster for "+str(attackDamage)+" damage.")
        print("Their defense reduces that damage by "+str(mon.defense))
        attackDamage -= mon.defense
        if(attackDamage < 0):
            attackDamage = 0
        mon.health -= attackDamage
        print(mon.name + "'s health is " + str(mon.health) + ".")
        if(mon.regeneration > 0):
            print("The monster is regenerating!")

        if(mon.health <= 0):
            mon.die(self)
        else:
            mon.attackPlayer(self)

        #Old way of doing combat, which isn't the way we want to
        # if self.health > mon.health:
        #     self.health -= mon.health
        #     print("You win. Your health is now " + str(self.health) + ".")
        #     mon.die()
        # else:
        #     print("You lose.")
        #     self.alive = False
        print()
        input("Press enter to continue...")

