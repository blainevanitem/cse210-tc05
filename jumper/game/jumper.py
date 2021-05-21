from game.console import Console

class Jumper:
    def __init__(self):
        self.empty_word = []
        self.guess = ""
        self.console = Console()
        

    def blank_word(self,word):
        #Used to create a list with _ for each letter in word
        for i in range(0,len(word)):
            #For each letter in the word add _ to empty list
            self.empty_word.append("_")

    def get_guess(self):
        #call display guess_prompt
        message = "What letter do you think is in my word: "
        self.guess = self.console.display_message(message)
        
