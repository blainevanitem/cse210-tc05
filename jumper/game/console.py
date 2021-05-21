class Console:


    def display_parachuter(self,list):

        for i in range (len(list)):
            print(list[i])
    
    def display_wordspace(self,list):

        for i in range (len(list)):
            print(list[i],end='')
            print(" ",end='')
        print("")
    def display_message(self, message):
        guess = input(message)

        return guess
    