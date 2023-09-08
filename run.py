import random

def select_word(words):
    return random.choice(words)

words = ["tiger", "three", "tree", "abrupt", "acclaim", "adhere", "advice", "afflict", "agitate", "allocate", "ambition", "amplify", "anecdote"]
remaining_attempts = 6
guessed_letter = ""

print(select_word(words))