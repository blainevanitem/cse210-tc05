from game.console import Console
from game.jumper import Jumper
from game.cutter import Cutter
import random

class Director:
    def __init__(self):
        self.keep_playing = True
        self.random_word = ""
        self.parachuter = ["  ___  "," /___\ "," \   / ","  \ /  ","   0   ","  /|\  ","  / \  ","       ","^^^^^^^"]
        self.cut_parachute = False
        self.guess = ""
        self.console = Console()
        self.jumper = Jumper()
        self.cutter = Cutter()

    def start_game(self):
        #Get words from list and randomly choose one for game
        self.get_text_file()
        self.random_word = self.cutter.get_word(self.word_list)
        while(self.keep_playing):
            self.do_outputs()
            self.get_inputs()
            self.do_updates()
        #If game is lost show that the parachuter is dead
        self.parachuter[0] = "   X   "
        self.console.display_parachuter(self.parachuter)
        self.console.display_answer(self.cutter.word)
            

    def do_outputs(self):
        #Display empty spaces and parachuter
        self.console.display_wordspace(self.cutter.empty_word)
        self.console.display_parachuter(self.parachuter)
        

    def do_updates(self):
        #Update parachuter and end if no parachute
        self.cutter.update_blanks(self.guess)
        self.cutter.cut_parachute(self.guess,self.parachuter)
        #need to update the blankword array with correct letter
        self.keep_playing = self.cutter.end_of_line()

    def get_inputs(self):
        #Get inputs
        self.guess = self.jumper.get_guess()

    def get_text_file(self):
        #Read file with words
        self.my_file = open("jumper\Randomwords.txt")
        self.word_list = self.my_file.readlines()
        self.my_file.close()
        


    