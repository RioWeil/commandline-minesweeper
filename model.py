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
        set_neighbours(self.board)
        

    """
    Returns a 2x2 array corresponding to a width * height minsweeper board with numbombs.
    width (int) - Width of the gameboard
    height (int) - Height of the gameboard
    numbombs (int) - Number of bombs on gameboard
    """
    def create_board(self, width, height, numbombs):
        bomblocs = random.sample(range(0, width * height), numbombs)
        board = []
        for i in range(height):
            row = []
            for j in range(width):
                if(i * width + j in bomblocs):
                    row.append(Tile(True))
                else:
                    row.append(Tile(False))
            board.append(row)
        return board

    """
    Updates tiles in board to reflect number of neighbouring bombs. 
    A tile with 3 neighbouring bombs will have bomb_neighbours set to 3.
    board (2D list) - Board of tiles to update
    """
    def set_neighbours(self, board):
        pass


    """
    Returns a string corresponding to the current gamestate
    """
    def render(self):
        return 0


    """
    Reveals the space on the board at coordinate (x, y)
    x (int) - x coordinate of space to check
    y (int) - y coordinate of space to check
    """
    def check_space(self, x, y):
        pass

    """
    Sets flag down at coordinate (x, y)
    x (int) - x coordinate of space to check
    y (int) - y coordinate of space to check
    """
    def set_flag(self, x, y):
        pass

    """
    Reveals all spaces on board
    """
    def reveal_all(self):
        pass

            