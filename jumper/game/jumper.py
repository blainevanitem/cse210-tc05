
class Jumper:      

        
    def in_word(self,letter, word):
        '''
        compare letter to word
        '''
        self.guess = letter
        
        if word.count(letter) == 0:
            return False
        else:
            return True
            