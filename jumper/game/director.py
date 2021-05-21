from game.console import Console
from game.jumper import Jumper
from game.cutter import Cutter
import random

class Director:
    def __init__(self):
        self.keep_playing = True
        self.word_list = ["Example"]
        self.cut_parachute = False
        self.wrongs = 0
        self.console = Console()
        self.jumper = Jumper()
        self.cutter = Cutter()

    def start_game(self):
        self.random_word = self.cutter.get_word(self.word_list)
        while(self.keep_playing):
            self.do_outputs()
            self.get_inputs()
            self.do_updates()
            

    def do_outputs(self):
        self.console.display_wordspace(self.cutter.empty_word)
        self.console.display_parachuter(self.cutter.parachuter)

    def do_updates(self):
        self.cutter.cut_parachute()
        if self.cut_parachute == True:
            self.wrongs += 1
            self.cutter.cut_parachute()
        #need to update the blank word array with correct letter

    def get_inputs(self):
        guess = self.console.display_message("Pick a letter to A-Z: ")
        self.cut_parachute = self.jumper.in_word(guess, self.cutter.word)


    