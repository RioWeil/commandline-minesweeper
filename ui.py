import model
import errors

class Game:
    """
    Initializes the Game.
    """
    def __init__(self):
        self.gamestate = model.GameState(1, 1, 1)
            
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
