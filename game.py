import requests
from drawing import stages, logo

class Game:
    lives = len(stages)
    word = None
    guessing_word = None
    end = False
    URL = "https://random-word-api.herokuapp.com/word"

    def __init__(self):
        
        self.word = self.fetch_random_word()
        self.guessing_word = "_" * len(self.word)

    def fetch_random_word(self):
        """
        #### Getting the random word from the api call
        """
        fetch_word = requests.get(self.URL)
        return fetch_word.json()[0]
    
    def show_start(self):
        """
        It will show the title of the game and basic details
        """
        print(logo)
        print(f"You will get total of {self.lives} chances to guess the word or u will have to hang till death 😈")
        print("_ " * len(self.word))

    def check_letter(self, letter):

        """
        It will check the input letter if its correct or not, if its correct then it will show output 
        """
        if letter in self.word:
            num_arr = [i for i in range(len(self.word)) if self.word[i] == letter]
            if len(num_arr) > 0:
                guess_arr = list(self.guessing_word)

                for i in range(len(guess_arr)):
                    if i in num_arr:
                        guess_arr[i] = letter
                self.guessing_word = ''.join(guess_arr)
                print(' '.join(guess_arr))

                #check if all letter are guessed
                if "_" not in self.guessing_word:
                    self.end = True
        else: 
            self.lives -=1
            print(stages[self.lives])

            # Check if the user still have lives remaining
            if self.lives < 1:
                self.end = True
                print(f"Your dead 💀, The word was {self.word}")
                return
            else:
                # print(self.guessing_word)
                print(' '.join(list(self.guessing_word)))
                print(f"You lost a live u have {self.lives} lives remaining")
