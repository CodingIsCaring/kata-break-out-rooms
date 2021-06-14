

def break_out_rooms(rounds, participants, room_size):
    total_rooms = len(participants) / room_size

    if len(participants) == room_size:
        result = [participants[0] + ", " + participants[1]]
    else:
        result = []
        for index in range(0, len(participants), 2):
            result.append(participants[index] + ", " + participants[index + 1])

    return [result]
