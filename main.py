from room import *
from player import *
from item import *
from monster import *
from maps import *
from Characters import *
import os
import updater
from saveGame import *


name = input("What's your name?\n")
player = Player(name)
print("")
def createWorld():

    startingRoom = Room("The entrance to the great dungeon",2,6)
    secondRoom = Room(roomdescriber(),2,5)
    Room.connectRooms(startingRoom, "north", secondRoom, "south")
    thirdRoom = Room(roomdescriber(),2,4)
    Room.connectRooms(secondRoom, "north", thirdRoom, "south")
    fourthRoom = Room(roomdescriber(),2,3)
    Room.connectRooms(thirdRoom, "north", fourthRoom, "south")
    fifthRoom = Room(roomdescriber(),3,3)
    Room.connectRooms(fourthRoom, "west", fifthRoom, "east")
    sixthRoom = Room(roomdescriber(),4,3)
    Room.connectRooms(fifthRoom, "west", sixthRoom, "east")
    seventhRoom = Room(roomdescriber(),5,3)
    Room.connectRooms(sixthRoom, "west", seventhRoom, "east")
    eigthRoom = Room(roomdescriber(),5,4)
    Room.connectRooms(seventhRoom, "south", eigthRoom, "north")
    ninthRoom = Room(roomdescriber(),6,4)
    Room.connectRooms(eigthRoom, "west", ninthRoom, "east")
    tenthRoom = Room(roomdescriber(),7,4)
    Room.connectRooms(ninthRoom, "west", tenthRoom, "east")

    player.location = startingRoom
    merchant1 = Merchant("merchant1")
    merchant1.putInRoom(startingRoom)


#    entrance = Room("You are in the entrance of The Dungeon of the End")
#    player.location = entrance
    longsword.putInRoom(startingRoom)
    hideArmor.putInRoom(startingRoom)
    hideArmor.putInRoom(startingRoom)
    monster1 = Troll("bob",secondRoom)
    monster2 = Troll("ted",secondRoom)
    monster3 = Troll("cindy",secondRoom)

#    genericDungeonRoom = Room("This is the place where a test monster is")
#    Room.connectRooms(entrance, "south", genericDungeonRoom, "north")


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
    print("equip <item> -- equips an item you are carrying. only one weapon and one armor can be equipped at once")
    print("unequip <item> -- unequips an item you have equipped.")
    print("wait -- waits one turn")
    print("")
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
        print(command)
        commandWords = command.split()
        print(commandWords)

        commands = ["attack","buy","drop","equip","exit","go","help","inspect","inventory","me","pickup","resume","save","sell","talk","unequip"]

        entry = str(commandWords[0].lower())
        print(entry)

        commandList = []
        for word in commands:
            print(word)
            if word.startswith(entry):
                commandList.append(word)
            print(commandList)
            # i = 0
            # while i<len(entry):
            #     if entry[i] == word[i]:
            #         print(word[i])
            #         print(word)
            #         i += 1
            #     else:
            #         break
            #     commandList.append(word)
            #     break
            #     print(commandList)
        if len(commandList) == 0:
            print("That is not a valid command")
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
            targetName = commandWords[1] #int(len(commandWords[0])+1):]
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
            else:
                print("That isn't currently equipped.")
                commandSuccess = False
                
        elif Command == "inspect":
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
            saveFile = str(commandWords[2].lower())
            saveRooms(saveFile)
            saveRoomConnections(saveFile)
            saveMonsters(saveFile)
            saveItems(saveFile)
            saveCharacters(saveFile)
            savePlayer(saveFile)
            print("this game has been saved as "+str(saveFile))

        elif Command == "resume":
            saveFile = commandWords[1].lower()
            if saveFile == None:
                print("Please specify name of saved game")
            with open(saveFile, "r"):
                file = saveFile.read()
                splitByObject = file.split("~")
                objects = splitByObject.split()

        if timePasses == True:
            updater.updateAll()

  
        
    #     def checkAmbiguity(entry):
    #          if entry == "i" or entry == "in":
    #             return True
    #             commandSuccess = False

    #     def checkCommand(entry, command): #Idk if this is the best place to put this function, might make the code prettier elsewhere
    #         matchedLetters = 0
    #         if len(entry)>len(command):
    #             return False
    #         for letter in range(0,len(entry)):
    #             #print("checking " + entry[letter] + " == " + command[letter])
    #             if entry[letter] == command[letter]:
    #                 matchedLetters += 1
    #         if matchedLetters == len(entry):
    #             #print("checking " + str(matchedLetters) + " == " + str(len(entry)))
    #             return True
    #         else:
    #             return False
    #     #def checkCommand(entry,command):
    #     #    if entry == command:
    #     #        return True

    #     firstWord = commandWords[0].lower()

    #     if checkAmbiguity(firstWord):
    #         print("did you mean inspect or inventory?")
    #         commandSuccess = False

    #     elif checkCommand(firstWord,"go"):   #cannot handle multi-word directions
    #         player.goDirection(commandWords[1]) 
    #         timePasses = True


    #     elif checkCommand(firstWord,"pickup"):  #can handle multi-word objects
    #         targetName = command[int(len(commandWords[0])+1):]
    #         target = player.location.getItemByName(targetName)
    #         if target != False:
    #             if (len(player.equipped)+len(player.items)<player.carryingCapacity):
    #                 player.pickup(target)
    #             else:
    #                 print("You're carrying too much. Try dropping some items first.")
    #                 commandSuccess = False
    #         else:
    #             print("No such item.")
    #             commandSuccess = False

    #     elif checkCommand(firstWord,"drop"):
    #         targetName = command[5:]
    #         target = player.isInInventory(targetName)
    #         if target != False:
    #             player.drop(target)
    #         else:
    #             print("That item is not currently in your inventory.")
    #             newtarget = player.isEquipped(targetName)
    #             if newtarget != False:
    #                 print("Make sure to unequip it first")
    #                 print()
    #             commandSuccess = False

    #     elif checkCommand(firstWord,"inventory"):
    #         player.showInventory()        
    #         player.showEquipped()


    #     elif checkCommand(firstWord,"help"):
    #         showHelp()


    #     elif checkCommand(firstWord,"exit"):
    #         playing = False


    #     elif checkCommand(firstWord,"attack"):
    #         targetName = command[7:]
    #         target = player.location.getMonsterByName(targetName)
    #         if target != False:
    #             player.attackMonster(target)
    #             timePasses = True
    #         else:
    #             print("No such monster.")
    #             commandSuccess = False


    #     elif checkCommand(firstWord,"wait"):
    #         timePasses = True
        

    #     elif checkCommand(firstWord,"me"):
    #         player.showStats()


    #     elif checkCommand(firstWord,"equip"):
    #         equipChoice = command[6:]
    #         equipitem = player.isInInventory(equipChoice)
    #         if equipitem != False:
    #             player.equip(equipitem)
    #             #Bug: A player can equip any number of items
    #         else:
    #             print("You aren't currently carrying that.")
    #             commandSuccess = False


    #     elif checkCommand(firstWord,"unequip"):
    #         equipChoice = command[8:]
    #         equipitem = player.isEquipped(equipChoice)
    #         if equipitem != False:
    #             player.unequip(equipitem)
    #         else:
    #             print("That isn't currently equipped.")
    #             commandSuccess = False
                
    #     elif checkCommand(firstWord,"inspect"):
    #         descriptionGiven = False
    #         while not descriptionGiven:
    #             for item in player.items:
    #                 if checkCommand(commandWords[1].lower(),item.name()):
    #                     item.describe()
    #                     descriptionGiven = True
    #         while not descriptionGiven:
    #             for item in player.location.items:
    #                     if checkCommand(commandWords[1].lower(),item.name()):
    #                         item.describe()
    #                         descriptionGiven = True 
    #         if not descriptionGiven: 
    #                 print("You do not have that item")
    #         commandSuccess = False

    #     elif checkCommand(firstWord,"talk"):
    #         characterName = commandWords[2].lower()
    #         character = player.location.getCharacterByName(characterName)
    #         if character != False:
    #             print(character.tagLine)
    #         else:
    #             print("That character is not in the room")
    #         commandSuccess = False

    #     elif checkCommand(firstWord,"view"):
    #         characterName = commandWords[1].lower()
    #         character = player.location.getCharacterByName(characterName)
    #         if character != False:
    #             for item in character.items:
    #                 print(item.name)
    #         else:
    #             print(str(characterName)+ " is not in this room")
    #         commandSuccess = False

    #     elif checkCommand(firstWord,"buy"):
    #         itemName = commandWords[1].lower()
    #         characterName = commandWords[3].lower()
    #         character = player.location.getCharacterByName(characterName)
    #         if character != False:
    #             item = character.getItemFromInventory(itemName)
    #             if item != False:
    #                 player.buy(character,item) 
    #             else:
    #                 print(str(characterName)+ " does not have that item")
    #         else:
    #             print(str(characterName)+" is not in this room")
    #         commandSuccess = False

    #     elif checkCommand(firstWord,"sell"):
    #         itemName = commandWords[1].lower()
    #         characterName = commandWords[3].lower()
    #         character = player.location.getCharacterByName(characterName)
    #         if character != False:
    #             item = character.getItemfromInventory(itemName)
    #             if item != False:
    #                 player.sell(character,item) 
    #             else:
    #                 print(str(characterName)+ " does not have that item")
    #         else:
    #             print(str(characterName)+" is not in this room")
    #         commandSuccess = False

    #     elif checkCommand(firstWord, "save"):
    #         saveFile = str(commandWords[2].lower())
    #         saveRooms(saveFile)
    #         saveRoomConnections(saveFile)
    #         saveMonsters(saveFile)
    #         saveItems(saveFile)
    #         saveCharacters(saveFile)
    #         savePlayer(saveFile)
    #         print("this game has been saved as "+str(saveFile))

    #     elif checkCommand(firstWord, "resume"):
    #         saveFile = commandWords[1].lower()


    #     else:
    #         print("Not a valid command")
    #         commandSuccess = False
    # if timePasses == True:
    #     updater.updateAll()

    


