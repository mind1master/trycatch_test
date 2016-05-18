import time

CACHE = set()


def rotate_premutations(board):
    '''
    Returns 4 options of the board rotated 0, 90, 180, 260 degrees.
    '''
    results = [board]

    # turn 90 degrees each time
    for _ in range(3):
        last_board = results[-1]
        new_board = []
        # j is a column index
        for j in range(len(last_board[0])):
            col = []  # column
            # i is row index
            for i in range(len(last_board)):
                col.append(last_board[i][j])

            # for 90 degrees turned board
            # column becomes a reversed row, so just append
            new_board.append(list(reversed(col)))

        results.append(new_board)

    return results


def board_key(board):
    '''
    Returns a single string with all elements of the board.
    Used to store the board in set.
    '''
    elements = []
    for row in board:
        elements += row
    return ''.join(elements)


# def _copy_board(old_board, new_board):
#     '''
#     Copies data from old_board to new_board
#     '''
#     for i in range(len(old_board)):
#         for j in range(len(old_board)):
#             new_board[i][j] = old_board[i][j]
#     return new_board


def _place(board, figure, i, j):
    if board[i][j] != ' ':
        # if cell is not empty
        return None

    new_board = []
    # copy
    for row in board:
        new_board.append(row[:])

    height = len(board)
    width = len(board[0])
    valid_placement = True
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
        # straights
        for y in range(height):
            consider.append((y, j))
        for x in range(width):
            consider.append((i, x))
        # diagonals
        for k in range(min(width, height)):
            consider.append((i-k, j-k))
        for k in range(min(width, height)):
            consider.append((i+k, j+k))
        for k in range(min(width, height)):
            consider.append((i-k, j+k))
        for k in range(min(width, height)):
            consider.append((i+k, j-k))
    elif figure == 'R':
        # rook
        # straights
        for y in range(height):
            consider.append((y, j))
        for x in range(width):
            consider.append((i, x))
    elif figure == 'B':
        # bishop
        # it goes out of bounds on purpose
        # such points are discarded later
        # diagonals
        for k in range(min(width, height)):
            consider.append((i-k, j-k))
        for k in range(min(width, height)):
            consider.append((i+k, j+k))
        for k in range(min(width, height)):
            consider.append((i-k, j+k))
        for k in range(min(width, height)):
            consider.append((i+k, j-k))
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

    # check all cells that would be influenced
    for y, x in consider:
        if y < 0 or y >= height or x < 0 or x >= width:
            # out of bounds
            continue
        if not board[y][x] in [' ', 'x']:
            # cell is taken means we can't use (i,j)
            valid_placement = False
            break

        new_board[y][x] = 'x'  # mark as theatened

    if not valid_placement:
        return None

    new_board[i][j] = figure
    return new_board


# def _reccur(board, figures_left):
#     if not figures_left:
#         ret_board = []
#         for row in board:
#             ret_row = []
#             for el in row:
#                 if el in [' ', 'x']:
#                     ret_row.append(' ')
#                 else:
#                     ret_row.append(el)
#             ret_board.append(ret_row)
#         return [ret_board]

#     m = len(board)
#     n = len(board[0])

#     results = []
#     figure = figures_left[0]

#     for i in range(m):
#         for j in range(n):
#             if board[i][j] != ' ':
#                 continue
#             new_board = _place(board, figure, i, j)
#             if not new_board:
#                 continue

#             if board_key(new_board) in CACHE:
#                 # aleady had it
#                 continue
#             CACHE.add(board_key(new_board))

#             results += _reccur(
#                 new_board,
#                 figures_left[1:]
#             )

#     return results


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

    cache = set()
    results = []
    # each element of stack is
    # {
    #     'board' # board BEFORE puting figure
    #     'new board'  # board AFTER puting figure, is changed with (i,changes)
    #     'figures': ...  # first one will be placed at this stack level
    #     'i', 'j'  # coordinates where figure is placed
    # }
    stack = [{
        'board': board,
        'new_board': None,
        'figures': figures,
        'i': 0,
        'j': 0,
    }]


    smaller_side = min(M, N)
    while stack:
        current_frame = stack[-1]

        if current_frame['i'] == M and current_frame['j'] == 0:
            # current board with current figure is completely done
            # go one frame up and try other position for prev figure
            del stack[-1]
            continue

        i, j = current_frame['i'], current_frame['j']
        figure = current_frame['figures'][0]
        current_frame['j'] += 1  # go to next cell next time
        # bound check
        if current_frame['j'] == N:
            # go to next row
            current_frame['j'] = 0
            current_frame['i'] += 1

        # start placing
        # there was a function call, but it was too slow

        if current_frame['board'][i][j] != ' ':
            # occupied
            continue

        consider = []
        if figure == 'K':
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
            # straights
            for y in range(M):
                consider.append((y, j))
            for x in range(N):
                consider.append((i, x))
            # diagonals
            for k in range(smaller_side):
                consider.append((i-k, j-k))
            for k in range(smaller_side):
                consider.append((i+k, j+k))
            for k in range(smaller_side):
                consider.append((i-k, j+k))
            for k in range(smaller_side):
                consider.append((i+k, j-k))
        elif figure == 'R':
            # rook
            # straights
            for y in range(M):
                consider.append((y, j))
            for x in range(N):
                consider.append((i, x))
        elif figure == 'B':
            # bishop
            # it goes out of bounds on purpose
            # such points are discarded later
            # diagonals
            for k in range(smaller_side):
                consider.append((i-k, j-k))
            for k in range(smaller_side):
                consider.append((i+k, j+k))
            for k in range(smaller_side):
                consider.append((i-k, j+k))
            for k in range(smaller_side):
                consider.append((i+k, j-k))
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
                # out of bounds
                continue
            if not current_frame['board'][y][x] in [' ', 'x']:
                # cell is taken means we can't use (i,j)
                valid_placement = False
                break

        if not valid_placement:
            continue

        # placement is good

        # copy board
        current_frame['new_board'] = []
        for row in current_frame['board']:
            current_frame['new_board'].append(row[:])

        # fill new_board
        for y, x in consider:
            if y < 0 or y >= M or x < 0 or x >= N:
                # out of bounds
                continue

            current_frame['new_board'][y][x] = 'x'  # mark as theatened

        current_frame['new_board'][i][j] = figure
        # end of placing


        key = board_key(current_frame['new_board'])
        if key in cache:
            # already had such board
            continue
        cache.add(key)


        if len(current_frame['figures']) == 1:
            # we have just placed the last figure
            # meaning this is one of the results
            results.append(current_frame['new_board'])
            continue

        # have more figure to consider
        # add new stack frame
        new_frame = {
            'board': current_frame['new_board'],
            'new_board': None,
            'figures': current_frame['figures'][1:],
            'i': 0,
            'j': 0,
        }
        stack.append(new_frame)


    # clean 'x' symbols
    for board in results:
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'x':
                    board[i][j] = ' '

    return results


if __name__ == '__main__':
    # TODO: add proper input/output
    start_t = time.time()
    # variants = get_variants(7, 7, kings=2, queens=2, bishops=2, knights=1)
    variants = get_variants(7, 7, kings=2, queens=2)
    print(
        'Got {} variants in {} secs'.format(
            len(variants), time.time() - start_t
        )
    )
