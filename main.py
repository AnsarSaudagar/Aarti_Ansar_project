from game import Game

hangman = Game()
hangman.show_start()

while hangman.end == False:
    answer = input(f"Please Guess the letter ,U have {hangman.lives} lives remaining\n")
    hangman.check_letter(answer)