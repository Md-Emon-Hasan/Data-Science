# guessing game
from ast import Not

secret_word = "emon"
guess_word = ""

while secret_word != guess_word:
    guess_word = input("Guess the secret secret word: ")
print("You Win")

# guessing game with limitation
secret_word = "emon"
guess_word = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess_word != secret_word and not (out_of_guess):
    if guess_count < guess_limit:
        guess_word = input("Guess the word: ")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("You win")
else:
    print("You lose")
    