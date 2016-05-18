import unittest

from chess_challenge import get_variants, rotate_premutations, _place


class Tests(unittest.TestCase):

    def test_basic(self):
        variants = get_variants(3, 3, kings=2, rooks=1)
        self.assertEqual(len(variants), 4)

        board = [
            ['K', ' ', 'K'],
            [' ', ' ', ' '],
            [' ', 'R', ' '],
        ]
        for premutation in rotate_premutations(board):
            self.assertTrue(premutation in variants)

    def test_bigger(self):
        variants = get_variants(4, 4, rooks=2, knights=4)
        self.assertEqual(len(variants), 8)

        board = [
            [' ', 'N', ' ', 'N'],
            ['R', ' ', ' ', ' '],
            [' ', 'N', ' ', 'N'],
            [' ', ' ', 'R', ' '],
        ]
        for premutation in rotate_premutations(board):
            self.assertTrue(premutation in variants)

        board = [
            [' ', 'N', ' ', 'N'],
            [' ', ' ', 'R', ' '],
            [' ', 'N', ' ', 'N'],
            ['R', ' ', ' ', ' '],
        ]
        for premutation in rotate_premutations(board):
            self.assertTrue(premutation in variants)

    def test_rotate(self):
        initial_board = [
            ['K', ' ', 'K'],
            [' ', ' ', ' '],
            [' ', 'R', ' '],
        ]

        premuatations = rotate_premutations(initial_board)

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

    def test_place_Q(self):
        board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(board, 'Q', 0, 0)
        should_be = [
            ['Q', 'x', 'x'],
            ['x', 'x', ' '],
            ['x', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'Q', 1, 0)
        should_be = [
            ['x', 'x', ' '],
            ['Q', 'x', 'x'],
            ['x', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'Q', 2, 0)
        should_be = [
            ['x', ' ', 'x'],
            ['x', 'x', ' '],
            ['Q', 'x', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'Q', 0, 1)
        should_be = [
            ['x', 'Q', 'x'],
            ['x', 'x', 'x'],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'Q', 1, 1)
        should_be = [
            ['x', 'x', 'x'],
            ['x', 'Q', 'x'],
            ['x', 'x', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'Q', 2, 1)
        should_be = [
            [' ', 'x', ' '],
            ['x', 'x', 'x'],
            ['x', 'Q', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'Q', 0, 2)
        should_be = [
            ['x', 'x', 'Q'],
            [' ', 'x', 'x'],
            ['x', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'Q', 1, 2)
        should_be = [
            [' ', 'x', 'x'],
            ['x', 'x', 'Q'],
            [' ', 'x', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'Q', 2, 2)
        should_be = [
            ['x', ' ', 'x'],
            [' ', 'x', 'x'],
            ['x', 'x', 'Q'],
        ]
        self.assertEqual(new_board, should_be)

    def test_place_B(self):
        board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(board, 'B', 0, 0)
        should_be = [
            ['B', ' ', ' '],
            [' ', 'x', ' '],
            [' ', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'B', 1, 0)
        should_be = [
            [' ', 'x', ' '],
            ['B', ' ', ' '],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'B', 2, 0)
        should_be = [
            [' ', ' ', 'x'],
            [' ', 'x', ' '],
            ['B', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'B', 0, 1)
        should_be = [
            [' ', 'B', ' '],
            ['x', ' ', 'x'],
            [' ', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'B', 1, 1)
        should_be = [
            ['x', ' ', 'x'],
            [' ', 'B', ' '],
            ['x', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'B', 2, 1)
        should_be = [
            [' ', ' ', ' '],
            ['x', ' ', 'x'],
            [' ', 'B', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'B', 0, 2)
        should_be = [
            [' ', ' ', 'B'],
            [' ', 'x', ' '],
            ['x', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'B', 1, 2)
        should_be = [
            [' ', 'x', ' '],
            [' ', ' ', 'B'],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'B', 2, 2)
        should_be = [
            ['x', ' ', ' '],
            [' ', 'x', ' '],
            [' ', ' ', 'B'],
        ]
        self.assertEqual(new_board, should_be)

    def test_place_R(self):
        board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(board, 'R', 0, 0)
        should_be = [
            ['R', 'x', 'x'],
            ['x', ' ', ' '],
            ['x', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'R', 1, 0)
        should_be = [
            ['x', ' ', ' '],
            ['R', 'x', 'x'],
            ['x', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'R', 2, 0)
        should_be = [
            ['x', ' ', ' '],
            ['x', ' ', ' '],
            ['R', 'x', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'R', 0, 1)
        should_be = [
            ['x', 'R', 'x'],
            [' ', 'x', ' '],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'R', 1, 1)
        should_be = [
            [' ', 'x', ' '],
            ['x', 'R', 'x'],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'R', 2, 1)
        should_be = [
            [' ', 'x', ' '],
            [' ', 'x', ' '],
            ['x', 'R', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'R', 0, 2)
        should_be = [
            ['x', 'x', 'R'],
            [' ', ' ', 'x'],
            [' ', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'R', 1, 2)
        should_be = [
            [' ', ' ', 'x'],
            ['x', 'x', 'R'],
            [' ', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'R', 2, 2)
        should_be = [
            [' ', ' ', 'x'],
            [' ', ' ', 'x'],
            ['x', 'x', 'R'],
        ]
        self.assertEqual(new_board, should_be)

    def test_place_K(self):
        board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(board, 'K', 0, 0)
        should_be = [
            ['K', 'x', ' '],
            ['x', 'x', ' '],
            [' ', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'K', 1, 0)
        should_be = [
            ['x', 'x', ' '],
            ['K', 'x', ' '],
            ['x', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'K', 2, 0)
        should_be = [
            [' ', ' ', ' '],
            ['x', 'x', ' '],
            ['K', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'K', 0, 1)
        should_be = [
            ['x', 'K', 'x'],
            ['x', 'x', 'x'],
            [' ', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'K', 1, 1)
        should_be = [
            ['x', 'x', 'x'],
            ['x', 'K', 'x'],
            ['x', 'x', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'K', 2, 1)
        should_be = [
            [' ', ' ', ' '],
            ['x', 'x', 'x'],
            ['x', 'K', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'K', 0, 2)
        should_be = [
            [' ', 'x', 'K'],
            [' ', 'x', 'x'],
            [' ', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'K', 1, 2)
        should_be = [
            [' ', 'x', 'x'],
            [' ', 'x', 'K'],
            [' ', 'x', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'K', 2, 2)
        should_be = [
            [' ', ' ', ' '],
            [' ', 'x', 'x'],
            [' ', 'x', 'K'],
        ]
        self.assertEqual(new_board, should_be)

    def test_place_N(self):
        board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(board, 'N', 0, 0)
        should_be = [
            ['N', ' ', ' '],
            [' ', ' ', 'x'],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'N', 1, 0)
        should_be = [
            [' ', ' ', 'x'],
            ['N', ' ', ' '],
            [' ', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'N', 2, 0)
        should_be = [
            [' ', 'x', ' '],
            [' ', ' ', 'x'],
            ['N', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'N', 0, 1)
        should_be = [
            [' ', 'N', ' '],
            [' ', ' ', ' '],
            ['x', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'N', 1, 1)
        should_be = [
            [' ', ' ', ' '],
            [' ', 'N', ' '],
            [' ', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        # Further

        new_board = _place(board, 'N', 2, 1)
        should_be = [
            ['x', ' ', 'x'],
            [' ', ' ', ' '],
            [' ', 'N', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'N', 0, 2)
        should_be = [
            [' ', ' ', 'N'],
            ['x', ' ', ' '],
            [' ', 'x', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'N', 1, 2)
        should_be = [
            ['x', ' ', ' '],
            [' ', ' ', 'N'],
            ['x', ' ', ' '],
        ]
        self.assertEqual(new_board, should_be)

        new_board = _place(board, 'N', 2, 2)
        should_be = [
            [' ', 'x', ' '],
            ['x', ' ', ' '],
            [' ', ' ', 'N'],
        ]
        self.assertEqual(new_board, should_be)

    def test_place_combined(self):
        board = [
            ['K', 'x', ' '],
            ['x', 'x', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(board, 'R', 0, 0)
        should_be = None
        self.assertEqual(new_board, should_be)

        board = [
            ['K', 'x', ' '],
            ['x', 'x', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(board, 'R', 0, 1)
        should_be = None
        self.assertEqual(new_board, should_be)

        board = [
            ['K', 'x', ' '],
            ['x', 'x', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(board, 'R', 0, 2)
        should_be = None
        self.assertEqual(new_board, should_be)

        board = [
            ['K', 'x', ' '],
            ['x', 'x', ' '],
            [' ', ' ', ' '],
        ]
        new_board = _place(board, 'R', 1, 2)
        should_be = [
            ['K', 'x', 'x'],
            ['x', 'x', 'R'],
            [' ', ' ', 'x'],
        ]
        self.assertEqual(new_board, should_be)

if __name__ == '__main__':
    unittest.main()
