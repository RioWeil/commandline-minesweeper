# commandline-minesweeper
The classic game Minesweeper, written in python, played on the command line.

## How to use
Download this repository, and run the ```main.py``` file in your Terminal. Follow the prompts to enter commands and play the game!

## Requirements
Must have Python 3.X installed, with the ```random``` module. ```unittest``` module is necessary to run tests.

## Minesweeper Rules
1. Specify the desired board width, height, and number of bombs.
2. Check any unrevealed (blank) square to start the game.
3. Numbers on revealed squares indicate the number of mines on neighbouring tiles (the neighbouring tiles being all surrounding tiles in a 3x3 grid). Use these numbers to identify which squares have hidden mines.
4. Place flags on squares to mark them as dangerous
5. Reveal all safe squares without mines to win the game. Checking a square with a mine results in a loss.