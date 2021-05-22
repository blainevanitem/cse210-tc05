import random
class Cutter:
    """ A manipulative person who is willing to cut the parachute off another persons back
    if they cannot guess the word that they are thinking of. The responsibility of this class 
    is to store the word and check if the player is guessing correctly and cut the 
    parachute if the guess is wrong.

    Stereotype:
        Information Holder

    Attributes:
        word (string): A placeholder for the word to be guessed.
        empty_word (list): A placeholder for the empty list that will hold the correct guessed letters
        wrong_guess (integer): A placeholder for how many wrong guesses have been made
        incorrect (boolean): If the player is incorrect or not in thier guess
    """
    def __init__(self):
        self.word = ""
        self.empty_word = []
        self.wrong_guess = 0
        self.incorrect = False    

    def blank_word(self,word):
        #Used to create a list with _ for each letter in word
        for i in range(0,len(word)):
            #For each letter in the word add _ to empty list
            self.empty_word.append("_")

    def get_word(self, word_list):
        # get word, save word to self.word
        self.word = word_list[random.randint(0,len(word_list)-1)]
        self.word = self.word.strip()
        self.blank_word(self.word)
        self.word_length = len(self.word)
        return self.word

    def cut_parachute(self,guess,parachuter):
        #if the guess is wrong, cut it. If the length of parachure index is 5 then end and put x in face. If the player wins then end game.
        for x in range((len(self.word))):
            if(guess != self.word[x]):
                self.incorrect = True
            elif(guess == self.word[x]):
                self.incorrect = False
                break
        if(self.incorrect):
            parachuter.pop(0)
            self.wrong_guess += 1

        self.incorrect = False


    def end_of_line(self):
        if(self.wrong_guess == 4):
            return False
        else:
            return True

    def update_blanks(self,guess):
        for x in range((len(self.word))):
            if guess == self.word[x]:
                self.empty_word[x] = guess
