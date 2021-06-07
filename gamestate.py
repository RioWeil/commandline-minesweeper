"""
Date: 06/06/2021
Name: Rio Weil
Title: gamestate.py
Description: Represents the Game state of the minesweeper game.
"""
import numpy as np

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
        self.state = create_board(width, height, numbombs)

    """
    Returns a 2x2 array corresponding to a width * height minsweeper board with numbombs.
    width (int) - Width of the gameboard
    height (int) - Height of the gameboard
    numbombs (int) - Number of bombs on gameboard
    """
    def create_board(self, width, height, numbombs):
        return 0

    """
    Prints out the current board to the console.
    """
    def render(self):
        return 0

    """
    Handles command given on the commandline
    command (string) - Command provided by user in the console
    """
    def handle_input(self, command):
        return 0

