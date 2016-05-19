"""Module to solve chess challenge."""

import time
import sys


# support python 2 and 3
if sys.version[0] == "3":
    raw_input = input


CACHE = set()


def _board_key(board):
    """
    Used to store the board in set.

    Return a single string with all elements of the board.
    (board itself is mutable so can't be stored in set)
    """
    elements = []
    for row in board:
        elements += row
    return ''.join(elements)


def _place(M, N, board, figure, i, j):
    """
    Place a `figure` at position i,j.

    Return a new board or None if placement is not allowed.
    """
    if board[i][j] != ' ':
        # if cell is not empty
        return None

    # (i,j) of cells that can be theatened and should be checked
    consider = []

    if figure == 'K':
        # king
        consider = [
            (i+1, j),
            (i-1, j),
            (i, j+1),
            (i, j-1),
            (i+1, j+1),
            (i-1, j+1),
            (i+1, j-1),
            (i-1, j-1),
        ]
    elif figure == 'Q':
        # queen
        # it goes out of bounds on purpose
        # such points are discarded later

        m = min(M, N)
        consider = [0] * (m * 4 + M + N)

        # straights
        y, x = 0, 0
        while y < M:
            consider[y] = (y, j)
            y += 1
        while x < N:
            consider[M+x] = (i, x)
            x += 1

        # diagonals
        k = 0
        while k < m:
            consider[M + N + k*4] = (i-k, j-k)
            consider[M + N + k*4 + 1] = (i+k, j+k)
            consider[M + N + k*4 + 2] = (i-k, j+k)
            consider[M + N + k*4 + 3] = (i+k, j-k)
            k += 1
    elif figure == 'R':
        # rook
        # preallocate
        consider = [0] * (M + N)
        # straights
        y, x = 0, 0
        while y < M:
            consider[y] = (y, j)
            y += 1
        while x < N:
            consider[M+x] = (i, x)
            x += 1
    elif figure == 'B':
        # bishop
        # diagonals
        # preallocate
        m = min(M, N)
        consider = [0] * (m * 4)

        k = 0
        while k < m:
            consider[k*4] = (i-k, j-k)
            consider[k*4 + 1] = (i+k, j+k)
            consider[k*4 + 2] = (i-k, j+k)
            consider[k*4 + 3] = (i+k, j-k)
            k += 1

    elif figure == 'N':
        # knight
        consider = [
            (i-2, j-1),
            (i-1, j-2),
            (i+2, j+1),
            (i+1, j+2),
            (i-2, j+1),
            (i-1, j+2),
            (i+2, j-1),
            (i+1, j-2),
        ]

    valid_placement = True
    # check all cells that would be influenced
    for y, x in consider:
        if y < 0 or y >= M or x < 0 or x >= N:
            # out of bounds, don't care
            continue
        if board[y][x] not in [' ', 'x']:
            # cell is taken means we can't use (i,j)
            valid_placement = False
            break

    if not valid_placement:
        return None

    new_board = [0] * M
    # copy
    row = 0
    while row < M:
        new_board[row] = board[row][:]
        row += 1

    # fill the new board
    for y, x in consider:
        if y < 0 or y >= M or x < 0 or x >= N:
            # out of bounds
            continue
        new_board[y][x] = 'x'  # mark as theatened

    new_board[i][j] = figure
    return new_board


def _reccur(M, N, board, figures_left):
    """
    Called recursively and puts one figure at each recursion level.

    Each next call has smaller figures_left then it's caller.
    Returns the final results for given (semi)populated board and figures.
    """
    if not figures_left:
        # all figures are placed, means we have a final variant
        # replace `x` with spaces
        i = 0
        while i < M:
            j = 0
            while j < N:
                if board[i][j] == 'x':
                    board[i][j] = ' '
                j += 1
            i += 1
        return [board]

    results = []
    # take first figure from set
    # we will try to put it somewhere
    figure = figures_left[0]

    i = 0
    # iterate over a board
    while i < M:
        j = 0
        while j < N:
            # check if vacant
            if board[i][j] != ' ':
                j += 1
                continue
            # try place the figure
            new_board = _place(M, N, board, figure, i, j)
            j += 1
            # check if placement was valid
            if not new_board:
                continue

            # check cache to reduce solution space
            key = _board_key(new_board)
            if key in CACHE:
                # aleady had this board configuration
                continue
            CACHE.add(key)

            # go to the next recursion level
            # there, the next figure will be attempted to be placed
            # and so on
            results += _reccur(
                M, N,
                new_board,
                figures_left[1:]
            )
        i += 1

    return results


def get_variants(M, N, kings=0, queens=0, bishops=0, rooks=0, knights=0):
    """
    Solve the given task.

    Returns a list of boards.
    """
    # construct board
    board = []
    for _ in range(M):
        board.append([' '] * N)

    # put together figures
    figures = []
    figures += ['Q'] * queens
    figures += ['B'] * bishops
    figures += ['R'] * rooks
    figures += ['K'] * kings
    figures += ['N'] * knights

    # start recursion
    results = _reccur(M, N, board, figures)

    return results


def main():
    """Interface to the command line."""
    M = int(raw_input('Enter M: '))
    assert M > 0, 'M must be positive'
    N = int(raw_input('Enter N: '))
    assert N > 0, 'N must be positive'
    kings = int(raw_input('Enter kings number: '))
    assert kings >= 0, 'kings number must be not negative'
    queens = int(raw_input('Enter queens number: '))
    assert queens >= 0, 'queens number must be not negative'
    bishops = int(raw_input('Enter bishops number: '))
    assert bishops >= 0, 'bishops number must be not negative'
    rooks = int(raw_input('Enter rooks number: '))
    assert rooks >= 0, 'rooks number must be not negative'
    knights = int(raw_input('Enter knights number: '))
    assert knights >= 0, 'knights number must be not negative'

    full_output = raw_input('Do you want all variants in the output? (y/n): ')
    assert full_output in ['y', 'n'], 'only `y` or `n`'

    start_t = time.time()
    variants = get_variants(M, N, kings, queens, bishops, rooks, knights)
    if full_output == 'y':
        for i, board in enumerate(variants):
            print('Board {}'.format(i))
            for row in board:
                print(row)

            print(' ')
    print(
        'Got {} variants in {} secs'.format(
            len(variants), time.time() - start_t
        )
    )

if __name__ == '__main__':
    main()
