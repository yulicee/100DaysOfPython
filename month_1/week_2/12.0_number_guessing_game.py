from random import randint
from number_art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high! Guess lower next time. 😅")
    elif guess < answer:
        print("Too low! Aim higher! 🚀")
    else:
        print(f"You got it! The answer was {answer}. Congratulations! 🎉")
        return True
    return False

def set_difficulty():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard' (default easy): ").strip().lower()
        if level == "" or level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Invalid input. Please enter 'easy' or 'hard'.")

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()
    guess = 0
    while turns > 0:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        
        while True:
            try:
                guess = int(input("Make a guess: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if check_answer(guess, answer, turns):
            break
        
        turns -= 1
        if turns == 0:
            print(f"Sorry, you've run out of guesses. The correct number was {answer}. Better luck next time! 🍀")
            break
        else:
            print("Guess again.")

    while True:
        play_again = input("\nDo you want to play again? Type 'yes' or 'no' (default yes): ").strip().lower()
        if play_again == "yes" or play_again == "":
            game()
            break
        elif play_again == "no":
            print("Thank you for playing! Come back soon for more guessing fun! 🎮")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

game()
