""" This is the main game. """
import classes
import control
import interactions

BOARD = classes.Board()
POSITIONS = classes.Positions()
BOARD.update_board(POSITIONS.get_positions())
BOARD.show_board()

print(
    '--------------------------------------------------------------------\n' +
    '|              Welcome to "Check yourself, mate!"                  |\n' +
    '--------------------------------------------------------------------\n' +
    '\nTo play you simply take turns entering your moves according to\n' +
    'the format <start position><end position>, for example  "E2E4"\n' +
    'would move the piece from E2 to the square E4.\n\n'
)
NAMES = interactions.request_player_name()

PLAYERS = []
# Set player names
for name in NAMES:
    PLAYERS.append(classes.Player(name))

# Assign teams. Happens just before starting each the game loop.
SECOND_TEAM = PLAYERS[0].assign_first_team()
PLAYERS[1].assign_second_team(SECOND_TEAM)
QUEUE = classes.player_queue(PLAYERS)

# Start play loop
GAME_STATUS = True
LAST_MOVE = ['', '']
EN_PASSANT_POSITION = ['', '']
while GAME_STATUS:
    CURRENT_PLAYER = next(QUEUE)
    USER_INPUT = interactions.request_move(CURRENT_PLAYER)
    while not control.check_only_valid_characters(USER_INPUT):
        print(
            'That\'s not a valid move. It needs to follow the pattern ' +
            '"E2E4". Please try again'
        )
        USER_INPUT = interactions.request_move(CURRENT_PLAYER)
    # Check whether there is a check that needs to be broken
    # Check that there are no obstacles (except for knights) Check that the
    # destination is not occupied by the same team Check that move pattern
    # conforms to the piece's move set
    MOVE = classes.Move(USER_INPUT)
    # x is the column and y is the row in the coordinate system
    MOVE_DETAILS = POSITIONS.check_positions(MOVE)
    # TODO check if moved piece == "pawn" and the end position is the
    # en-passant position. Then execute special logic: remove previously moved
    # pawn and place new pawn on the desired square.
    verification = False
    while not verification:
        BASIC_CHECK = control.check_team_and_capture(
                CURRENT_PLAYER.team,
                MOVE_DETAILS['piece_start'].team,
                MOVE_DETAILS['piece_end'],
                )
        # TODO implement an en_passant function
        EN_PASSANT = control.check_en_passant(
                MOVE_DETAILS['piece_start'].type,
                MOVE.end.get_coordinates(),
                EN_PASSANT_POSITION
                )
        NORMAL_MOVE = MOVE_DETAILS['piece_start'].verify_move(
                move=MOVE,
                captured_piece=MOVE_DETAILS['piece_end']
                )

        if BASIC_CHECK and (EN_PASSANT or NORMAL_MOVE):
            verification = True
        else:
            print('Sorry, this piece can\'t be moved like that.'
                  ' Please try again.')
            USER_INPUT = interactions.request_move(CURRENT_PLAYER)
            MOVE = classes.Move(USER_INPUT)
            MOVE_DETAILS = POSITIONS.check_positions(MOVE.get_coordinates())
    # TODO implement update_en_passant_position()
    if EN_PASSANT:
        CAPTURED_PIECE = POSITIONS.en_passant_capture(LAST_MOVE)
    else:
        CAPTURED_PIECE = MOVE_DETAILS['piece_end']
    EN_PASSANT_POSITION = control.update_en_passant_position(
            MOVE_DETAILS['piece_start'].type,
            MOVE
            )
    LAST_MOVE = POSITIONS.update_positions(MOVE)
    BOARD.update_board(POSITIONS.get_positions(), MOVE.get_coordinates())
    if CAPTURED_PIECE != '':
        print(f'{CURRENT_PLAYER} captured: {CAPTURED_PIECE}.')
    print('')
    """ If last moved piece was pawn and move length was 2, save the position
    for the en-passant take """
    # TODO check if the MOVE_DETAILS['piece_end'] is not null. Then print a
    # text with CURRENT_PLAYER and the captured piece.
    """
    General game loop
    - Set up player names (wait with this part for a bit)
    - Set up board (happens in the Board class)
    - Choose white and black (wait with this for a bit)
    - Ask for move (happens in interactions.py)
    - Validate move (wait with this for a bit)
    - Execute move (just feed some new values into the positions and then feed
    the
      positions to the Board class's update_board() function)
    - Check for check and check mate (wait with this)
        - No check mate, go to step "Ask for move"
        - Yes check mate, display score + end game message and ask for rematch
    """
