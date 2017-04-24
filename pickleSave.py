from player import currentPlayers
from monster import currentMonsters
from room import CurrentRooms
from room import roomConnections
from Characters import currentCharacters
import pickle

dictionaryOfLists = {}
dictionaryOfLists["currentPlayers"] = currentPlayers
dictionaryOfLists["currentMonsters"] = currentMonsters
dictionaryOfLists["currentRooms"] = currentRooms
dictionaryOfLists["roomConnections"] = roomConnections
dictionaryOfLists["currentCharacters"] = currentCharacters

pickle.dump(currentPlayers,open("infile","wb"))