class Character:
    characterCounter = 0
    def __init__(self,name):
        self.type = name + str(charcterCounter)
        Character.characterCounter += 1
        self.items = []
        self.location = None

    def putInRoom(self, room):
        self.loc = room
        room.addCharacter(self)

    def GetItemFromInventory(self,item):
        for thing in self.items:
            if thing.name.lower() == item.lower():
                return thing
        return False

class Merchant(Character):
    self.tagLine = "Good day. I am a Merchant. You can buy items from my selection of wares or sell me your own."
    merchantListNumber = random.randint(1,3)
    if merchantListNumber = 1:
        self.items = Item.merchantList1[:]
    elif merchantListNumber = 2:
        self.items = Item.merchantList2[:]
    else:
        self.items = Item.merchantList3[:]

class Blacksmith(Character):
    self.tagLine = "Good day. I am a Blacksmith. You can buy items from my selection of wares or sell me your own."
    blacksmithListNumber = random.randint(1,3)
    if blacksmithListNumber = 1:
        self.items = Item.blacksmithList1[:]
    elif blacksmithListNumber = 2:
        self.items = Item.blacksmithList2[:]
    else:
        self.items = Item.blacksmithList3[:]

