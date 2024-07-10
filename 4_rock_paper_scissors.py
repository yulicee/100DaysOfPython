import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

def get_user_choice():
    valid_choices = {
        "1": "rock",
        "2": "paper",
        "3": "scissors"
    }
    print("Enter your choice: 1 for rock, 2 for paper, 3 for scissors")
    user_input = input("Your choice: ").strip()
    while user_input not in valid_choices:
        print("Invalid choice. Must be 1 (rock), 2 (paper) or 3 (scissors)!")
        user_input = input("Your choice: ").strip()
    return valid_choices[user_input]

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", None
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!", "user"
    else:
        return "Computer wins!", "computer"

def get_num_rounds():
    while True:
        try:
            num_rounds = int(input("Enter number of rounds to play (default 3): ").strip() or "3")
            if num_rounds <= 0:
                print("Number of rounds must be greater than zero.")
            else:
                return num_rounds
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def play_game(num_rounds=3):
    print("Welcome to Rock, Paper, Scissors!")
    user_wins = 0  # Initialize user wins counter
    computer_wins = 0  # Initialize computer wins counter
    
    for game_counter in range(1, num_rounds + 1):
        print(f"Game {game_counter}:")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose:\n{choices[user_choice]}")
        print(f"Computer chose:\n{choices[computer_choice]}")
        
        result, winner = determine_winner(user_choice, computer_choice)
        print(result)
        
        if winner == "user":
            user_wins += 1
        elif winner == "computer":
            computer_wins += 1
        
        print(f"User wins: {user_wins}, Computer wins: {computer_wins}")
        print()

    print("\nGame Over!")
    if user_wins > computer_wins:
        print("Congratulations! You are the final winner!")
    elif computer_wins > user_wins:
        print("Computer is the final winner. Better luck next time!")
    else:
        print("It's a tie! No overall winner.")

if __name__ == "__main__":
    num_rounds = get_num_rounds()
    play_game(num_rounds)

