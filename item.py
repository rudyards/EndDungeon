import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#list of current items (for pickling)
currentItems = []

#Item Class
class Item:
    def __init__(self, name, desc, buyValue, sellValue):
        self.name = name
        self.desc = desc
        self.loc = None
        self.buyValue = buyValue
        self.sellValue = sellValue
        currentItems.append(self)

    #provides description of item
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    #places item in room
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)

#weapons are a subtype that inherit from Item
class Weapon(Item):
    #Weapons only have 1 new thing about them, damage (which is a bonus to their damage)
    def __init__(self, name, desc, buyValue, sellValue, damage):
        Item.__init__(self,name,desc,buyValue,sellValue)
        self.damage = damage
        self.type = "weapon"

#armor is one as well
class Armor(Item):
    #Weapons only have 1 new thing about them, damage (which is a bonus to their damage)
    def __init__(self, name, desc, buyValue, sellValue, defense):
        Item.__init__(self,name,desc,buyValue,sellValue)
        self.defense = defense
        self.type = "armor"



#Treasure items: Not useful but can be sold for quite a bit
goldBar = Item("goldBar", "While old, this brick of gold will sell for a pretty penny",200,150)
pieceOfArt = Item("pieceOfArt", "How did this end up in a dungeon?",150,100)
#Junk items: Not useful, but this helps tone down how good monster drops are
brokenSword = Item("brokenSword", "This sword hilt likely once served an adventurer well,at least until they died. Horribly.",5,1)
monsterSkull = Item("monsterSkull", "A fractured and cleaned skull of a monster. You breifly debate holding it and monologuing. But you aren't a bard.",5,1)
rock = Item("rock", "It's just a rock. Useful for testing your carrying capacity, at least?",2,1)
#Healing potion: Gives you health back, woo
healingPotion = Item("healingPotion", "A glass bottle full of a curative, green liquid",80,20)
#Weapons: Gauntlet and Dagger act as tier 1, longsword tier 2, warhammer tier 3, greatsword tier 4
gauntlet = Weapon("spikedGauntlet","This fits over your hand, preventing you from wielding other weapons. But it can smash faces, so that's a plus.",10,5,1)
dagger = Weapon("dagger", "Small, sharp, slipping between ribs with grace",5,2, 1)
longsword = Weapon("longsword", "A basic weapon, sharp and effective",15,7, 2)
warhammer = Weapon("warhammer", "Massive crushing force delivered with an overhead swing!",20,10, 3)
greatsword = Weapon("greatsword", "This weapon is incredibly heavy, easily capable of  cleaving skulls in half",35,15, 4)
#Armor: Hide armor is tier 1, chainshift tier 2, chainmail tier 3, plate tier 4
hideArmor = Armor("hideArmor", "Made of baloth leather, this should keep you safer",15,6, 1)
chainShirt = Armor("chainShirt", "A shirt made of interwoven rings, crafted of the finest steel",30,10,2)
chainmail = Armor("chainmail", "Heavy rings of metal cover the upper body of this armor, reinforced with leather",45,20,3)
platemail = Armor("platemail", "The sturdiest armor in this dungeon. Moving is going to be a sturggle, but at least you'll never die.",60,30,4) 

#A function that can be called when items randomly drop in order to properly create them (while reducing how much we need to repeat ourselves)
def makeItem(kind):
    if kind == "goldBar":
        return Item("goldBar", "While old, this brick of gold will sell for a pretty penny",200,150)
    if kind == "healingPotion":
        return Item("healingPotion", "This amulet replenishes health",80,20)
    if kind =="pieceOfArt":
        return Item("pieceOfArt", "How did this end up in a dungeon?",150,100)
    if kind == "monsterSkull":
        return Item("monsterSkull", "A fractured and cleaned skull of a monster. You breifly debate holding it and monologuing. But you aren't a bard.",5,1)
    if kind == "rock":
        return Item("rock", "It's just a rock. Useful for testing your carrying capacity, at least?",2,1)
    if kind == "brokenSword":
        return Item("brokenSword", "This sword hilt likely once served an adventurer well, at least until they died. Horribly.",5,1)
    if kind == "gauntlet":
        return Weapon("spikedGauntlet","This fits over your hand, preventing you from wielding other weapons. But it can smash faces, so that's a plus.",10,5,1)        
    if kind == "dagger":
        return Weapon("dagger", "Small, sharp, slipping between ribs with grace",5,2, 1)
    if kind == "longsword":
        return Weapon("longsword", "A basic weapon, sharp and effective",15,7, 2)
    if kind == "warhammer":
        return Weapon("warhammer", "Massive crushing force delivered with an overhead swing!",20,10, 3)
    if kind == "greatsword":
        return Weapon("greatsword", "This weapon is increadibly heavy, easily capable of  cleaving skulls in half",35,15, 4)
    if kind == "hideArmor":
        return Armor("hideArmor", "Made of baloth leather, this should keep you safer",15,6, 1)
    if kind == "chainShirt":
        return Armor("chainShirt", "A shirt made of interwoven rings, crafted of the finest steel",30,10,2)
    if kind == "chainmail":
        return Armor("chainmail", "Heavy rings of metal cover the upper body of this armor, reinforced with leather",45,20,3)
    if kind == "platemail":
        return Armor("platemail", "The sturdiest armor in this dungeon. Moving is going to be a sturggle, but at least you'll never die.",60,30,4) 

#Three random item lists for the merchants. They will have one of the following sets of wares
merchantList1 = ["hideArmor","chainShirt","platemail","healingPotion"]
merchantList2 = ["chainmail","hideArmor","platemail","dagger"]
merchantList3 = ["chainShirt","chainmail","dagger", "healingPotion"]
#Three random item lists but for blacksmiths. Blacksmiths only sell weapons
blacksmithList1 = ["gauntlet","longsword","warhammer","dagger"]
blacksmithList2 = ["dagger","greatsword","warhammer","gauntlet"]
blacksmithList3 = ["greatsword", "warhammer","gauntlet","dagger","longsword"]



#All of the items that exist in the game. Useful for random loot.
totalItemList = ["goldBar","brokenSword","gauntlet","dagger","longsword","warhammer","greatsword","hideArmor","chainmail","chainShirt","platemail","healingPotion","pieceofArt", "monsterSkull", "rock"]

