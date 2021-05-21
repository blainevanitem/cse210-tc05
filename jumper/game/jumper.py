from game.console import Console

class Jumper:
    def __init__(self):
        self.guess = ""
        self.console = Console()
        
    def get_guess(self):
        #call display guess_prompt
        message = "What letter do you think is in my word: "
        self.guess = self.console.display_message(message)
        
