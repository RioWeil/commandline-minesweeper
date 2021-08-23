"""
Date: 08/22/2021
Name: Rio Weil
Title: ui.py
Description: Frontend code for minesweeper game, responsible for the UI through the console.
"""

import model
import errors

class Game:
    """
    Initializes the Game.
    """
    def __init__(self):
        try:
            width, height, numbombs = self.initialparams()
            self.gamestate = model.GameState(width, height, numbombs)
            self.gameloop()
        except(IndexError):
            print("It looks like you didn't format your input correctly! Restarting...")
            Game()
        except(ValueError):
            print("It looks like your inputs weren't integers! Restarting...")
            Game()
        except(errors.ZeroException):
            print("It looks like your board has size zero! Restarting...")
            Game()
        except(errors.TooManyBombsException):
            print("It looks like you have too many bombs for the size of your board! Restarting...")
            Game()

    """
    Ask the user for the board dimensions and the number of bombs desired.
    Returns the width, height, and number of bombs of the board.
    """
    def initialparams(self):
        params = input("Welcome to Minesweeper!\nEnter the board width, board height, and number of bombs in the form width height numbombs\n")
        split_params = params.split()
        return int(split_params[0]), int(split_params[1]), int(split_params[2])

    """
    Main gameloop of the minesweeper game
    """
    def gameloop(self):
        while(True):
            self.render()
            self.handle_input()
            if(self.gamestate.gameover):
                self.reveal_all()
                self.render()
                print("You lose!")
                self.play_again()
                break
            if(self.is_win()):
                self.reveal_all()
                self.render()
                print("You win!")
                self.play_again()
                break

            
    """
    Handles command given on the commandline
    """
    def handle_input(self):
        command = input("Enter command\ncheck row col - reveals space at (col, row)\nflag row col - places/removes flag at (col, row)\nfold - to give up\n")
        split_command = command.split()
        try:
            if(split_command[0] == "check"):
                row = int(split_command[1]) - 1
                col = int(split_command[2]) - 1
                if (row < 0) or (row > self.gamestate.height - 1) or (col < 0) or (col > self.gamestate.width - 1):
                    print("Coordinates outside of board! Try again...")
                    self.handle_input()
                else:
                    self.gamestate.check_space(row, col)
            elif(split_command[0] == "flag"):
                row = int(split_command[1]) - 1
                col = int(split_command[2]) - 1
                if (row < 0) or (row > self.gamestate.height - 1) or (col < 0) or (col > self.gamestate.width - 1):
                    print("Coordinates outside of board! Try again...")
                    self.handle_input()
                else:
                    self.gamestate.set_flag(row, col)
            elif(split_command[0] == "fold"):
                self.gamestate.gameover = True
            else:
                print("Invalid command! Try again...")
                self.handle_input()
        except(IndexError):
            print("It looks like you didn't format your input correctly! Try again...")
            self.handle_input()
        except(ValueError):
            print("It looks like your inputs weren't integers! Try again...")
            self.handle_input()


    """
    Renders the current game board.
    """
    def render(self):
        print(self.gamestate.render())

    """
    Returns true if game is in winning state, false otherwise
    """
    def is_win(self):
        return self.gamestate.is_win()

    """
    Returns true if game is in losing state, false otherwise
    """
    def is_lose(self):
        return self.gamestate.is_lose()

    """
    Reveals entire gameboard
    """
    def reveal_all(self):
        self.gamestate.reveal_all()

    """
    Asks player if they want to play another game, creates new Game if yes
    """
    def play_again(self):
        answer = input("Would you like to play again? (y/n)\n")
        if answer == "y":
            Game()
        elif answer == "n":
            return
        else:
            print("Invalid command! Try again...")
            self.play_again()

        
