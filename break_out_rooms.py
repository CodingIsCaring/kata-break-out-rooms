

def break_out_rooms(rounds, participants, room_size):
    total_rooms = len(participants) / room_size

    if len(participants) == room_size:
        result = [participants[0] + ", " + participants[1]]
    else:
        result = []
        for index in range(0, len(participants), room_size):
            result.append(get_random_participants(index, participants, room_size))

    return [result]


def get_random_participants(index, participants, room_size):
    room = ''
    for i in range(room_size):
        room = room + participants[index + i] + ", "
    position_last_comma = len(room) - 2
    return room[0: position_last_comma]
