import random
import os
from blackjack_art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    # Check for blackjack (21 with 2 cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # Convert all aces from 11 to 1 as needed
    num_aces = cards.count(11)
    total_score = sum(cards)
    
    while total_score > 21 and num_aces:
        total_score -= 10
        num_aces -= 1
    
    return total_score

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "draw"
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "lose"
    elif user_score == 0:
        return "win"
    elif user_score > 21:
        return "lose"
    elif computer_score > 21:
        return "win"
    elif user_score > computer_score:
        return "win"
    else:
        return "lose"

def play_round(round_num):
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    
    result = compare(user_score, computer_score)
    if result == "win":
        print(f"Round {round_num}: Congratulations! You win this round! 🎉")
    elif result == "lose":
        print(f"Round {round_num}: Sorry, you lose this round. 😢")
    else:
        print(f"Round {round_num}: It's a draw this round. 😐")
    
    return result

clear()
print(logo)

user_wins = 0
computer_wins = 0
while True:
    rounds_to_play = input("How many rounds of Blackjack do you want to play? ")
    if rounds_to_play.isdigit() and int(rounds_to_play) > 0:
        break
    else:
        print("Please enter a valid number of rounds.")

for round_num in range(1, int(rounds_to_play) + 1):
    clear()
    print(f"Round {round_num} / {rounds_to_play}")
    result = play_round(round_num)
    if result == "win":
        user_wins += 1
    elif result == "lose":
        computer_wins += 1

    print(f"\nScore after Round {round_num}: You: {user_wins} - Computer: {computer_wins}\n")
    input("Press Enter to continue...")

clear()
print(f"Final score after {rounds_to_play} rounds:")
print(f"You: {user_wins} - Computer: {computer_wins}")

if user_wins > computer_wins:
    print("Congratulations! You win this game! 🎉")
elif computer_wins > user_wins:
    print("Sorry, the computer wins this game. 😢")
else:
    print("It's a tie. No one won this game. 😐")

input("Press Enter to exit...")
