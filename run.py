import random

def select_word(words):
    return random.choice(words)

def print_secret_word(secret_word):
    print(" _ " * len(secret_word))

words = ["tiger", "three", "tree", "abrupt", "acclaim", "adhere", "advice", "afflict", "agitate", "allocate", "ambition", "amplify", "anecdote"]
remaining_attempts = 6
guessed_letter = ""

print("Welcome to the Hangman Game! \n")
secret_word = select_word(words)
print_secret_word(secret_word)