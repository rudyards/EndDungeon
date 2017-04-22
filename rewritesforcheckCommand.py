commands = ["attack","buy","drop","equip","exit","go","help","inspect","inventory","me","pickup","resume","save","sell","talk","unequip"]
def checkCommand(entry):
    commandList = commands[:]
    for command in commands:
        i = 0
        while i<len(entry):
            print(entry[i])
            print(command[i])
            if entry[i] != command[i]:
                commandList.remove(command)
            i += 1
            print(commandList)
    if len(commandList) == 0:
        print("That is not a valid command")
        commandSuccess = False
    elif len(commandList) == 1:
        callCommand(commandList[0])
        print(commandList[0])
    else:
        print("did you mean "+commandList[0]+ "or"+commandList[1])
        commandSuccess = False

def callCommand(command):

        if command == "go":   #cannot handle multi-word directions
            player.goDirection(commandWords[1]) 
            timePasses = True


        elif command == "pickup":  #can handle multi-word objects
            targetName = command[int(len(commandWords[0])+1):]
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

        elif command == "drop":
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

        elif command == "inventory":
            player.showInventory()        
            player.showEquipped()


        elif command == "help":
            showHelp()


        elif command == "exit":
            playing = False


        elif command == "attack":
            targetName = command[7:]
            target = player.location.getMonsterByName(targetName)
            if target != False:
                player.attackMonster(target)
                timePasses = True
            else:
                print("No such monster.")
                commandSuccess = False


        elif command == "wait":
            timePasses = True
        

        elif command == "me":
            player.showStats()


        elif command == "equip":
            equipChoice = command[6:]
            equipitem = player.isInInventory(equipChoice)
            if equipitem != False:
                player.equip(equipitem)
                #Bug: A player can equip any number of items
            else:
                print("You aren't currently carrying that.")
                commandSuccess = False


        elif command == "unequip":
            equipChoice = command[8:]
            equipitem = player.isEquipped(equipChoice)
            if equipitem != False:
                player.unequip(equipitem)
            else:
                print("That isn't currently equipped.")
                commandSuccess = False
                
        elif command == "inspect":
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

        elif command == "talk":
            characterName = commandWords[2].lower()
            character = player.location.getCharacterByName(characterName)
            if character != False:
                print(character.tagLine)
            else:
                print("That character is not in the room")
            commandSuccess = False

        elif command == "view":
            characterName = commandWords[1].lower()
            character = player.location.getCharacterByName(characterName)
            if character != False:
                for item in character.items:
                    print(item.name)
            else:
                print(str(characterName)+ " is not in this room")
            commandSuccess = False

        elif command == "buy":
            itemName = commandWords[1].lower()
            characterName = commandWords[3].lower()
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

        elif command == "sell":
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

        elif command == "save":
            saveFile = str(commandWords[2].lower())
            saveRooms(saveFile)
            saveRoomConnections(saveFile)
            saveMonsters(saveFile)
            saveItems(saveFile)
            saveCharacters(saveFile)
            savePlayer(saveFile)
            print("this game has been saved as "+str(saveFile))

        elif command == "resume":
            saveFile = commandWords[1].lower()


        else:
            print("Not a valid command")
            commandSuccess = False
        if timePasses == True:
            updater.updateAll()

checkCommand(commandWords[0].lower())

 