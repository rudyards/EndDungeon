from room import currentRooms
from monster import currentMonsters
from Characters import currentCharacters
from item import currentItems
from player import currentPlayers
   # elif Command == "resume":
   #          saveFile = commandWords[1].lower()
   #          if saveFile == None:
   #              print("Please specify name of saved game")
   #          with open(saveFile, "r"):
   #              file = saveFile.read()
   #              splitByObject = file.split("~")
   #              objects = splitByObject.split()
                
 # elif Command == "save2":
        #     saveFile = str(commandWords[2].lower())
        #     saveRooms(saveFile)
        #     saveRoomConnections(saveFile)
        #     saveMonsters(saveFile)
        #     saveItems(saveFile)
        #     saveCharacters(saveFile)
        #     savePlayer(saveFile)
        #     print("this game has been saved as "+str(saveFile))

    # Non-pickle resume:
#     file = game.read()
#     listOfObjects = file.split('~')
#     objects = file.split()
#     for object in objects:
#         if object[0] == "room":
#             Room(object[1],object[2],object[3],object[4],object[5])
#         elif object[0] == ""

def saveRooms(infile):
    with open(infile,"a") as saveFile:
        for room in currentRooms:
            saveFile.write("room"+"\n")
            saveFile.write(room.desc+"\n")
            saveFile.write(str(room.x)+"\n")
            saveFile.write(str(room.y)+"\n")
            saveFile.write("~\n")

def saveRoomConnections(infile):
    with open(infile,"a") as saveFile:
        for connection in roomConnections: #Make connections objects?
            saveFile.write("connection"+"\n")
            saveFile.write(str(connection[0].id)+"\n")
            saveFile.write(connection[1]+"\n")
            saveFile.write(str(connection[2].id)+"\n")
            saveFile.write(connection[3]+"\n")
            saveFile.write("~\n")

def saveMonsters(infile):
    with open(infile, "a") as saveFile:
        for monster in currentMonsters:
            saveFile.write("monster"+"\n")
            saveFile.write(monster.name+"\n")
            saveFile.write(str(monster.health)+"\n")
            saveFile.write(str(monster.room.id)+"\n")
            saveFile.write(str(monster.damaged)+"\n")
            saveFile.write(str(monster.defense)+"\n")
            saveFile.write(str(monster.level)+"\n")
            saveFile.write("~\n")

def saveItems(infile):
    with open(infile,"a") as saveFile:
        for item in currentItems:
            saveFile.write("item"+"\n")
            saveFile.write(item.name+"\n")
            saveFile.write(item.desc+"\n")
            saveFile.write(str(item.buyValue)+"\n")
            saveFile.write(str(item.sellValue)+"\n")
            saveFile.write(str(item.loc)+"\n")
            saveFile.write("~\n")

def saveCharacters(infile):
    with open(infile,"a") as saveFile:
        for character in currentCharacters:
            saveFile.write("character"+"\n")
            saveFile.write(character.name+"\n")
            for item in character.items:
                saveFile.write(item.name+"\n")
            saveFile.write("endOfItems"+"\n")
            saveFile.write("~\n")

def savePlayer(infile):
    with open(infile,"a") as saveFile:
        for player in currentPlayers:
            saveFile.write("player"+"\n")
            saveFile.write(player.name+"\n")
            saveFile.write(str(player.location)+"\n")
            saveFile.write(str(player.strength)+"\n")
            saveFile.write(str(player.dexterity)+"\n")
            saveFile.write(str(player.constitution)+"\n")
            saveFile.write(str(player.wisdom)+"\n")
            saveFile.write(str(player.intelligence)+"\n") 
            saveFile.write(str(player.charisma)+"\n")
            saveFile.write(str(player.hasWeapon)+"\n")
            saveFile.write(str(player.hasArmor)+"\n")
            saveFile.write(str(player.bonusDamage)+"\n")
            saveFile.write(str(player.poisonRegenLoss)+"\n")
            saveFile.write(str(player.poisonTimeLeft)+"\n")
            saveFile.write(str(player.xp)+"\n")
            saveFile.write(str(player.gp)+"\n")
            saveFile.write(str(player.level)+"\n")
            for item in player.items:
                saveFile.write(item.name+"\n")
                saveFile.write("endOfItems\n")
            for item in player.equipped:
                saveFile.write(item.name+"\n")
                saveFile.write("endOfEquipped\n")
            saveFile.write("~\n")

def saveGameVariables(infile):
    with open(infile,"a") as saveFile:
        saveFile.write(str(counter.getValue()))




