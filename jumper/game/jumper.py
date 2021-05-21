class Jumper:
    def __init__(self):
        empty_word = []

    def empty_word(self,word):
        for i in range(0,len(word)):
            self.empty_word.append("_")

    def get_guess(self):
        #call display guess_prompt
        message = "What letter do you think is in my word"
        return message
        
    def is_letter(self, guess, word):
        '''
        compare letter to word
        '''
        times = word.count(guess)
        
        space = word.index(guess)
        self.empty_word.insert(guess, space)
        if times > 1:
            for _ in range(1, times):
                space = word.index(guess,space)
                self.empty_word.insert(guess, space)



