from room import *
from player import *
from item import *
from monster import *
from maps import *
from Characters import *
import os
import updater
from saveGame import *
import pickle
import glob
import random


def coinFlip():
    result = random.randint(0,1)
    if result == 0:
        return True
    else:
        return False

def generateBaseMap():
    #This is the function that creates the base dungeon used in the game. The useful thing about doing the code this way is
    #that it would be trivial to have additional functions for alternative maps and randomly decide between them
    #The base map looks like this: http://grid-paint.com/images/details/4760687939158016
    startingRoom = Room("The entrance to the great dungeon",2,6)
    secondRoom = Room(roomdescriber(),2,5)
    Room.simpleConnectRooms(startingRoom, secondRoom)
    thirdRoom = Room(roomdescriber(),2,4)
    Room.simpleConnectRooms(secondRoom, thirdRoom)
    fourthRoom = Room(roomdescriber(),2,3)
    Room.simpleConnectRooms(thirdRoom, fourthRoom)
    fifthRoom = Room(roomdescriber(),3,3)
    Room.simpleConnectRooms(fourthRoom, fifthRoom)
    sixthRoom = Room(roomdescriber(),4,3)
    Room.simpleConnectRooms(fifthRoom, sixthRoom)
    seventhRoom = Room(roomdescriber(),5,3)
    Room.simpleConnectRooms(sixthRoom, seventhRoom)
    eigthRoom = Room(roomdescriber(),5,4)
    Room.simpleConnectRooms(seventhRoom, eigthRoom)
    ninthRoom = Room(roomdescriber(),6,4)
    Room.simpleConnectRooms(eigthRoom, ninthRoom)
    EndRoom = Room(roomdescriber(),7,4)
    Room.simpleConnectRooms(ninthRoom, EndRoom)

    #Once it has created all the rooms, this function returns a list which contains all of them
    return [startingRoom,secondRoom,thirdRoom,fourthRoom,fifthRoom,sixthRoom,seventhRoom,eigthRoom,ninthRoom,EndRoom]

def firstBaseExpansion(rooms):
    addedRooms = []
    firstBonusRoom = None
    secondBonusRoom = None
    thirdBonusRoom = None
    fourthBonusRoom = None
    fifthBonusRoom = None
    sixthBonusRoom = None
    seventhBonusRoom = None
    eigthBonusRoom = None
    ninthBonusRoom = None

    #firstBaseExpansion is called after the map is made and is based a current version of the map. It is designed only for compatibility
    #with baseMap. It goes through a series of rooms, and decides whether or not they'll be included in this iteration of the map.
    #Once they've been generated, there is a chance whether or not they connect to other nearby bonus rooms.
    #The full map, after the firstBaseExpansion, looks like: http://grid-paint.com/images/details/5914211465035776
    if coinFlip():
        firstBonusRoom = Room(roomdescriber(),3,6)
        Room.simpleConnectRooms(rooms[0], firstBonusRoom)
        addedRooms.append(firstBonusRoom)
    if coinFlip():
        secondBonusRoom = Room(roomdescriber(),3,5)
        Room.simpleConnectRooms(rooms[1], secondBonusRoom)
        addedRooms.append(secondBonusRoom)
        if firstBonusRoom in addedRooms:
            if coinFlip():
                Room.simpleConnectRooms(firstBonusRoom, secondBonusRoom)
    if coinFlip():
        thirdBonusRoom = Room(roomdescriber(),3,4)
        Room.simpleConnectRooms(rooms[2], thirdBonusRoom)
        Room.simpleConnectRooms(rooms[4], thirdBonusRoom)
        addedRooms.append(thirdBonusRoom)
        if secondBonusRoom in addedRooms:
            if coinFlip():
                Room.simpleConnectRooms(secondBonusRoom,thirdBonusRoom)
    if coinFlip():
        fourthBonusRoom = Room(roomdescriber(),4,4)
        Room.simpleConnectRooms(rooms[5], fourthBonusRoom)
        Room.simpleConnectRooms(rooms[7], fourthBonusRoom)
        addedRooms.append(fourthBonusRoom)
        if thirdBonusRoom in addedRooms:
            if coinFlip():
                Room.simpleConnectRooms(thirdBonusRoom,fourthBonusRoom)
    if coinFlip():
        fifthBonusRoom = Room(roomdescriber(),5,5)
        Room.simpleConnectRooms(rooms[7], fifthBonusRoom)
        addedRooms.append(fifthBonusRoom)
    if coinFlip():
        sixthBonusRoom = Room(roomdescriber(),6,5)
        Room.simpleConnectRooms(rooms[8], sixthBonusRoom)
        addedRooms.append(sixthBonusRoom)
        if fifthBonusRoom in addedRooms:
            if coinFlip():
                Room.simpleConnectRooms(fifthBonusRoom,sixthBonusRoom)
    if coinFlip():
        seventhBonusRoom = Room(roomdescriber(),7,5)
        Room.simpleConnectRooms(rooms[9],seventhBonusRoom)
        addedRooms.append(seventhBonusRoom)
        if sixthBonusRoom in addedRooms:
            if coinFlip():
                Room.simpleConnectRooms(sixthBonusRoom,seventhBonusRoom)
    if coinFlip():
        eigthBonusRoom = Room(roomdescriber(),6,3)
        Room.simpleConnectRooms(rooms[8],eigthBonusRoom)
        Room.simpleConnectRooms(rooms[6],eigthBonusRoom)
        addedRooms.append(eigthBonusRoom)
    if coinFlip():
        ninthBonusRoom = Room(roomdescriber(),7,3)
        Room.simpleConnectRooms(rooms[9],ninthBonusRoom)
        addedRooms.append(ninthBonusRoom)



def createWorld():
    #The player's name isn't relevant to anything right now, but it's an opportunity for us to allow cheat codes
    #If a player uses the name grader, they get a bunch of bonus levels to make testing easier.
    name = input("What's your name?\n")
    player = Player(name)
    if player.name == "grader":
        while i < 10:
            player.xp += 200
            i+=1
        print("You start 10 levels higher than normal!")
    print("")

    #Then, we instantiate the base map, set the player's location to the first room of the map, and run our expansion code
    coreRooms = generateBaseMap()
    player.location = coreRooms[0]
    firstBaseExpansion(coreRooms)
    #We also establish a Merchant in the first room so the players can buy and sell items, as well as give them some starting items
    merchant1 = Merchant("merchant1")
    merchant1.putInRoom(player.location)
    if coinFlip():
        dagger.putInRoom(player.location)
    else:
        gauntlet.putInRoom(player.location)        
    hideArmor.putInRoom(player.location)
    rock.putInRoom(player.location)
    rapty = Velociraptor("Rapty",player.location)
    rapty2 = Velociraptor("Rapty",player.location)



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
    if player.location.hasCharacters():
        print("This room contains the following characters:")
        for i in player.location.characters:
            print(i.name)
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
    print("attack <monster> -- makes one attack against a monster")
    print("inventory -- opens your inventory")
    print("pickup <item> -- picks up the item")
    print("drop <item> -- places item from inventory into room")
    print("inspect <item> -- displays description of item")
    print("equip <item> -- equips an item you are carrying. only one weapon and one armor can be equipped at once")
    print("unequip <item> -- unequips an item you have equipped.")
    print("heal -- uses a healing potion (if one is in inventory) to regain health")
    print("wait -- waits one turn")
    print("talk to <character> -- say hi to a character")
    print("view <character> wares -- displays character's items for sale")
    print("buy <item> from <character> -- purchases item from a character")
    print("sell <item> to <character> -- sells an item to a character")
    print("save as <file name> -- saves current game progress to file")
    print("")
    input("Press enter to continue...")


option = input("resume or newGame? (Just press enter to skip)\n")
if option.lower() == "resume":
    directory = os.path.dirname(os.path.realpath(__file__))
    print(glob.glob(os.path.basename((os.path.join(str(directory),"*.sav")))))
    game = input("Which game would you like to resume?\n")
    with open(game,"rb") as file:
        currentRooms = pickle.load(file)
        roomConnections = pickle.load(file)
        currentMonsters = pickle.load(file)
        currentCharacters = pickle.load(file)
        currentPlayers = pickle.load(file)
        player = currentPlayers[0]
else:
    createWorld()
    player = currentPlayers[0]



playing = True
while playing and player.alive:
    printSituation()
    commandSuccess = False
    timePasses = False
    while not commandSuccess:
        commandSuccess = True
        command = input("What now? ")
        commandWords = command.split()

        commands = ["attack","buy","drop","equip", "exit","go","help","inventory", "inspect","me","pickup","save","sell","talk","unequip","view"]
        #Buy command breaks if improperly syntaxed
        if (len(commandWords) > 0):
            entry = str(commandWords[0].lower())
        else:
            entry = " "

        commandList = []
        for word in commands:
            if word.startswith(entry):
                commandList.append(word)

        if len(commandList) == 0:
            print("That is not a valid command. Enter 'help' to see command options")
            commandSuccess = False
            Command = None
        elif len(commandList) == 2:
            print("did you mean "+commandList[0]+ " or "+commandList[1]+"?")
            commandSuccess = False
            Command = None
        else:
            Command = str(commandList[0])

        if Command == "go":   #cannot handle multi-word directions
            player.goDirection(commandWords[1]) 
            timePasses = True


        elif Command == "pickup":  #can handle multi-word objects
            targetName = commandWords[1]
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

        elif Command == "heal":
            for item in player.items:
                if item.name == "HealingPotion":
                    if player.maxhealth-15 < player.health:
                        healthGain = player.maxhealth - player.health
                        if healthGain < 1:
                            healthGain = 0
                    else:
                        healthGain = 15
                    player.health += 15
                    if player.health > player.maxhealth:
                        player.health = player.maxhealth
                    print("You gained "+str(healthGain))
                    player.health = player.maxhealth
                    break
                print("You do not have a HealingPotion in your inventory")
            commandSuccess = False

        elif Command == "drop":
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

        elif Command == "inventory":
            player.showInventory()        
            player.showEquipped()


        elif Command == "help":
            showHelp()


        elif Command == "exit":
            playing = False


        elif Command == "attack":
            targetName = command[7:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                player.attackMonster(target)
                timePasses = True
            else:
                print("No such monster.")
                commandSuccess = False


        elif Command == "wait":
            timePasses = True
        

        elif Command == "me":
            player.showStats()


        elif Command == "equip":
            equipChoice = command[6:]
            equipitem = player.isInInventory(equipChoice)
            if equipitem != False:
                player.equip(equipitem)
                #Bug: A player can equip any number of items
            else:
                print("You aren't currently carrying that.")
                commandSuccess = False


        elif Command == "unequip":
            equipChoice = command[8:]
            equipitem = player.isEquipped(equipChoice)
            if equipitem != False:
                player.unequip(equipitem)
                player.items.append(equipitem)
            else:
                print("That isn't currently equipped.")
                commandSuccess = False
                
        elif Command == "inspect":
            descriptionGiven = False
            if commandWords[1] == None:
                print("Please specify which object you want to inspect")
            for item in player.items:
                if checkCommand(commandWords[1].lower(),item.name()):
                    item.describe()
                    descriptionGiven = True
            for item in player.location.items:
                if checkCommand(commandWords[1].lower(),item.name()):
                    item.describe()
                    descriptionGiven = True 
            if not descriptionGiven: 
                print("You do not have that item")
                descriptionGiven = True
            commandSuccess = False

        elif Command == "talk":
            characterName = commandWords[2].lower()
            character = player.location.getCharacterByName(characterName)
            if character != False:
                print(character.tagLine)
            else:
                print("That character is not in the room")
            commandSuccess = False

        elif Command == "view":
            characterName = commandWords[1].lower()
            character = player.location.getCharacterByName(characterName)
            if character != False:
                for item in character.items:
                    print(item.name)
            else:
                print(str(characterName)+ " is not in this room")
            commandSuccess = False

        elif Command == "buy":
            itemName = commandWords[1].lower()
            if itemName == None:
                print("Please specify whom you want to buy from")
                commandSuccess = False
            characterName = commandWords[3].lower()
            if characterName == None:
                print("Please specify what item you want to buy")
                commandSuccess = False
            character = player.location.getCharacterByName(characterName)
            if character != False:
                item = character.getItemFromInventory(itemName)
                if item != False:
                    player.buy(character,item) 
                else:
                    print(str(characterName)+ " does not have that item")
            else:
                print(str(characterName)+" is not in this room")
            commandSuccess = False

        elif Command == "sell":
            itemName = commandWords[1].lower()
            characterName = commandWords[3].lower()
            character = player.location.getCharacterByName(characterName)
            if character != False:
                item = character.getItemfromInventory(itemName)
                if item != False:
                    player.sell(character,item) 
                else:
                    print(str(characterName)+ " does not have that item")
            else:
                print(str(characterName)+" is not in this room")
            commandSuccess = False

        elif Command == "save":
            saveFile = commandWords[2].lower()
            with open(saveFile+".sav","wb") as f:
                pickle.dump(currentRooms,f)
                pickle.dump(currentMonsters,f)
                pickle.dump(currentCharacters,f)
                pickle.dump(currentPlayers,f)
                commandSuccess = False

        if timePasses == True:
            updater.updateAll()

  

    




