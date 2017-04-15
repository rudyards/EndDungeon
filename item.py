import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc, buyValue, sellValue):
        self.name = name
        self.desc = desc
        self.loc = None
    def describe(self):
        clear()
        print(self.desc)
        print()
        input("Press enter to continue...")
    def putInRoom(self, room):
        self.loc = room
        room.addItem(self)

class Weapon(Item):
    #Weapons only have 1 new thing about them, damage (which is a bonus to their damage)
    def __init__(self, name, desc, buyValue, sellValue, damage):
        Item.__init__(self,name,desc,buyValue,sellValue)
        self.damage = damage
        self.type = "weapon"


class Armor(Item):
    #Weapons only have 1 new thing about them, damage (which is a bonus to their damage)
    def __init__(self, name, desc, buyValue, sellValue, defense):
        Item.__init__(self,name,desc,buyValue,sellValue)
        self.defense = defense
        self.type = "armor"


goldBar = Item("Gold Bar", "While blovered, this brick of gold will sell for a pretty penny",200,150)
brokenSword = Item("Broken Sword", "This sword hilt likely once served an adventurer well,at least until they died. Horribly.",5,1)

gauntlet = Weapon("Spiked Gauntlet","This fits over your hand, preventing you from wieldingother weapons. But it can smash faces, so that's a plus.",10,5,1)
dagger = Weapon("Dagger", "Small, sharp, slipping between ribs with grace",5,2, 1)
longsword = Weapon("Longsword", "A basic weapon, sharp and effective",15,7, 2)
warhammer = Weapon("Warhammer", "Massive crushing force delivered with an overhead swing!",20,10, 3)
greatsword = Weapon("Greatsword", "This weapon is increadibly heavy, easily capable of  cleaving skulls in half",35,15, 4)

hideArmor = Armor("Hide Armor", "Made of baloth leather, this should keep you safer",15,6, 1)
chainShirt = Armor("Chain Shirt", "A shirt made of interwoven rings, crafted of the finest steel",30,10,2)
chainmail = Armor("Chainmail", "Heavy rings of metal cover the upper body of this armor, reinforced with leather",45,20,3)
platemail = Armor("Platemail", "The sturdiest armor in this dungeon. Moving is going to be a sturggle, but at least you'll never die.",60,30,4) 

merchantList1 = [hideArmor,chainShirt,platemail]
merchantList2 = [chaimail,hideArmor,platemail,dagger]
merchantList3 = [chainShirt,chainmail,dagger]

blacksmithList1 = [gauntlet,lognsword,warhammer,dagger]
blacksmithList2 = [dagger,greatsword,warhammer,gauntlet]
blacksmithList3 = [greatsword, warhammer,gauntlet,dagger,longsword]