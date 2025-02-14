import pygame
from constants import *
import sys
from cell import *
from sudoku_generator import *




class Board:

    def __init__(self, width, height, screen, difficulty):
        """Constructor for the Board class.
        screen is a window from PyGame.
        difficulty is a variable to indicate if the user chose easy medium, or hard."""

        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None


        self.cells = [
            [
                Cell(0, row, col, screen)
                for col in range(9)
            ]
            for row in range(9)
        ]

        if difficulty == "easy":
            removed_cells = 30
        elif difficulty == "medium":
            removed_cells = 40
        elif difficulty == "hard":
            removed_cells = 50
        else:
            raise Exception("Difficulty must be either easy or medium. or hard")



        sudoku_board = SudokuGenerator(self.width, removed_cells)
        sudoku_board.fill_values()

        #create a copy of the complete board
        self.complete_sudoku_board = [
            [" " for row in range(9)]
            for col in range(9)
        ]
        for row in range(9):
            for col in range(9):
                self.complete_sudoku_board[row][col] = sudoku_board.get_board()[row][col]
         #finish setting up the sudoko board
        self.sudoku_board = sudoku_board
        self.sudoku_board.remove_cells()
        board = self.sudoku_board.get_board()

        #save the board as cells
        for row in range(self.width):
            for col in range(self.width):
                if board[row][col] != 0:
                    self.cells[row][col] = Cell(board[row][col], row, col, screen, pre_filled=True)
                else:
                    self.cells[row][col] = Cell(board[row][col], row, col, screen, pre_filled=False)



    def draw(self):
        """Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        Draws every cell on this board."""
        self.screen.fill(BG_COLOR)
        for row in range(self.width):
            for col in range(self.width):
                self.cells[row][col].draw()

        for i in range (0,10, 3):
                pygame.draw.line(
                self.screen,
                (0,0,0),
                (0, i*SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_WIDTH + 1
            )


        for i in range(0, 10, 3):
            pygame.draw.line(
                self.screen,
                (0,0,0),
                (i * SQUARE_SIZE, 0),
                (i * SQUARE_SIZE, HEIGHT),
                LINE_WIDTH + 1

            )





    def select(self, row, col):
        """Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value."""
        if self.selected_cell:
            self.selected_cell.selected = False

        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def click(self, x_cord, y_cord):
        """If a tuple of (x,y) coordinates is within the displayed board,
        this function returns a tuple of the (row, col) of the cell which was clicked.
        Otherwise, this function returns None."""
        if 0 <= x_cord < HEIGHT and 0 <= y_cord < WIDTH:
            row = x_cord // SQUARE_SIZE
            col = y_cord // SQUARE_SIZE

            return row, col
        return None

    def clear(self):
        """Clears the value cell.
        Note that the user can only remove the cell values and
        sketched values that are filled by themselves."""

        if self.selected_cell:
            self.selected_cell.set_sketched_value(0)

        #allows for user inputted values to be cleared
        if self.selected_cell.value != 0 and not self.selected_cell.pre_filled:
            self.selected_cell.set_cell_value(0)

    def sketch(self, value):
        """Sets the sketched value of the current selected cell equal to the user entered value.
        It will be displayed at the top left corner of the cell using the draw() function."""
        # inputs the sketched value
        if self.selected_cell:
            self.selected_cell.set_sketched_value(value)


    def place_number(self, value):
        """Sets the value of the current selected cell equal to the user entered value.
        Called when the user presses the Enter key."""
        if self.selected_cell:
            if self.selected_cell.value == 0:
                self.selected_cell.set_cell_value(value)
                self.selected_cell.sketched_value = 0


    def reset_to_original(self):
        """Resets all cells in the board to their original values
        (0 if cleared, otherwise the corresponding digit)."""

        board = self.sudoku_board.get_board()

        for row in range(self.width):
            for col in range(self.width):
                if board[row][col] != 0:
                    self.cells[row][col] = Cell(board[row][col], row, col, self.screen, pre_filled=True)
                else:
                    self.cells[row][col] = Cell(board[row][col], row, col, self.screen, pre_filled=False)




    def is_full(self):
        """Returns a Boolean value indicating whether the board is full or not."""
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        """Updates the underlying 2D board with the values in all cells."""
        new_board = [[0 for x in range(BOARD_ROWS)] for x in range(BOARD_COLS)]

        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                new_board[row][col] = self.cells[row][col].value

        return new_board

    def find_empty(self):
        """Finds an empty cell and returns its row and col as a tuple (x,y)."""

        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.cells[row][col].value == 0:
                    return (row, col)
        return None

    def check_board(self):
        """Check whether the Sudoku board is solved correctly."""


        for row in range(BOARD_ROWS):
            row_val = [self.cells[row][col].value for col in range(BOARD_COLS)]
            if len(row_val) != len(set(row_val)) or 0 in row_val:
                return False

        for col in range(BOARD_COLS):
            col_val = [self.cells[row][col].value for row in range(BOARD_ROWS)]
            if len(col_val) != len(set(col_val)) or 0 in col_val:
                return False

        for rbox in range(0, BOARD_ROWS, 3):
            for cbox in range(0, BOARD_COLS, 3):
                box_values = []
                for i in range(3):
                    for j in range(3):
                        box_values.append(self.cells[rbox + i][cbox + j].value)
                if len(box_values) != len(set(box_values)) or 0 in box_values:
                    return False

        return True





