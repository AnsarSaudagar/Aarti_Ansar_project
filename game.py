import requests
from drawing import stages, logo

class Game:
    lives = len(stages)
    word = None
    guessing_word = None
    end = False

    def __init__(self, word):
        self.word = word
        self.guessing_word = "_" * len(self.word)

    def fetch_random_word(self):
        # Getting the word from the api call
        fetch_word = requests.get(self.URL_WORD)
        self.word = fetch_word.json()[0]
    
    def show_start(self):
        print(logo)
        print(f"You will get total of {self.lives} chances to guess the word or u will have to hang till death 😈")
        print("_ " * len(self.word))

    def check_letter(self, letter):
        check = False
        if letter in self.word:
            num_arr = [i for i in range(len(self.word)) if self.word[i] == letter]
            # print(num_arr)
            if len(num_arr) > 0:
                guess_arr = list(self.guessing_word)

                for i in range(len(guess_arr)):
                    if i in num_arr:
                        guess_arr[i] = letter
                self.guessing_word = ''.join(guess_arr)
                print(' '.join(guess_arr))
        else: 
            self.lives -=1
            print(stages[self.lives])
            if self.lives < 1:
                self.end = True
                print(f"Your dead 💀, The word was {self.word}")
                return
            else:
                print(self.guessing_word)
                print(f"You lost a live u have {self.lives} lives remaining")
