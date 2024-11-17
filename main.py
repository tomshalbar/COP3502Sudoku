import pygame
from cell import *
from board import *
from sudoku_generator import *


def generate_sudoku(size, removed) -> list[list]:
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    original_board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    sudoku.print_board()
    return board

def main():
    #testing
    generate_sudoku(3, 4)

if __name__ == '__main__':
    main()