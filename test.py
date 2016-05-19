import unittest

from chess_challenge import get_variants, _place, main


class Tests(unittest.TestCase):

    def _rotate_premutations(self, board):
        """
        Return 4 options of the board.

        Rotated 0, 90, 180, 260 degrees.
        """
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

    def test_kings_rook(self):
        """Test from challenge."""
        variants = get_variants(3, 3, kings=2, rooks=1)
        self.assertEqual(len(variants), 4)

        board = [
            ['K', ' ', 'K'],
            [' ', ' ', ' '],
            [' ', 'R', ' '],
        ]
        for premutation in self._rotate_premutations(board):
            self.assertTrue(premutation in variants)

    def test_queen_bishop(self):
        """Test queen and bishop."""
        variants = get_variants(3, 3, queens=1, bishops=1)
        self.assertEqual(len(variants), 16)

        board = [
            ['Q', ' ', ' '],
            [' ', ' ', ' '],
            [' ', 'B', ' '],
        ]
        for premutation in self._rotate_premutations(board):
            self.assertTrue(premutation in variants)

        board = [
            ['Q', ' ', ' '],
            [' ', ' ', 'B'],
            [' ', ' ', ' '],
        ]
        for premutation in self._rotate_premutations(board):
            self.assertTrue(premutation in variants)

        board = [
            [' ', 'Q', ' '],
            [' ', ' ', ' '],
            ['B', ' ', ' '],
        ]
        for premutation in self._rotate_premutations(board):
            self.assertTrue(premutation in variants)

        board = [
            [' ', 'Q', ' '],
            [' ', ' ', ' '],
            [' ', ' ', 'B'],
        ]
        for premutation in self._rotate_premutations(board):
            self.assertTrue(premutation in variants)

    def test_rooks_knights(self):
        """Test from challenge."""
        variants = get_variants(4, 4, rooks=2, knights=4)
        self.assertEqual(len(variants), 8)

        board = [
            [' ', 'N', ' ', 'N'],
            ['R', ' ', ' ', ' '],
            [' ', 'N', ' ', 'N'],
            [' ', ' ', 'R', ' '],
        ]
        for premutation in self._rotate_premutations(board):
            self.assertTrue(premutation in variants)

        board = [
            [' ', 'N', ' ', 'N'],
            [' ', ' ', 'R', ' '],
            [' ', 'N', ' ', 'N'],
            ['R', ' ', ' ', ' '],
        ]
        for premutation in self._rotate_premutations(board):
            self.assertTrue(premutation in variants)

    def test_rotate(self):
        """Test utility rotation function."""
        initial_board = [
            ['K', ' ', 'K'],
            [' ', ' ', ' '],
            [' ', 'R', ' '],
        ]

        premuatations = self._rotate_premutations(initial_board)

        self.assertEqual(len(premuatations), 4)
        self.assertEqual(premuatations[0], initial_board)

        # rotate 90 degrees
        board_90 = [
            [' ', ' ', 'K'],
            ['R', ' ', ' '],
            [' ', ' ', 'K'],
        ]
        self.assertEqual(premuatations[1], board_90)

        # rotate 180 degrees
        board_180 = [
            [' ', 'R', ' '],
            [' ', ' ', ' '],
            ['K', ' ', 'K'],
        ]
        self.assertEqual(premuatations[2], board_180)

        # rotate 270 degrees
        board_270 = [
            ['K', ' ', ' '],
            [' ', ' ', 'R'],
            ['K', ' ', ' '],
        ]
        self.assertEqual(premuatations[3], board_270)

    def test_place_queen(self):
        """Test queen placement."""
        board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(3, 3, board, 'Q', 0, 0)
        should_be = [
            ['Q', 'x', 'x'],
            ['x', 'x', ' '],
            ['x', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'Q', 1, 0)
        should_be = [
            ['x', 'x', ' '],
            ['Q', 'x', 'x'],
            ['x', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'Q', 2, 0)
        should_be = [
            ['x', ' ', 'x'],
            ['x', 'x', ' '],
            ['Q', 'x', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'Q', 0, 1)
        should_be = [
            ['x', 'Q', 'x'],
            ['x', 'x', 'x'],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'Q', 1, 1)
        should_be = [
            ['x', 'x', 'x'],
            ['x', 'Q', 'x'],
            ['x', 'x', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'Q', 2, 1)
        should_be = [
            [' ', 'x', ' '],
            ['x', 'x', 'x'],
            ['x', 'Q', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'Q', 0, 2)
        should_be = [
            ['x', 'x', 'Q'],
            [' ', 'x', 'x'],
            ['x', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'Q', 1, 2)
        should_be = [
            [' ', 'x', 'x'],
            ['x', 'x', 'Q'],
            [' ', 'x', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'Q', 2, 2)
        should_be = [
            ['x', ' ', 'x'],
            [' ', 'x', 'x'],
            ['x', 'x', 'Q'],
        ]
        self.assertEqual(new_board, should_be)

    def test_place_bishop(self):
        """Test bishop placement."""
        board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(3, 3, board, 'B', 0, 0)
        should_be = [
            ['B', ' ', ' '],
            [' ', 'x', ' '],
            [' ', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'B', 1, 0)
        should_be = [
            [' ', 'x', ' '],
            ['B', ' ', ' '],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'B', 2, 0)
        should_be = [
            [' ', ' ', 'x'],
            [' ', 'x', ' '],
            ['B', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'B', 0, 1)
        should_be = [
            [' ', 'B', ' '],
            ['x', ' ', 'x'],
            [' ', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'B', 1, 1)
        should_be = [
            ['x', ' ', 'x'],
            [' ', 'B', ' '],
            ['x', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'B', 2, 1)
        should_be = [
            [' ', ' ', ' '],
            ['x', ' ', 'x'],
            [' ', 'B', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'B', 0, 2)
        should_be = [
            [' ', ' ', 'B'],
            [' ', 'x', ' '],
            ['x', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'B', 1, 2)
        should_be = [
            [' ', 'x', ' '],
            [' ', ' ', 'B'],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'B', 2, 2)
        should_be = [
            ['x', ' ', ' '],
            [' ', 'x', ' '],
            [' ', ' ', 'B'],
        ]
        self.assertEqual(new_board, should_be)

    def test_place_rook(self):
        """Test rook placement."""
        board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(3, 3, board, 'R', 0, 0)
        should_be = [
            ['R', 'x', 'x'],
            ['x', ' ', ' '],
            ['x', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'R', 1, 0)
        should_be = [
            ['x', ' ', ' '],
            ['R', 'x', 'x'],
            ['x', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'R', 2, 0)
        should_be = [
            ['x', ' ', ' '],
            ['x', ' ', ' '],
            ['R', 'x', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'R', 0, 1)
        should_be = [
            ['x', 'R', 'x'],
            [' ', 'x', ' '],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'R', 1, 1)
        should_be = [
            [' ', 'x', ' '],
            ['x', 'R', 'x'],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'R', 2, 1)
        should_be = [
            [' ', 'x', ' '],
            [' ', 'x', ' '],
            ['x', 'R', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'R', 0, 2)
        should_be = [
            ['x', 'x', 'R'],
            [' ', ' ', 'x'],
            [' ', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'R', 1, 2)
        should_be = [
            [' ', ' ', 'x'],
            ['x', 'x', 'R'],
            [' ', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'R', 2, 2)
        should_be = [
            [' ', ' ', 'x'],
            [' ', ' ', 'x'],
            ['x', 'x', 'R'],
        ]
        self.assertEqual(new_board, should_be)

    def test_place_king(self):
        """Test king placement."""
        board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(3, 3, board, 'K', 0, 0)
        should_be = [
            ['K', 'x', ' '],
            ['x', 'x', ' '],
            [' ', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'K', 1, 0)
        should_be = [
            ['x', 'x', ' '],
            ['K', 'x', ' '],
            ['x', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'K', 2, 0)
        should_be = [
            [' ', ' ', ' '],
            ['x', 'x', ' '],
            ['K', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'K', 0, 1)
        should_be = [
            ['x', 'K', 'x'],
            ['x', 'x', 'x'],
            [' ', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'K', 1, 1)
        should_be = [
            ['x', 'x', 'x'],
            ['x', 'K', 'x'],
            ['x', 'x', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'K', 2, 1)
        should_be = [
            [' ', ' ', ' '],
            ['x', 'x', 'x'],
            ['x', 'K', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'K', 0, 2)
        should_be = [
            [' ', 'x', 'K'],
            [' ', 'x', 'x'],
            [' ', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'K', 1, 2)
        should_be = [
            [' ', 'x', 'x'],
            [' ', 'x', 'K'],
            [' ', 'x', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'K', 2, 2)
        should_be = [
            [' ', ' ', ' '],
            [' ', 'x', 'x'],
            [' ', 'x', 'K'],
        ]
        self.assertEqual(new_board, should_be)

    def test_place_knight(self):
        """Test knight placement."""
        board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(3, 3, board, 'N', 0, 0)
        should_be = [
            ['N', ' ', ' '],
            [' ', ' ', 'x'],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'N', 1, 0)
        should_be = [
            [' ', ' ', 'x'],
            ['N', ' ', ' '],
            [' ', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'N', 2, 0)
        should_be = [
            [' ', 'x', ' '],
            [' ', ' ', 'x'],
            ['N', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'N', 0, 1)
        should_be = [
            [' ', 'N', ' '],
            [' ', ' ', ' '],
            ['x', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'N', 1, 1)
        should_be = [
            [' ', ' ', ' '],
            [' ', 'N', ' '],
            [' ', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        # Further

        new_board = _place(3, 3, board, 'N', 2, 1)
        should_be = [
            ['x', ' ', 'x'],
            [' ', ' ', ' '],
            [' ', 'N', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'N', 0, 2)
        should_be = [
            [' ', ' ', 'N'],
            ['x', ' ', ' '],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'N', 1, 2)
        should_be = [
            ['x', ' ', ' '],
            [' ', ' ', 'N'],
            ['x', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(3, 3, board, 'N', 2, 2)
        should_be = [
            [' ', 'x', ' '],
            ['x', ' ', ' '],
            [' ', ' ', 'N'],
        ]
        self.assertEqual(new_board, should_be)

    def test_place_combined(self):
        """Test multiple placement."""
        board = [
            ['K', 'x', ' '],
            ['x', 'x', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(3, 3, board, 'R', 0, 0)
        should_be = None
        self.assertEqual(new_board, should_be)

        board = [
            ['K', 'x', ' '],
            ['x', 'x', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(3, 3, board, 'R', 0, 1)
        should_be = None
        self.assertEqual(new_board, should_be)

        board = [
            ['K', 'x', ' '],
            ['x', 'x', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(3, 3, board, 'R', 0, 2)
        should_be = None
        self.assertEqual(new_board, should_be)

        board = [
            ['K', 'x', ' '],
            ['x', 'x', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(3, 3, board, 'R', 1, 2)
        should_be = [
            ['K', 'x', 'x'],
            ['x', 'x', 'R'],
            [' ', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

    def test_main(self):
        """Test main method."""
        results_len = main(3, 3, kings=2, rooks=1, full_output=True)
        self.assertEqual(results_len, 4)


if __name__ == '__main__':
    unittest.main()
