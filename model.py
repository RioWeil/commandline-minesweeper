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
        for i in range(width):
            row = []
            for j in range(height):
                pass

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
        splitcomm = command.split
        if(splitcomm[0] == "check"):
            return 0
        elif(splitcomm[0] == "flag"):
            return 0
        elif(splitcomm[0] == "fold"):
            return 0
        else:
            raise errors.InvalidInputException("")
            