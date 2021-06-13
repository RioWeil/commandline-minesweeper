import model
import errors

class Game:
    """
    Initializes the Game.
    """
    def __init__(self):
        width, height, numbombs = self.initialparams()
        self.gamestate = model.GameState(width, height, numbombs)
        self.gameloop()

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
            if(self.is_lose()):
                self.reveal_all()
                self.render()
                print("You lose!")
                self.play_again()
            if(self.is_win()):
                self.reveal_all()
                self.render()
                print("You win!")
                self.play_again()

            
    """
    Handles command given on the commandline
    """
    def handle_input(self):
        command = input("Enter command\ncheck row col - reveals space at row/col\nflag row col - places flag at row/col\nfold - to give up\n")
        split_command = command.split
        if(split_command[0] == "check"):
            row = int(split_command[1]) - 1
            col = int(split_command[2]) - 1
            self.gamestate.board.check_space(row, col)
        elif(split_command[0] == "flag"):
            row = int(split_command[1]) - 1
            col = int(split_command[2]) - 1
            self.gamestate.board.set_flag(row, col)
        elif(split_command[0] == "fold"):
            self.gamestate.gameover = True
        else:
            print("Invalid command!")
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
        if (answer == "y"):
            Game()
