from room import currentRooms

def findRoombyID(ID):
    for rooms in currentRooms:
        if rooms.ID == int(ID):
            return rooms
    raise RuntimeError("room id not in currentRooms")