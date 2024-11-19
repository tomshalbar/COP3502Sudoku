from unittest import TestCase

from sudoku_generator import *

class TestSudokuGenerator(TestCase):
    sudoku1 = SudokuGenerator(9, 20)
    sudoku1.board[0][0] = 9
    sudoku1.board[1][4] = 9
    sudoku1.board[6][8] = 9
    sudoku1.board[8][1] = 9
    sudoku1.print_board()
    sudoko2 = SudokuGenerator(9, 30)

    def test_valid_in_row(self):
        self.assertFalse(self.sudoku1.valid_in_row(1, 9))
        self.assertFalse(self.sudoku1.valid_in_row(6, 9))
        self.assertTrue(self.sudoku1.valid_in_row(7, 9))
        self.assertTrue(self.sudoku1.valid_in_row(2, 9))


    def test_valid_in_col(self):
        self.assertFalse(self.sudoku1.valid_in_col(4, 9))
        self.assertFalse(self.sudoku1.valid_in_col(1, 9))
        self.assertTrue(self.sudoku1.valid_in_col(7, 9))
        self.assertTrue(self.sudoku1.valid_in_col(2, 9))

    def test_valid_in_box(self):
        self.assertFalse(self.sudoku1.valid_in_box(0, 0, 9))
        self.assertFalse(self.sudoku1.valid_in_box(6, 6, 9))
        self.assertTrue(self.sudoku1.valid_in_box(3, 3, 9))
        self.assertTrue(self.sudoku1.valid_in_box(0, 6, 9))

    def test_is_valid(self):
        self.assertFalse(self.sudoku1.is_valid(2, 1, 9))
        self.assertFalse(self.sudoku1.is_valid(7, 7, 9))
        self.assertFalse(self.sudoku1.is_valid(0, 7, 9))
        self.assertFalse(self.sudoku1.is_valid(6, 7, 9))
        self.assertFalse(self.sudoku1.is_valid(3, 0, 9))
        self.assertFalse(self.sudoku1.is_valid(5, 4, 9))
        self.assertTrue(self.sudoku1.is_valid(5, 2, 9))
        self.assertTrue(self.sudoku1.is_valid(7, 3, 9))
        self.assertTrue(self.sudoku1.is_valid(2, 7, 9))

