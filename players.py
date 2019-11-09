""" This module contains the player class. """
from numpy.random import randint
from typing import List, Generator


class Player:
    """ The class is used to keep track of name, team and the points in the
    game. """
    teams = ['white', 'black']

    def __init__(self, name: str):
        self.name = name
        self.team = ''
        self.points = 0

    def assign_first_team(self):
        """ Randomly assigns a team to the player and returns the other colour,
        to be assigned to the other player. """
        idx = randint(2, size=1)[0]
        team = Player.teams[idx]
        self.team = team

        return Player.teams[idx - 1]

    def assign_second_team(self, team: str):
        """ Assigns the provided team as the player's team. The team of the
        first player is generated with the function Player.assign_first_team.
        """
        self.team = team

    def add_points(self, points: int) -> int:
        """ Add points after a piece has been captured. Returns current points.
        """
        self.points += points

        return self.points

    def __repr__(self):
        """ The class is described with the player name. """

        return self.name


def player_queue(players: List[Player]) -> Generator[Player, None, None]:
    """ Orders the players with the white team first and then creates an
    infinite queue. """
    for player in players:
        if player.team == 'white':
            first_player = player
        else:
            second_player = player
    queue = ['', first_player, second_player]
    i = 1
    while True:
        yield queue[i]
        i = i * -1
