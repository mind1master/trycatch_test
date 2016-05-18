import time

CACHE = set()


def board_key(board):
    '''
    Returns a single string with all elements of the board.
    Used to store the board in set.
    '''
    elements = []
    for row in board:
        elements += row
    return ''.join(elements)


def _place(M, N, board, figure, i, j):
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
    if not figures_left:
        # return
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
    figure = figures_left[0]

    i = 0
    while i < M:
        j = 0
        while j < N:
            if board[i][j] != ' ':
                j += 1
                continue
            new_board = _place(M, N, board, figure, i, j)
            j += 1
            if not new_board:
                continue

            key = board_key(new_board)
            if key in CACHE:
                # aleady had it
                continue
            CACHE.add(key)

            results += _reccur(
                M, N,
                new_board,
                figures_left[1:]
            )
        i += 1


    return results


def get_variants(M, N, kings=0, queens=0, bishops=0, rooks=0, knights=0):
    '''
    Solves the given task.
    Returns a list of boards.
    '''
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

    results = _reccur(M, N, board, figures)

    return results


if __name__ == '__main__':
    # TODO: add proper input/output
    start_t = time.time()
    variants = get_variants(7, 7, kings=2, queens=2, bishops=2, knights=1)
    print(
        'Got {} variants in {} secs'.format(
            len(variants), time.time() - start_t
        )
    )
