import gamestate
import numpy as np

print("Welcome to command line minesweeper!")
print("Enter the desired boardsize in the form: width, height")
dim = input()
dim = dim.split()
print("Enter the desired number of bombs")
numbombs = input()
