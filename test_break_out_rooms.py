from pathlib import Path

import pytest

from break_out_rooms import break_out_rooms, get_rooms_in_round


@pytest.fixture
def odd_participants():
    f = Path('test_participants.txt')
    return f.read_text().strip().split('\n')


@pytest.fixture
def even_participants():
    f = Path('test_participants.txt')
    return f.read_text().strip().split('\n')[:-1]


def test_get_rooms_in_round_size_2(even_participants):
    print(even_participants)
    rooms = get_rooms_in_round(even_participants, 2)
    assert len(rooms) == 5
    assert all([len(r) == 2 for r in rooms])


def test_get_rooms_in_round_size_2_odd(odd_participants):
    rooms = get_rooms_in_round(odd_participants, 2)
    assert len(rooms) == 5
    assert all([len(r) == 2 for r in rooms[:-1]])
    assert len(rooms[-1]) == 3


def test_break_out_rooms_non_deterministic(even_participants):
    rounds = break_out_rooms(2, even_participants, 2, False)
    assert len(rounds) == 2


def test_break_out_rooms_deterministic(even_participants):
    rounds = break_out_rooms(2, even_participants, 2, True)
    assert len(rounds) == 2
    round1, round2 = rounds
    assert all([room1 == room2 for room1, room2 in zip(round1, round2)])
