import numpy as np
import matplotlib.pyplot as plt
import pieces


class Board:
    def __init__(self):
        self.positions = [
                [
                    pieces.Tower('white'),
                    pieces.Knight('white'),
                    pieces.Bishop('white'),
                    pieces.Queen('white'),
                    pieces.King('white'),
                    pieces.Bishop('white'),
                    pieces.Knight('white'),
                    pieces.Tower('white'),
                ],
                [
                    pieces.Pawn('white'),
                    pieces.Pawn('white'),
                    pieces.Pawn('white'),
                    pieces.Pawn('white'),
                    pieces.Pawn('white'),
                    pieces.Pawn('white'),
                    pieces.Pawn('white'),
                    pieces.Pawn('white'),
                ],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                ['', '', '', '', '', '', '', ''],
                [
                    pieces.Pawn('black'),
                    pieces.Pawn('black'),
                    pieces.Pawn('black'),
                    pieces.Pawn('black'),
                    pieces.Pawn('black'),
                    pieces.Pawn('black'),
                    pieces.Pawn('black'),
                    pieces.Pawn('black'),
                ],
                [
                    pieces.Tower('black'),
                    pieces.Knight('black'),
                    pieces.Bishop('black'),
                    pieces.Queen('black'),
                    pieces.King('black'),
                    pieces.Bishop('black'),
                    pieces.Knight('black'),
                    pieces.Tower('black'),
                ],
            ]

    def draw_board(self) -> plt.Figure:
        """ Draws the main board and its coordinates in a figure and shows
        it """
        # 0 is white
        board = []
        for value in range(1, 9):

            if value % 2 == 0:
                row = [0, 1] * 4
            else:
                row = [1, 0] * 4
            board.append(row)

        fig = plt.figure(figsize=(4, 4), dpi=150)
        # Using gridspec to be able to control the layout of the two axes that
        # hold coordinates.
        gs = plt.GridSpec(
            nrows=2,
            ncols=2,
            figure=fig,
            width_ratios=[0.1, 0.9],
            height_ratios=[0.1, 0.9],
            wspace=0.03,
            hspace=0.03
        )
        ax_cols = fig.add_subplot(gs[0, 1])
        ax_rows = fig.add_subplot(gs[1, 0])
        ax_board = fig.add_subplot(gs[1, 1])

        # Setting up main board
        ax_board.matshow(board, cmap='Greys')
        ax_board.set_xticks([])
        ax_board.set_yticks([])

        # Making sure the first and last squares are fully visible
        ax_board.set_ylim(bottom=-0.5, top=7.5)

        # Fixing columns
        X = np.arange(1.5, 9.5)
        Y = np.zeros(8)

        ax_cols.set_xticks([])
        ax_cols.set_yticks([])

        i = 0
        labels = 'abcdefgh'
        for x, y in zip(X, Y):
            ax_cols.text(x, y, labels[i], ha='center', va='bottom', fontsize=8)
            i += 1
        ax_cols.set_xlim(1, 9)
        ax_cols.set_ylim(bottom=0, top=2)

        # Fixing rows
        Y = np.arange(1.5, 9)
        X = np.zeros(8)

        i = 0
        labels = '123456789'
        for x, y in zip(X, Y):
            ax_rows.text(x, y, labels[i], ha='center', va='center', fontsize=8)
            i += 1
        ax_rows.set_xlim(-1, 1)
        ax_rows.set_ylim(bottom=1.1, top=9.1)

        def _remove_ax_elements(
                ax: plt.Axes,
                ticks: bool,
                spines: bool) -> plt.Axes:
            """ Removes x and y tick marks as well as all spines. """
            if ticks:
                ax.set_xticks([])
                ax.set_yticks([])
                ax.tick_params(
                    axis='both',
                    which='both',
                    bottom=False,
                    top=False,
                    left=False,
                    right=False
                )

            if spines:
                ax.spines['right'].set_color('none')
                ax.spines['left'].set_color('none')
                ax.spines['top'].set_color('none')
                ax.spines['bottom'].set_color('none')

            return ax

        ax_rows = _remove_ax_elements(ax_rows, True, True)
        ax_cols = _remove_ax_elements(ax_cols, True, True)
        ax_board = _remove_ax_elements(ax_board, True, False)
        fig.suptitle('Chess')

        # Placing pieces
        for y, row in enumerate(self.positions):

            for x, piece in enumerate(row):

                if piece != '':
                    ax_board.scatter(x, y, marker=piece.marker, c=piece.color,
                                     s=piece.size, label=piece.type)

        plt.show()


board = Board()
board.draw_board()
