from game.console import Console
from game.jumper import Jumper
from game.cutter import Cutter
import random

class Director:
    def __init__(self):
        self.keep_playing = True
        self.word_list = ["Example"]
        self.random_word = ""
        self.parachuter = ["  ___  "," /___\ "," \   / ","  \ /  ","   0   ","  /|\  ","  / \  ","       ","^^^^^^^"]
        self.cut_parachute = False
        self.console = Console()
        self.jumper = Jumper()
        self.cutter = Cutter()

    def start_game(self):
        self.random_word = self.cutter.get_word(self.word_list) #need to select the word first and get spaces.
        while(self.keep_playing):
            self.do_outputs()
            self.do_updates()
            self.do_outputs()

    def do_outputs(self):
        self.console.display_spaces()
        self.console.display_parachuter()

    def do_updates(self):
        self.cutter.cut_parachute()
        #need to update the blank word array with correct letter

    def get_inputs(self):
        self.jumper.get_guess()


    