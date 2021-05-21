
class Jumper:
    def __init__(self):
        self.guess = ""        

        
    def is_letter(self,letter, word):
        '''
        compare letter to word
        '''
        self.guess = letter
        times = word.count(self.guess)
        
        
        for _ in range(0, times):
            space = word.index(self.guess,space)
            self.empty_word.insert(self.guess, space)
        if times == 0:
            return False
        else:
            return True