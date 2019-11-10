""" This module acts as the input/output interface for the players. """
from typing import List
from classes import Player


def request_player_name() -> List[str]:
    """ Asks for two player names and returns them as a list. """
    print('Who\'s playing?\n')
    names = []

    for i in range(2):
        name = input(f'Name of Player {i + 1}: ')
        names.append(name)

    return names


def request_move(player: Player, *args):
    """ Asks the user for input in order to make a move. """
    print(f'{player.team.title()} to move.')
    if len(args) == 0:
        move = input(f'{player}, please enter your move: ')
    else:
        move = args[0]

    return move.lower().strip()
