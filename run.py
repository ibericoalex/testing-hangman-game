import os
import random
from words import word_list
from hangman_pics import HANGMAN_PICS

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_word(difficulty):
    if difficulty == "1":
        return random.choice([word for word in word_list if len(word) == 3])
    elif difficulty == "2":
        return random.choice([word for word in word_list if 4 <= len(word) <= 6])
    else:
        return random.choice([word for word in word_list if len(word) > 7])

def play_game(username):
    clear_screen()
    print(f"\nHello, {username}! Choose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty = input("Enter a number (1/2/3): ")
    while difficulty not in ["1", "2", "3"]:
        difficulty = input(f"Invalid choice, {username}. Please choose again (1/2/3): ")

    word = get_word(difficulty).upper()
    guessed = ["_"] * len(word)
    incorrect_guesses = 0
    max_guesses = {"1": 5, "2": 6, "3": 8}
    incorrect_guessed_letters = []

    while "_" in guessed and incorrect_guesses < max_guesses[difficulty]:
        clear_screen()
        print(HANGMAN_PICS[incorrect_guesses])
        print(" ".join(guessed))
        print(f"Incorrectly guessed letters, {username}: {', '.join(incorrect_guessed_letters)}")
        print(f"Attempts left, {username}: {max_guesses[difficulty] - incorrect_guesses}")
        guess = input("Guess a letter: ").upper()

        if guess in guessed or guess in incorrect_guessed_letters:
            print(f"You've already guessed that letter, {username}. Try again.")
            continue

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            incorrect_guesses += 1
            incorrect_guessed_letters.append(guess)

    print(HANGMAN_PICS[incorrect_guesses])
    if "_" not in guessed:
        print(f"Congratulations, {username}! You guessed the word: {word}")
    else:
        print(f"Sorry, {username}. You ran out of guesses. The word was: {word}")

def main():
    print("Welcome to Hangman!")
    username = input("Enter your username: ")
    print(random.choice([f"Let's have some fun, {username}!", f"Ready to guess, {username}?", f"Can you beat the game, {username}?"]))

    while True:
        print(f"\nHello, {username}! What would you like to do?")
        print("1. Start Game")
        print("2. View Rules")
        print("3. Exit Game")
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            play_game(username)
        elif choice == "2":
            print("\nRules:")
            print("1. Choose a difficulty level by entering a number.")
            print("2. Guess letters to uncover the hidden word.")
            print("3. You have a limited number of incorrect guesses based on the difficulty.")
            print("4. If you guess the word before running out of guesses, you win!")
        elif choice == "3":
            print(f"Thanks for playing, {username}! Goodbye!")
            break
        else:
            print(f"Invalid choice, {username}. Please choose again.")

if __name__ == "__main__":
    main()