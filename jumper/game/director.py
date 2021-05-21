from game.console import Console
from game.jumper import Jumper
from game.cutter import Cutter
import random

class Director:
    def __init__(self):
        self.keep_playing = True
        self.word_list = ["Example"]
        self.parachuter = ["  ___  "," /___\ "," \   / ","  \ /  ","   0   ","  /|\  ","  / \  ","       ","^^^^^^^"]
        self.cut_parachute = False
        self.console = Console()
        self.jumper = Jumper()
        self.cutter = Cutter()

    def start_game(self):
        while(self.keep_playing):
            self.console.display_spaces()
            self.console.display_parachuter()
            self.jumper
            self.cutter
