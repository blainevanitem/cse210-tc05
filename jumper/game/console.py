class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """

    def display_parachuter(self,parachuter):
        #Display list with new lines for each index
        print("")
        for x in range(0,len(parachuter)):
            print(parachuter[x])
    
    def display_wordspace(self,list):
        #Display list with spaces between each index
        print(" ".join(list))
        
    def display_message(self, message):\
        #Display string and recieve input
        guess = input(message)
        return guess

    def display_answer(self,answer):
        #Display answer
        print("The word was: " + answer)

    