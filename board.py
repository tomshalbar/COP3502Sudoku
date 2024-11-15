
class Board:

    def __init__(self, width, height, screen, difficulty):
        """Constructor for the Board class.
        screen is a window from PyGame.
        difficulty is a variable to indicate if the user chose easy medium, or hard."""
        pass

    def draw(self):
        """Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        Draws every cell on this board."""
        pass

    def select(self, row, col):
        """Marks the cell at (row, col) in the board as the current selected cell.
        Once a cell has been selected, the user can edit its value or sketched value."""
        pass

    def click(self, row, col):
        """If a tuple of (x,y) coordinates is within the displayed board,
        this function returns a tuple of the (row, col) of the cell which was clicked.
        Otherwise, this function returns None."""
        pass

    def clear(self):
        """Clears the value cell.
        Note that the user can only remove the cell values and
        sketched values that are filled by themselves."""
        pass

    def sketch(self, value):
        """Sets the sketched value of the current selected cell equal to the user entered value.
        It will be displayed at the top left corner of the cell using the draw() function."""
        pass


    def place_number(self, value):
        """Sets the value of the current selected cell equal to the user entered value.
        Called when the user presses the Enter key."""
        pass


    def reset_to_original(self):
        """Resets all cells in the board to their original values
        (0 if cleared, otherwise the corresponding digit)."""
        pass


    def is_full(self):
        """Returns a Boolean value indicating whether the board is full or not."""
        pass

    def update_board(self):
        """Updates the underlying 2D board with the values in all cells."""
        pass

    def find_empty(self):
        """Finds an empty cell and returns its row and col as a tuple (x,y)."""
        pass

    def check_board(self):
        """Check whether the Sudoku board is solved correctly."""
        pass

