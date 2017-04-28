import os
import item
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

currentPlayers = []

class Player:
    def __init__(self, name):
        self.location = None
        self.name = name
        currentPlayers.append(self)

        #Stats
        self.strength = random.randint(-1,1) #Each 2 points in str gives you +1 damage
        self.dexterity = random.randint(-1,1) #Each 2 points in dex gives you +1 defense
        self.constitution = random.randint(-1,1) #Each point in con gives you +4 HP
        self.wisdom = random.randint(-1,1) #Doesn't do anything, unfortunately
        self.intelligence = random.randint(-1,1) #Intelligence gives you 10% extra XP per point 
        self.charisma = random.randint(-1,1) #Doesn't do anything, unfortunately


        #Equipment/inventory management
        self.hasWeapon = False
        self.hasArmor = False
        self.items = []
        self.equipped = []
        self.carryingCapacity = 6+self.strength #Players can carry a max of 6 items that aren't equipped. This goes up with str

        #Vitality stuff
        self.maxhealth = 50 + 4*self.constitution
        self.health = self.maxhealth
        self.alive = True
        self.regen = self.constitution//5 #Regeneration is hard to acquire, but if you've leveled up a bit and gotten lucky, you should have some

        #Combat stuff
        self.damage = 0 + self.strength//2
        self.bonusDamage = 0 #Damage is seperated from bonus damage, since bonus damage is something that you get from equipment
        self.defense = 0 + self.dexterity//2

        self.poisonRegenLoss = 0 #Players don't edit this, typically, this is more of a monster thing.
        self.poisonTimeLeft = 0
        #Character Advancement things
        self.xp = 0
        self.gp = 10
        self.level = 1
   

    def update(self):
        self.checkXP()
        if (self.health < self.maxhealth):
            self.health += self.regen
            if self.health > self.maxhealth:
                self.health = self.maxhealth

        if self.poisonTimeLeft > 0:
            self.health -= self.poisonRegenLoss
            if self.location.name != "Virulent Room":
                self.poisonTimeLeft -= 1


        



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
        print("You have "+str(self.health)+" health, "+str(self.xp)+" xp, and "+str(self.gp)+" gold")
        print("You can carry a maximum of "+str(self.carryingCapacity)+" items")
        input("Press enter to continue...")

    def goDirection(self, direction):
        if(self.location.hasMonsters()):
            print("As you leave, the monsters lash out.")
            for monster in self.location.monsters:
                monster.attackPlayer(self)
            input("Press any key to continue...")

        self.location = self.location.getDestination(direction)

    def pickup(self, item):
        self.items.append(item)
        item.loc = self
        self.location.removeItem(item)

    def equip(self,item):
        #You can only equip weapons and armor that are in your inventory. You need to pick up somethng to equip it
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
                self.defense += item.defense
                self.equipped.append(item)
                self.items.remove(item)
            else:
                print("You already have a weapon equipped")

    def drop(self, item):
        #You can't drop items that are currently equipped, you need to unequip them first
        self.items.remove(item)
        item.loc = self.location
        self.location.addItem(item)

    def unequip(self,item):
        if item.type == "weapon":
            self.bonusDamage -= item.damage
            self.equipped.remove(item)
            self.items.append(item)
        if item.type == "armor":
            self.defense -= item.defense
            self.equipped.remove(item)
            self.items.append(item)

    def showInventory(self):
        clear()
        print("You are currently carrying:")
        print()
        items = self.items[:]
        while len(items) != 0:
            currentItem = items[0].name
            del items[0]
            counter = 1
            for item in items:
                if item.name == currentItem:
                    counter += 1
                    items.remove(item)
            print(currentItem+" x"+str(counter))
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

    def getItemFromInventory(self,item):
        for thing in self.items:
            if thing.name.lower() == item.lower():
                return thing
        return False

    def isEquipped(self, name):
        for i in self.equipped:
            if i.name.lower() == name.lower():
                return i
        return False

    def checkXP(self):
        #Every 200 XP, you level up, and each of your stats are randomly increased by 0 or 1
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

            #Once your stats increase, it quickly updates the carrying capacity and such.
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
        if(mon.regeneration > 0 and mon.health > 0):
            print("The monster is regenerating!")

        if(mon.health <= 0):
            mon.die(self)
        else:
            mon.damaged = True
            mon.attackPlayer(self)

        print()
        input("Press enter to continue...")

    def buy(self,character,item):
        self.items.append(item)
        self.gp -= item.buyValue
        character.items.remove(item)
        print("You bought "+str(item.name))

    def sell(self,character,item):
        self.items.remove(item)
        self.gp += item.sellValue
        character.items.append(item)
        print("You sold "+str(item.name))

    def ViewCharacterItems(self,character):
        print("These items are for sale:")
        for item in character.items:
            print(item)