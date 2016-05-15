import unittest

from chess_challenge import get_variants, rotate_premutations


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
        variants = get_variants(4, 4, rooks=1, knights=4)
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
            ['K', ' ', ' '],
            [' ', ' ', 'R'],
            ['K', ' ', ' '],
        ]
        self.assertEqual(premuatations[1], board_90)

        # rotate 180 degrees
        board_180 = [
            [' ', ' ', 'K'],
            ['R', ' ', ' '],
            [' ', ' ', 'K'],
        ]
        self.assertEqual(premuatations[2], board_180)

        # rotate 270 degrees
        board_270 = [
            [' ', 'R', ' '],
            [' ', ' ', ' '],
            ['K', ' ', 'K'],
        ]
        self.assertEqual(premuatations[3], board_270)


if __name__ == '__main__':
    unittest.main()

