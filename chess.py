""" This is the main game. """
import matplotlib.pyplot as plt
from board import Board
from positions import Positions
from interactions import request_move
from control import check_only_valid_characters
from rules import Move

BOARD = Board()
POSITIONS = Positions()
BOARD.update_board(POSITIONS.get_positions())
BOARD.show_board()

while True:
    USER_INPUT = request_move()
    MOVE = Move(USER_INPUT)
    POSITIONS.update_positions(MOVE.get_coordinates())
    BOARD.update_board(POSITIONS.get_positions(), MOVE.get_coordinates())
# Send in the coordinates of the move to the Position class. Then the positions
# just have to take whatever is at the start position and insert that at the
# end position.
"""
General game loop
- Set up player names (wait with this part for a bit)
- Set up board (happens in the Board class)
- Choose white and black (wait with this for a bit)
- Ask for move (happens in interactions.py)
- Validate move (wait with this for a bit)
- Execute move (just feed some new values into the positions and then feed the
  positions to the Board class's update_board() function)
- Check for check and check mate (wait with this)
    - No check mate, go to step "Ask for move"
    - Yes check mate, display score + end game message and ask for rematch
"""
