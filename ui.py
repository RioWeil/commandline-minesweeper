import model
import errors

class Game:
    """
    Initializes the Game.
    """
    def __init__(self):
        self.gamestate = model.GameState(1, 1, 1)

    """
    Ask the user for the board dimensions and the number of bombs desired.
    """
    def initialparams(self):
        pass

    """
    Main gameloop of the minesweeper game
    """
    def gameloop(self):
        pass
            
    """
    Handles command given on the commandline
    command (string) - Command provided by user in the console
    """
    def handle_input(self, command):
        split_command = command.split
        if(split_command[0] == "check"):
            pass
        elif(split_command[0] == "flag"):
            pass
        elif(split_command[0] == "fold"):
            pass
        else:
            raise errors.InvalidInputException("")

    """
    Renders the current game board.
    """
    def render(self):
        pass

    """
    Returns true if game is in winning state, false otherwise
    """
    def is_win(self):
        pass

    """
    Returns true if game is in losing state, false otherwise
    """
    def is_lose(self):
        pass

    """
    Asks player if they want to play another game, creates new Game if yes
    """
    def play_again(self):
        pass
