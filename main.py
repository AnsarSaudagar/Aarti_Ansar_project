from game import Game
import requests

# word = "https://random-word-api.herokuapp.com/word"

# fetch_word = requests.get(word)
fetch_word = "ansar"

# print(fetch_word)
hangman = Game(fetch_word)
hangman.show_start()

while hangman.end == False:
    answer = input(f"Please Guess the letter ,U have {hangman.lives} lives remaining\n")
    hangman.check_letter(answer)