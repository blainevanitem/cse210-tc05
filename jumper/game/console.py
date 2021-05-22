class Console:


    def display_parachuter(self,parachuter):
        print("")
        for x in range(0,len(parachuter)):
            print(parachuter[x])
    
    def display_wordspace(self,list):
        print(" ".join(list))
        
    def display_message(self, message):
        guess = input(message)

        return guess

    def display_answer(self,answer):
        print("The word was: " + answer)

    