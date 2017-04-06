from room import *
from player import *
from item import *
from monster import *
import os
import updater

player = Player()

def createWorld():
    entrance = Room("You are in the entrance of The Dungeon of the End")
    player.location = entrance
    longsword.putInRoom(entrance)
    hideArmor.putInRoom(entrance)
    rock1.putInRoom(entrance)
    rock2.putInRoom(entrance)
    rock3.putInRoom(entrance)
    rock4.putInRoom(entrance)
    rock5.putInRoom(entrance)
    rock6.putInRoom(entrance)
    rock7.putInRoom(entrance)
    rock8.putInRoom(entrance)

    genericDungeonRoom = Room("This is the place where the test monster is")
    Room.connectRooms(entrance, "south", genericDungeonRoom, "north")
    questBeast = Monster("Questbeast", 1, genericDungeonRoom,200)

    # a = Room("You are in room 1")
    # b = Room("You are in room 2")
    # c = Room("You are in room 3")
    # d = Room("You are in room 4")
    # Room.connectRooms(a, "east", b, "west")
    # Room.connectRooms(c, "east", d, "west")
    # Room.connectRooms(a, "north", c, "south")
    # Room.connectRooms(b, "north", d, "south")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printSituation():
    clear()
    print(player.location.desc)
    print()
    if player.location.hasMonsters():
        print("This room contains the following monsters:")
        for m in player.location.monsters:
            print(m.name)
        print()
    if player.location.hasItems():
        print("This room contains the following items:")
        for i in player.location.items:
            print(i.name)
        print()
    print("You can go in the following directions:")
    for e in player.location.exitNames():
        print(e)
    print()

def showHelp():
    clear()
    print("go <direction> -- moves you in the given direction")
    print("attack <monster> -- make one attack against a monster")
    print("inventory -- opens your inventory")
    print("pickup <item> -- picks up the item")
    print("equip <item> -- equips an item you are carrying. only one weapon and one armor can be equipped at once")
    print("unequip <item> -- unequip an item you have equipped.")
    print("wait -- wait one turn")
    input("Press enter to continue...")



createWorld()
playing = True
while playing and player.alive:
    printSituation()
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        commandWords = command.split()

        if commandWords[0].lower() == "go":   #cannot handle multi-word directions
            player.goDirection(commandWords[1]) 
            timePasses = True


        elif commandWords[0].lower() == "pickup":  #can handle multi-word objects
            targetName = command[7:]
            target = player.location.getItemByName(targetName)
            if target != False:
                if (len(player.equipped)+len(player.items)<player.carryingCapacity):
                    player.pickup(target)
                else:
                    print("You're carrying too much. Try dropping some items first.")
                    commandSuccess = False
            else:
                print("No such item.")
                commandSuccess = False

        elif commandWords[0].lower() == "drop":
            targetName = command[5:]
            target = player.isInInventory(targetName)
            if target != False:
                player.drop(target)
            else:
                print("That item is not currently in your inventory.")
                newtarget = player.isEquipped(targetName)
                if newtarget != False:
                    print("Make sure to unequip it first")
                    print()
                commandSuccess = False

        elif commandWords[0].lower() == "inventory":
            player.showInventory()        
            player.showEquipped()


        elif commandWords[0].lower() == "help":
            showHelp()


        elif commandWords[0].lower() == "exit":
            playing = False


        elif commandWords[0].lower() == "attack":
            targetName = command[7:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                player.attackMonster(target)
            else:
                print("No such monster.")
                commandSuccess = False


        elif commandWords[0].lower() == "wait":
            timePasses = True
        

        elif commandWords[0].lower() == "me":
            player.showStats()


        elif commandWords[0].lower() == "equip":
            equipChoice = command[6:]
            equipitem = player.isInInventory(equipChoice)
            if equipitem != False:
                player.equip(equipitem)
                #Bug: A player can equip any number of items
            else:
                print("You aren't currently carrying that.")
                commandSuccess = False


        elif commandWords[0].lower() == "unequip":
            equipChoice = command[8:]
            equipitem = player.isEquipped(equipChoice)
            if equipitem != False:
                player.unequip(equipitem)
            else:
                print("That isn't currently equipped.")
                commandSuccess = False
                
        elif checkCommand(commandWords[0].lower(),"inspect"):
            descriptionGiven = False
            while not descriptionGiven:
                for item in player.items:
                    if checkCommand(commandWords[1].lower(),item.name()):
                        item.describe()
                        descriptionGiven = True
            while not descriptionGiven:
                for item in player.location.items:
                        if checkCommand(commandWords[1].lower(),item.name()):
                            item.describe()
                            descriptionGiven = True 
            if not descriptionGiven: 
                    print("You do not have that item")
            commandSuccess = False

        else:
            print("Not a valid command")
            commandSuccess = False
    if timePasses == True:
        updater.updateAll()

    


