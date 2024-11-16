import math, random

class SudokuGenerator:
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length: int, removed_cells: int):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [["-" for i in range(self.row_length)] for j in range(self.row_length)]
        self.box_length = int(row_length ** .5)

    '''
	Returns a 2D python list of numbers which represents the board

    '''
    def get_board(self) -> list[list]:
        return self.board


    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

    '''
    def print_board(self) -> None:
        for row in range(self.row_length):
            for col in range(self.row_length):
                print(self.board[row][col], end=' ')
            print()

    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True
    '''
    def valid_in_row(self, row, num) -> bool:
        return False if num in self.get_board()[row] else True

    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True
    '''
    def valid_in_col(self, col, num) -> bool:
        for row in range(self.row_length):
          if num == self.get_board()[row][col]:
              return False
        return True


    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

    '''
    def valid_in_box(self, row_start, col_start, num) -> bool:
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if num == self.get_board()[row][col]:
                    return False
        return True

    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box
    '''
    def is_valid(self, row, col, num) -> bool:
        if not self.valid_in_row(row, num):
            return False
        if not self.valid_in_col(col, num):
            return False
        if not self.valid_in_box(row//3 * 3, col//3 * 3, num):
            return False
        return True

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box
    '''
    def fill_box(self, row_start, col_start) -> None:
        nums_in_box = [1,2,3,4,5,6,7,8,9]
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                chosen_num =  random.choice(nums_in_box)
                self.board[row][col] = chosen_num
                nums_in_box.remove(chosen_num)
    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)
    '''
    def fill_diagonal(self) -> None:
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

    '''
    def fill_remaining(self, row: int, col: int) -> bool:
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(int(row // self.box_length) * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining
    '''
    def fill_values(self) -> None:
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self) -> None:
        for i in range(self.removed_cells):
            removed_a_cell = False
            while not removed_a_cell:
                row = random.randint(0, int(self.row_length) - 1)
                col = random.randint(0, int(self.row_length) - 1)
                if self.get_board()[row][col] == 0:
                    continue
                self.board[row][col] = 0
                removed_a_cell = True



