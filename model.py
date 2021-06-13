"""
Date: 06/06/2021
Name: Rio Weil
Title: model.py
Description: Backend code for minesweeper game
"""
import random
import errors

"""
Represents a single tile on the minesweeper board
"""
class Tile:
    """
    Initializes the tile.
    is_bomb (boolean) - Whether the tile is a bomb tile or not
    """
    def __init__(self, is_bomb):
        self.is_bomb = is_bomb
        self.flagged = False
        self.revealed = False
        self.bomb_neighbours = 0


"""
Represents a minesweeper gamestate
"""
class GameState:
    """
    Initializes the gamestate.
    Throws ZeroException if board has size zero.
    Throws TooManyBombsException if number of bombs specified is too many for board.
    width (int) - Width of the gameboard
    height (int) - Height of the gameboard
    numbombs (int) - Number of bombs on gameboard
    """
    def __init__(self, width, height, numbombs):
        if(width == 0 or height == 0):
            raise errors.ZeroException
        if(numbombs > width * height):
            raise errors.TooManyBombsException
        self.width = width
        self.height = height
        self.numbombs = numbombs
        self.victory = False
        self.gameover = False
        self.board = self.create_board(width, height, numbombs)
        self.set_neighbours()
        

    """
    Returns a 2x2 array corresponding to a width * height minsweeper board with numbombs.
    width (int) - Width of the gameboard
    height (int) - Height of the gameboard
    numbombs (int) - Number of bombs on gameboard
    """
    def create_board(self, width, height, numbombs):
        bomblocs = random.sample(range(0, width * height), numbombs)
        newboard = []
        for i in range(height):
            row = []
            for j in range(width):
                if(i * width + j in bomblocs):
                    row.append(Tile(True))
                else:
                    row.append(Tile(False))
            newboard.append(row)
        return newboard

    """
    Updates tiles in board to reflect number of neighbouring bombs. 
    A tile with 3 neighbouring bombs will have bomb_neighbours set to 3.
    board (2D list) - Board of tiles to update
    """
    def set_neighbours(self):
        for i in range(self.height):
            for j in range(self.width):
                count = 0
                if (i - 1 >= 0):
                    count += self.is_bomb_set(i - 1, j)
                    if (j - 1 >= 0):
                        count += self.is_bomb_set(i - 1, j - 1)
                    if (j + 1 < self.width):
                        count += self.is_bomb_set(i - 1, j + 1)
                if (i + 1 < self.height):
                    count += self.is_bomb_set(i + 1, j)
                    if (j - 1 >= 0):
                        count += self.is_bomb_set(i + 1, j - 1)
                    if (j + 1 < self.width):
                        count += self.is_bomb_set(i + 1, j + 1)
                if (j - 1 >= 0):
                    count += self.is_bomb_set(i, j - 1)
                if (j + 1 < self.width):
                    count += self.is_bomb_set(i, j + 1)
                self.board[i][j].bomb_neighbours = count

    """
    Helper function for set_neighbours
    Returns 1 if set_bomb is True, 0 otherwise.
    """
    def is_bomb_set(self, row, col):
        if (self.board[row][col].is_bomb):
            return 1
        else:
            return 0

    """
    Returns a string corresponding to the current gamestate
    """
    def render(self):
        rendered_board = self.render_label_row()
        rendered_board += "\n"
        for i in range(self.height):
            rendered_board += self.render_border_row()
            rendered_board += "\n"
            rendered_board += self.render_minefield_row(i)
            rendered_board += "\n"
        rendered_board += self.render_border_row()
        return rendered_board

    """
    Returns a string labelling the columns of the board
    """
    def render_label_row(self):
        row = "   "
        for i in range(1, self.width + 1):
            row += str(i % 10)
            if ((i+1) % 10 == 0) and (not (self.width == i)):
                row += str((i+1) // 10)
            else:
                row += " "
        return row

    """
    Return a string with a border row of the form +-+-+-+
    """
    def render_border_row(self):
        row = "  "
        for i in range(self.width):
            row += "+-"
        row += "+"
        return row
    
    """
    Returns a string with the board information of the form X  |1| |F|...
    """
    def render_minefield_row(self, row):
        row_to_render = self.board[row]
        newrow = str(row + 1)
        if (row < 9):
            newrow += " "
        for i in range(self.width):
            newrow += "|"
            if not row_to_render[i].revealed:
                if row_to_render[i].flagged:
                    newrow += "F"
                else:
                    newrow += " "
            else:
                if row_to_render[i].is_bomb:
                    newrow += "B"
                else:
                    newrow += str(row_to_render[i].bomb_neighbours)
        newrow += "|"
        return newrow



    """
    Reveals the space on the board at coordinate (x, y).
    Throws IndexError if trying to access coordinate not in the board.
    If space has zero bombs, calls recursive helper function on all neighbours.
    row (int) - row coordinate of space to check (0 based indexing)
    col (int) - column coordinate of space to check (0 based indexing)
    """
    def check_space(self, row, col):
        self.board[row][col].revealed = True
        if self.board[row][col].is_bomb:
            self.gameover = True
            return
        if self.board[row][col].bomb_neighbours == 0:
            if (row - 1 >= 0):
                self.check_space_notbomb(row - 1, col)
                if (col - 1 >= 0):
                    self.check_space_notbomb(row - 1, col - 1)
                if (col + 1 < self.width):
                    self.check_space_notbomb(row - 1, col + 1)
            if (row + 1 < self.height):
                self.check_space_notbomb(row + 1, col)
                if (col - 1 >= 0):
                    self.check_space_notbomb(row + 1, col - 1)
                if (col + 1 < self.width):
                    self.check_space_notbomb(row + 1, col + 1)
            if (col - 1 >= 0):
                self.check_space_notbomb(row, col - 1)
            if (col + 1 < self.width):
                self.check_space_notbomb(row, col + 1)
            

    """
    Recursive helper function for check_space.
    Reveals space if not a bomb, and if space was not revealed previously and
    has zero bomb neighbours, recursively calls itself on neighbours.
    """
    def check_space_notbomb(self, row, col):
        if (not self.board[row][col].revealed) and (not self.board[row][col].is_bomb):
            self.board[row][col].revealed = True
            if self.board[row][col].bomb_neighbours == 0:
                if (row - 1 >= 0):
                    self.check_space_notbomb(row - 1, col)
                    if (col - 1 >= 0):
                        self.check_space_notbomb(row - 1, col - 1)
                    if (col + 1 < self.width):
                        self.check_space_notbomb(row - 1, col + 1)
                if (row + 1 < self.height):
                    self.check_space_notbomb(row + 1, col)
                    if (col - 1 >= 0):
                        self.check_space_notbomb(row + 1, col - 1)
                    if (col + 1 < self.width):
                        self.check_space_notbomb(row + 1, col + 1)
                if (col - 1 >= 0):
                    self.check_space_notbomb(row, col - 1)
                if (col + 1 < self.width):
                    self.check_space_notbomb(row, col + 1)

    """
    Sets flag down at coordinate (x, y).
    Throws IndexError if trying to access coordinate not in the board.
    row (int) - row coordinate of space to flag (0 based indexing)
    col (int) - column coordinate of space to flag (0 based indexing)
    """
    def set_flag(self, row, col):
        self.board[row][col].flagged = True

    """
    Returns true if board is in winning state (all tiles revealed except bombs)
    """
    def is_win(self):
        count = 0
        for i in range(self.height):
            for j in range(self.width):
                if (not self.board[i][j].is_bomb) and (self.board[i][j].revealed):
                    count += 1
        return (count == (self.width * self.height - self.numbombs))


    """
    Reveals all spaces on board
    """
    def reveal_all(self):
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j].revealed = True