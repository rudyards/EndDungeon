from room import currentRooms
from room import roomConnections
from monster import currentMonsters
from Characters import currentCharacters
from item import currentItems
from player import currentPlayers

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
            saveFile.write(str(connection[0])+"\n")
            saveFile.write(connection[1]+"\n")
            saveFile.write(str(connection[2])+"\n")
            saveFile.write(connection[3]+"\n")
            saveFile.write("~\n")

def saveMonsters(infile):
    with open(infile, "a") as saveFile:
        for monster in currentMonsters:
            saveFile.write("monster"+"\n")
            saveFile.write(monster.name+"\n")
            saveFile.write(str(monster.health)+"\n")
            saveFile.write(str(monster.room)+"\n")
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





