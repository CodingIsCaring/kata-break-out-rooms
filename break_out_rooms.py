import random


def create_room_with_random_participants(room_size, shadow_participants):
    room = []
    for _ in range(room_size):
        randomized_index = random.randint(0, len(shadow_participants) - 1)
        randomized_participant = shadow_participants.pop(randomized_index)
        room.append(randomized_participant)
    return room


def get_rooms_in_round(participants: list[str], room_size: int, deterministic=False):
    if deterministic:
        random.seed(room_size)
    rooms = []
    shadow_participants = participants.copy()
    while len(shadow_participants) >= 2 * room_size:
        room = create_room_with_random_participants(room_size, shadow_participants)
        rooms.append(room)
    rooms.append(shadow_participants)
    return rooms


def break_out_rooms(
    rounds: int, participants: list[str], room_size: int, deterministic=False
):
    all_rounds = []
    for _ in range(rounds):
        rooms = get_rooms_in_round(participants, room_size, deterministic)
        all_rounds.append(rooms)
    return all_rounds


# Just a refactor of break_out_rooms using list comprehensions
def break_out_rooms_list_comprehension(
    rounds: int, participants: list[str], room_size: int
):
    return [get_rooms_in_round(participants, room_size) for _ in range(rounds)]
