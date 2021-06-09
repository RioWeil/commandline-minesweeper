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
    Returns a string corresponding to the current gamestate
    """
    def render(self):
        return 0

    """
    Handles command given on the commandline
    command (string) - Command provided by user in the console
    """
    def handle_input(self, command):
        split_command = command.split
        if(split_command[0] == "check"):
            check_space(split_command[1], split_command[2])
        elif(split_command[0] == "flag"):
            set_flag(split_command[1], split_command[2])
        elif(split_command[0] == "fold"):
            self.gameover = True
        else:
            raise errors.InvalidInputException("")

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
    def reveal_all():
        pass

            