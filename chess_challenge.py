"""Module to solve chess challenge."""

import time
import argparse


class Piece:
    """Base class for all pieces."""

    symbol = ''
    _positions = []  # to avoid re-allocations

    def affected_positions(self, M, N, i, j):
        """
        Method to get affected positions if pieced placed at (i, j).

        Should return list of (y, x) affected positions.
        """
        raise NotImplementedError


class King(Piece):
    """King"""

    symbol = 'K'

    def affected_positions(self, M, N, i, j):
        self._positions = [
            (i+1, j),
            (i-1, j),
            (i, j+1),
            (i, j-1),
            (i+1, j+1),
            (i-1, j+1),
            (i+1, j-1),
            (i-1, j-1),
        ]

        return self._positions


class Queen(Piece):
    """Queen"""

    symbol = 'Q'

    def affected_positions(self, M, N, i, j):
        # it goes out of bounds on purpose
        # such points are discarded later

        smaller_side = min(M, N)
        if not self._positions:
            self._positions = [0] * (smaller_side * 4 + M + N)

        # straights
        for y in range(M):
            self._positions[y] = (y, j)
        for x in range(N):
            self._positions[M+x] = (i, x)

        # diagonals
        for k in range(smaller_side):
            self._positions[M + N + k*4] = (i-k, j-k)
            self._positions[M + N + k*4 + 1] = (i+k, j+k)
            self._positions[M + N + k*4 + 2] = (i-k, j+k)
            self._positions[M + N + k*4 + 3] = (i+k, j-k)

        return self._positions


class Rook(Piece):
    """Rook"""

    symbol = 'R'

    def affected_positions(self, M, N, i, j):
        # it goes out of bounds on purpose
        # such points are discarded later

        if not self._positions:
            self._positions = [0] * (M + N)

        # straights
        for y in range(M):
            self._positions[y] = (y, j)
        for x in range(N):
            self._positions[M+x] = (i, x)

        return self._positions


class Bishop(Piece):
    """Bishop"""

    symbol = 'B'

    def affected_positions(self, M, N, i, j):
        # it goes out of bounds on purpose
        # such points are discarded later

        smaller_side = min(M, N)
        if not self._positions:
            self._positions = [0] * (smaller_side * 4)

        # diagonals
        for k in range(smaller_side):
            self._positions[k*4] = (i-k, j-k)
            self._positions[k*4 + 1] = (i+k, j+k)
            self._positions[k*4 + 2] = (i-k, j+k)
            self._positions[k*4 + 3] = (i+k, j-k)

        return self._positions


class Knight(Piece):
    """Knight"""

    symbol = 'N'

    def affected_positions(self, M, N, i, j):
        self._positions = [
            (i-2, j-1),
            (i-1, j-2),
            (i+2, j+1),
            (i+1, j+2),
            (i-2, j+1),
            (i-1, j+2),
            (i+2, j-1),
            (i+1, j-2),
        ]
        return self._positions


class Board:
    """Game board"""

    def __init__(self, M, N):
        """Init an empty MxN board."""
        self.M = M
        self.N = N
        self._board = [0] * M
        for i in range(M):
            self._board[i] = [' '] * N

        self._key = None

    @property
    def key(self):
        """
        Used to store the board in set.

        Return a single string with all elements of the board.
        (board itself is mutable so can't be stored in set)
        """
        if not self._key:
            elements = []
            for row in self._board:
                elements += row
            self._key = ''.join(elements)
        return self._key

    def set(self, i, j, value):
        self._board[i][j] = value

    def place(self, piece, i, j):
        """
        Try to place a piece at (i,j).

        Should return new board or None, if placement is not valid.
        """
        if self._board[i][j] != ' ':
            # if cell is not empty
            return None

        # get all cells that would be affected
        affected = piece.affected_positions(self.M, self.N, i, j)

        # filter out-of-bounds
        affected = [
            (y, x)
            for (y, x) in affected
            if y >= 0 and y < self.M and x >= 0 and x < self.N
        ]

        valid_placement = True

        for y, x in affected:
            # check if empty
            if self._board[y][x] not in [' ', 'x']:
                # cell is taken means we can't use (i,j)
                valid_placement = False
                break

        if not valid_placement:
            return None

        new_board = Board(self.M, self.N)
        for y in range(self.M):
            for x in range(self.N):
                if (y, x) in affected:
                    new_board.set(y, x, 'x')
                else:
                    new_board.set(y, x, self._board[y][x])

        new_board.set(i, j, piece.symbol)

        return new_board

    def is_empty(self, i, j):
        """Check if position is empty"""
        return self._board[i][j] == ' '

    def as_list(self):
        """Board as a list with 'x' removed."""
        for i in range(self.M):
            for j in range(self.N):
                if self._board[i][j] == 'x':
                    self._board[i][j] = ' '
        return self._board


def _reccur(M, N, board, pieces_left, cache):
    """
    Called recursively and puts one piece at each recursion level.

    Each next call has smaller pieces_left then it's caller.
    Returns the final results for given (semi)populated board and pieces.
    """
    if not pieces_left:
        # all pieces are placed, means we have a final variant
        # replace `x` with spaces
        return [board.as_list()]

    results = []
    # take first piece from set
    # we will try to put it somewhere
    piece = pieces_left[0]

    # iterate over a board
    for i in range(M):
        for j in range(N):
            # check if vacant
            if not board.is_empty(i, j):
                continue

            # try place the piece
            new_board = board.place(piece, i, j)

            # check if placement was valid
            if not new_board:
                continue

            # check cache to reduce solution space
            if new_board.key in cache:
                # aleady had this board configuration
                continue
            cache.add(new_board.key)

            # go to the next recursion level
            # there, the next piece will be attempted to be placed
            # and so on
            results += _reccur(
                M, N,
                new_board,
                pieces_left[1:],
                cache
            )

    return results


def get_variants(M, N, kings=0, queens=0, bishops=0, rooks=0, knights=0):
    """
    Solve the given task.

    Returns a list of boards.
    """
    cache = set()
    # construct board
    board = Board(M, N)

    # put together pieces
    pieces = []
    pieces += [Queen() for _ in range(queens)]
    pieces += [Bishop() for _ in range(bishops)]
    pieces += [Rook() for _ in range(rooks)]
    pieces += [King() for _ in range(kings)]
    pieces += [Knight() for _ in range(knights)]

    # start recursion
    results = _reccur(M, N, board, pieces, cache)

    return results


def main(M, N, kings=0, queens=0, bishops=0, rooks=0, knights=0,
         full_output=True):
    """Interface to the command line."""
    start_t = time.time()
    variants = get_variants(M, N, kings, queens, bishops, rooks, knights)
    if full_output:
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
    return len(variants)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chess challenge.')
    parser.add_argument('M', type=int)
    parser.add_argument('N', type=int)
    parser.add_argument('kings', type=int)
    parser.add_argument('queens', type=int)
    parser.add_argument('bishops', type=int)
    parser.add_argument('rooks', type=int)
    parser.add_argument('knights', type=int)
    parser.add_argument('--compact', action="store_true")
    args = parser.parse_args()
    main(
        args.M, args.N, args.kings, args.queens, args.bishops,
        args.rooks, args.knights, not args.compact
    )
