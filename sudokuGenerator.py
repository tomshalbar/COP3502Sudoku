import sudoku_generator

class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        """Constructor for the SudokuGenerator class.
        For the purposes of this project, row_length is always 9
        removed_cells could vary depending on the difficulty level chosen.
    (see “UI Requirements”)."""

        pass

    def get_board(self):
        """Returns a 2D python list of numbers, which represents the board"""
        pass

    def print_board(self):
        """Displays the board to the console."""
        pass

    def valid_in_row(self, row, num):
        """Returns a Boolean value.
        Determines if num is contained in the given row of the board."""
        pass

    def valid_in_col(self, col, num):
        """Returns a Boolean value.
        Determines if num is contained in the given column of the board."""
        pass

    def valid_in_box(self, row_start, col_start, num):
        """Returns a Boolean value.
        Determines if num is contained in the 3x3 box from
        (row_start, col_start) to (row_start+2, col_start+2)."""
        pass

    def is_valid(self, row, col, num):
        """Returns if it is valid to enter num at (row, col) in the board.
        This is done by checking the appropriate row, column, and box."""
        pass

    def fill_box(self, row_start, col_start):
        """Randomly fills in values in the 3x3 box from
    (row_start, col_start) to (row_start+2, col_start+2).
        Uses unused_in_box to ensure no values occur in the box more than once."""
        pass

    def fill_diagonal(self):
        """Fills the three boxes along the main diagonal of the board.
        This is the first major step in generating a Sudoku.
        See the Step 1 picture in Sudoku Generation for further explanation."""
        pass

    def fill_remaining(self):
        """This method is provided for students.
        Fills the remaining squares in the board.
        It is the second major step in generating a Sudoku.
        This will return a boolean."""
        pass

    def fill_values(self):
        """This method is provided for students.
        It constructs a solution by calling fill_diagonal and fill_remaining."""
        pass

    def remove_cells(self):
        """This method removes the appropriate number of cells from the board.
        It does so by randomly generating (row, col) coordinates of the board and
        setting the value to 0.
        Note: Be careful not to remove the same cell multiple times.
        A cell can only be removed once.
        This method should be called after generating the Sudoku solution."""
        pass







