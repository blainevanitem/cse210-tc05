import random
class Cutter:
    def __init__(self):
        self.word = ""
        self.empty_word = []
        self.parachuter = ["  ___  "," /___\ "," \   / ","  \ /  ","   0   ","  /|\  ","  / \  ","       ","^^^^^^^"]
    def blank_word(self,word):
        #Used to create a list with _ for each letter in word
        for i in range(0,len(word)):
            #For each letter in the word add _ to empty list
            self.empty_word.append("_")
    def get_word(self, word_list):
        # get word, save word to self.word
        self.word = word_list[(random.randint(0,len(word_list)- 1))]
        self.blank_word(self.word)
        return self.word
    def cut_parachute(self):
        
        '''
        for loop to see if letter in word.
        return true or false
        '''
        self.parachute.pop[0]
    def update_empty(self,guess):
        times = self.word.count(guess)
        
        space = self.word.index(guess)
        self.empty_word[space] = guess
        if times>1:
            for _ in range(1, times):
                space = word.index(self.guess,space)