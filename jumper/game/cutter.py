from game.jumper import Jumper
from game.director import Director
import random
class Cutter:
    def __init__(self):
        self.word = ""
        self.empty_word = []
        self.wrong_guess = 0      
        self.jumper = Jumper()
        self.director = Director()
    def blank_word(self,word):
        #Used to create a list with _ for each letter in word
        for i in range(0,len(word)):
            #For each letter in the word add _ to empty list
            self.empty_word.append("_")
    def get_word(self, word_list):
        # get word, save word to self.word
        self.word = word_list.index(random.randint(0,len(word_list)))
        self.blank_word(self.word)
        return self.word
    def cut_parachute(self, get_guess):
        
        '''
        for loop to see if letter in word.
        return true or false
        '''
        times = self.is_letter(self.jumper.guess,self.word)
        if times == 0:
            self.director.parachuter.pop[0]
            self.wrong_guess += 1
            if self.wrong_guess == 4:
                self.director.keep_playing = False
        

    def is_letter(self, guess, word):
        '''
        compare letter to word
        '''
        times = word.count(self.jumper.guess)
        
        space = word.index(self.jumper.guess)
        self.empty_word.insert(self.jumper.guess, space)
        if times > 1:
            for _ in range(1, times):
                space = word.index(self.jumper.guess,space)
                self.empty_word.insert(self.jumper.guess, space)

        return times