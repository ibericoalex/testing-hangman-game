import random
from words import words



def generate_random_word(words):
    """
    Function to select a random word from the list and
    return the letter in uppercase.
    """
    word = random.choice(words)
    return word.upper()

