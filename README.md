# Goal
The plan is to create a playable chess game.

Currently, the idea is to create the board as matplotlib plot.

The pieces will be created as figures/patches in matplotlib.

## Logic rules
- is_check_mate: gets executed at the start of every turn. Ends game if True.
- is_king_checked: you can only make a move which breaks the check.
- is_stalemate: gets executed at the start of every turn. Runs a loop through each piece and stops as soon as it finds a possible move. If none are found, game ends.

## The board
Create it as a matplotlib figure.

The final version can have one axes for the board, one axis for each player with player name + captured pieces, and potentially one legend for all pieces.

It might be possible to "animate" the board by using an update function. See [this tutorial](https://github.com/rougier/matplotlib-tutorial/blob/master/README.rst) for more info
