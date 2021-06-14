

def break_out_rooms(rounds, participants, room_size):
    if len(participants) == room_size:
        result = [participants[0] + ", " + participants[1]]
    else:
        result = [participants[0] + ", " + participants[1]]
        result2 = participants[2] + ", " + participants[3]
        result.append(result2)
    return [result]
