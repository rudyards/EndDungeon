import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Item:
    def __init__(self, name, desc):
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
    def __init__(self,name,desc,damage):
        super(Weapon,self).__init__(name,desc)
        self.damage = damage
        self.type = "weapon"


class Armor(Item):
    #Weapons only have 1 new thing about them, damage (which is a bonus to their damage)
    def __init__(self,name,desc,defense):
        super(Armor,self).__init__(name,desc)
        self.defense = defense
        self.type = "armor"






longsword = Weapon("Longsword", "A basic weapon, sharp and effective", 3)
hideArmor = Armor("Hide Armor", "Made of baloth leather, this should keep you safer", 1)
rock1 = Item("Rock", "a rock, used for testing carrying capacity")
rock2 = Item("Rock2", "a rock, used for testing carrying capacity")
rock3 = Item("Rock3", "a rock, used for testing carrying capacity")
rock4 = Item("Rock4", "a rock, used for testing carrying capacity")
rock5 = Item("Rock5", "a rock, used for testing carrying capacity")
rock6 = Item("Rock6", "a rock, used for testing carrying capacity")
rock7 = Item("Rock7", "a rock, used for testing carrying capacity")
rock8 = Item("Rock8", "a rock, used for testing carrying capacity")
