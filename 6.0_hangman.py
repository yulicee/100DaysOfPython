import random
import sys
import os
from hangman_words import word_list
from hangman_logo import logo, stages

def clear_screen():
    """Clears the console screen."""
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def select_random_word(word_list):
    """Selects a random word from the given word list."""
    return random.choice(word_list)

def print_current_status(display, guessed_letters, lives):
    """Prints the current game status including the hangman, guessed letters, and word display."""
    clear_screen()
    print(logo)
    print(' '.join(display))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(stages[lives])

def get_guess(guessed_letters):
    """Prompts the player to guess a letter, ensuring the input is valid and hasn't been guessed before."""
    while True:
        guess = input("Guess a letter: ").lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print(f"You've already guessed '{guess}'. Try again.")
            else:
                return guess
        else:
            print("Please enter a single alphabetical character.")

def play_game():
    """Main function to play the Hangman game."""
    while True:
        chosen_word = select_random_word(word_list)
        word_length = len(chosen_word)
        end_of_game = False
        lives = 6
        guessed_letters = []
        display = ["_" for _ in range(word_length)]

        while not end_of_game:
            print_current_status(display, guessed_letters, lives)
            guess = get_guess(guessed_letters)
            guessed_letters.append(guess)

            if guess in chosen_word:
                for position in range(word_length):
                    if chosen_word[position] == guess:
                        display[position] = guess
            else:
                print(f"'{guess}' is not in the word. You lose a life!")
                lives -= 1
                if lives == 0:
                    end_of_game = True

            if "_" not in display:
                end_of_game = True

        print_current_status(display, guessed_letters, lives)
        if lives == 0:
            print(f"Sorry, you lost! The word was '{chosen_word}'.")
        else:
            print("Congratulations, you guessed the word!")

        play_again = input("Do you want to play again? (yes/no, default=yes): ").strip().lower() or "yes"
        if play_again != "yes":
            break

    print("Thanks for playing Hangman! See you next time!")

if __name__ == "__main__":
    play_game()
