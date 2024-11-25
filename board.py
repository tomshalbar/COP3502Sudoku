import pygame
from constants import *
import sys
from cell import *


#variables


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

        #creates 81 cell classes for each cell in the board
        self.cells = [
            [
                Cell(0, row, col, screen)
                for col in range(9)
            ]
            for row in range(9)
        ]

    def draw(self):
        """Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        Draws every cell on this board."""
        # pass
        for i in range (1,BOARD_ROWS):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i*SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_WIDTH
            )


        #draw vertical grids
        for i in range(1, BOARD_COLS):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i * SQUARE_SIZE, 0),
                (i * SQUARE_SIZE, HEIGHT),
                LINE_WIDTH

            )



    def select(self, row, col):
        """Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value."""
        # selects a new cell and deselects old cell
        if self.selected_cell:
            self.selected_cell.selected = False

        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def click(self, x_cord, y_cord):
        """If a tuple of (x,y) coordinates is within the displayed board,
        this function returns a tuple of the (row, col) of the cell which was clicked.
        Otherwise, this function returns None."""
        # re-maps the raw coordinates to the grid created if raw coordinates are in the board
        if 0 <= x_cord < HEIGHT and 0 <= y_cord < WIDTH:
            row = x_cord // SQUARE_SIZE
            col = y_cord // SQUARE_SIZE

            return row, col
        return None

    def clear(self):
        """Clears the value cell.
        Note that the user can only remove the cell values and
        sketched values that are filled by themselves."""

        #clears only user-inputted values for the cell selected
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

        #sets new cell value and removes the sketched value
        if self.selected_cell:
            if self.selected_cell.value == 0:
                self.selected_cell.set_cell_value(value)
                self.selected_cell.sketched_value = 0


    def reset_to_original(self):
        """Resets all cells in the board to their original values
        (0 if cleared, otherwise the corresponding digit)."""

        #loops over all values to reset to original and clear all sketched values
        curr_board = self.get_board()

        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                original_val = curr_board[row][col]
                self.cells[row][col].set_cell_value(original_val)
                self.cells[row][col].set_sketched_value(0)



    def is_full(self):
        """Returns a Boolean value indicating whether the board is full or not."""
        # checks to see if every square is empty and returns result
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        """Updates the underlying 2D board with the values in all cells."""
        # creates a new 2D board that is empty
        new_board = [[0 for x in range(BOARD_ROWS)] for x in range(BOARD_COLS)]

        # fills in the values for the new board created earlier
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                new_board[row][col] = self.cells[row][col].value

        return new_board

    def find_empty(self):
        """Finds an empty cell and returns its row and col as a tuple (x,y)."""

        #loops through all values and checks for empty cells.
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.cells[row][col].value == 0:
                    return (row, col)
        return None

    def check_board(self):
        """Check whether the Sudoku board is solved correctly."""

        # for row and col checkers the function creates a list and checks for duplicates or empty squares in the list

        # rows
        for row in range(BOARD_ROWS):
            row_val = [self.cells[row][col].value for col in range(BOARD_COLS)]
            if len(row_val) != len(set(row_val)) or 0 in row_val:
                return False

        # cols
        for col in range(BOARD_COLS):
            col_val = [self.cells[row][col].value for row in range(BOARD_ROWS)]
            if len(col_val) != len(set(col_val)) or 0 in col_val:
                return False

        # 3x3
        # seperates the board in to 3x3 grids and checks for duplicates and empty spaces
        for rbox in range(0, BOARD_ROWS, 3):
            for cbox in range(0, BOARD_COLS, 3):
                box_values = []
                for i in range(3):
                    for j in range(3):
                        box_values.append(self.cells[rbox + i][cbox + j].value)
                if len(box_values) != len(set(box_values)) or 0 in box_values:
                    return False

        return True




