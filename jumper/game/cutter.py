from game.jumper import Jumper
import random
class Cutter:
    def __init__(self):
        self.word = ""
        self.empty_word = []        
        self.jumper = Jumper()
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
        if get_guess == True:
            return False
        else:
            self.parachute = self.parachute.pop[0]
            return True

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