import random

# Word List
words = [
    "abrupt", "acclaim", "adhere", "advice", "afflict", "agitate", "allocate", 
    "ambition", "amplify", "anecdote"
]

# Choose Difficulty Level
def choose_difficulty():
    print("\nChoose a difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter your choice (1/2/3): ")
    return choice

# Display the current state of the word
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

# ASCII Art for Hangman
def display_hangman(incorrect_guesses):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    print(stages[incorrect_guesses])

# Main Game Loop
def play_game():
    difficulty = choose_difficulty()
    if difficulty == "1":
        max_guesses = 5
    elif difficulty == "2":
        max_guesses = 7
    else:
        max_guesses = 9

    word_to_guess = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0

    while True:
        print(display_word(word_to_guess, guessed_letters))
        display_hangman(incorrect_guesses)
        guess = input("Guess a letter: ").lower()
        
        if guess in word_to_guess:
            guessed_letters.append(guess)
        else:
            incorrect_guesses += 1
            print(f"Incorrect! You have {max_guesses - incorrect_guesses} lives left.")
        
        if set(word_to_guess) <= set(guessed_letters):
            print(f"{username}, congratulations! You've successfully guessed the word!")
            break
        elif incorrect_guesses == max_guesses:
            print(f"Sorry, {username}, you've run out of guesses. The correct word was {word_to_guess}. Better luck next time!")
            break

# View Rules
def view_rules():
    print("\nRules of Hangman:")
    print("1. A random word will be chosen.")
    print("2. You have to guess the word letter by letter.")
    print("3. For each incorrect guess, a part of the hangman will be drawn.")
    print("4. The game ends when you guess the word correctly or the hangman is fully drawn.")
    print("5. The number of guesses allowed depends on the chosen difficulty level.")
    input("\nPress Enter to return to the main menu.")

# Main Menu
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Start Game")
        print("2. View Rules")
        print("3. Exit Game")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            play_game()
        elif choice == "2":
            view_rules()
        elif choice == "3":
            print(f"Thanks for playing, {username}! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Main Execution
if __name__ == "__main__":
    username = input("Please enter your username: ")
    print(f"Welcome, {username}!")
    main_menu()
