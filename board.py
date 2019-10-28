import numpy as np
import matplotlib.pyplot as plt


def draw_board():
    # 0 is white
    board = []
    for value in range(1, 9):

        if value % 2 == 0:
            row = [0, 1] * 4
        else:
            row = [1, 0] * 4
        board.append(row)

    fig = plt.figure(figsize=(4, 4), dpi=150)
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

    # Remove labels
    ax_board.tick_params(
        axis='both',
        which='both',
        bottom=False,
        top=False,
        left=False,
        right=False
    )

    # Fixing columns
    X = np.arange(1.5, 9.5)
    Y = np.zeros(8)

    ax_cols.set_xticks([])
    ax_cols.set_yticks([])
    ax_cols.tick_params(
        axis='both',
        which='both',
        bottom=False,
        top=False,
        left=False,
        right=False
    )

    i = 0
    labels = 'abcdefgh'
    for x, y in zip(X, Y):
        ax_cols.text(x, y, labels[i], ha='center', va='bottom', fontsize=8)
        i += 1
    ax_cols.set_xlim(1, 9)
    ax_cols.set_ylim(bottom=0, top=2)
    ax_cols.spines['right'].set_color('none')
    ax_cols.spines['left'].set_color('none')
    ax_cols.spines['top'].set_color('none')
    ax_cols.spines['bottom'].set_color('none')

    # Fixing rows
    Y = np.arange(1.5, 9)
    X = np.zeros(8)

    ax_rows.set_xticks([])
    ax_rows.set_yticks([])
    ax_rows.tick_params(
        axis='both',
        which='both',
        bottom=False,
        top=False,
        left=False,
        right=False
    )

    i = 0
    labels = '123456789'
    for x, y in zip(X, Y):
        ax_rows.text(x, y, labels[i], ha='center', va='center', fontsize=8)
        i += 1
    ax_rows.set_xlim(-1, 1)
    ax_rows.set_ylim(bottom=1.1, top=9.1)
    ax_rows.spines['right'].set_color('none')
    ax_rows.spines['left'].set_color('none')
    ax_rows.spines['top'].set_color('none')
    ax_rows.spines['bottom'].set_color('none')

    plt.tight_layout()
    fig.suptitle('Chess')

    plt.show()


draw_board()
