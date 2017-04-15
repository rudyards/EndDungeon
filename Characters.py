class Character:
    characterCounter = 0
    def __init__(self,name):
        self.type = name + str(charcterCounter)
        Character.characterCounter += 1
        self.items = []

class Merchant(Character):
    merchantListNumber = random.randint(1,3)
    if merchantListNumber = 1:
        self.items = Item.merchantList1[:]
    elif merchantListNumber = 2:
        self.items = Item.merchantList2[:]
    else:
        self.items = Item.merchantList3[:]

class Blacksmith(Character):
    blacksmithListNumber = random.randint(1,3)
    if blacksmithListNumber = 1:
        self.items = Item.blacksmithList1[:]
    elif blacksmithListNumber = 2:
        self.items = Item.blacksmithList2[:]
    else:
        self.items = Item.blacksmithList3[:]

