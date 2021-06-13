"""
Date: 06/06/2021
Name: Rio Weil
Title: model.py
Description: Backend code for minesweeper game
"""
import numpy as np
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
        return


    """
    Returns a string corresponding to the current gamestate
    """
    def render(self):
        rendered_board = self.render_label_row()
        for i in range(self.height):
            rendered_board += render_border_row()
            rendered_board += render_minefield_row(i)
        rendered_board += render_border_row()
        return rendered_board

    """
    Returns a string labelling the columns of the board
    """
    def render_label_row(self):
        row = "   "
        for i in range(1, self.width + 1):
            row += str(i % 10)
            if ((i+1) % 10 == 0):
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
        row = str(row + 1)
        if (row < 9):
            row += " "
        for i in range(self.width):
            row += "|"
            if not row_to_render[i].revealed:
                if row_to_render[i].flagged:
                    row += "F"
                else:
                    row += " "
            else:
                if row_to_render[i].is_bomb:
                    row += "B"
                else:
                    row += row_to_render[i].bomb_neighbours
        row += "|"
        return row



    """
    Reveals the space on the board at coordinate (x, y).
    Throws IndexError if trying to access coordinate not in the board.
    If space has zero bombs, recursively calls function on all neighbours.
    row (int) - row coordinate of space to check (0 based indexing)
    col (int) - column coordinate of space to check (0 based indexing)
    """
    def check_space(self, row, col):
        return
    
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
        for i in range(self.width):
            for j in range(self.height):
                if (not self.board[i][j].is_bomb) and (self.board[i][j].revealed):
                    count += 1
        return (count == (self.width * self.height - self.numbombs))


    """
    Reveals all spaces on board
    """
    def reveal_all(self):
        for i in range(self.width):
            for j in range(self.height):
                self.board[i][j].revealed = True