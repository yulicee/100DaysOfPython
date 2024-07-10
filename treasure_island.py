import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to the next line after printing the text

def start_game():
    clear_screen()
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    print_with_delay("Searcher, welcome to Treasure Island.")
    print_with_delay("Many, many years ago, a great treasure was hidden in the depths of this island.")
    print_with_delay("Only you can find it.")
    print_with_delay("Will you be brave enough to start the hunt for the treasure?")
    choice1 = input("Type 'yes' or 'no': ").lower()
    if choice1 == "yes":
        print_with_delay("You are indeed very brave. Start your journey now.")
        print_with_delay("You are walking along the shoreline when you see a small island.")
        print_with_delay("You can either try and best the sea to reach the island or wait for a boat.")
        choice2 = input("Type 'swim' or 'wait': ").lower()
        if choice2 == "wait":
            print_with_delay("You meekly wait for a boat and arrive at the island well rested and refreshed.")
            print_with_delay("On the shore, you see a decrepit house with three doors.")
            print_with_delay("One door is red and made of wood, one door is yellow and designed of brick, and one door is blue and carved from stone.")
            choice3 = input("Which door do you choose? Choose carefully or this will be the end of your wanderings. Type 'red', 'yellow', or 'blue': ").lower()
            if choice3 == "red":
                print_with_delay("You open the red door and are burned by fire.")
                print_with_delay("Game over.")
                play_again()
            elif choice3 == "yellow":
                print_with_delay("You open the yellow door and find the treasure!")
                print_with_delay("Congratulations, you have won the game!")
                play_again()
            elif choice3 == "blue":
                print_with_delay("You open the blue door and are eaten by beasts.")
                print_with_delay("Game over.")
                play_again()
            else:
                print_with_delay("Invalid choice. Game over.")
                play_again()
        elif choice2 == "swim":
            print_with_delay("You attempt to swim to the island but are attacked by a gigantic trout.")
            print_with_delay("Game over.")
            play_again()
        else:
            print_with_delay("Invalid choice. Game over.")
            play_again()
    elif choice1 == "no":
        print_with_delay("You have wisely decided not to start the hunt for the treasure.")
        print_with_delay("Game over.")
        play_again()
    else:
        print_with_delay("Invalid choice. Game over.")
        play_again()

def play_again():
    choice = input("Do you want to start over? Type 'yes' or 'no': ").lower()
    if choice == "yes":
        start_game()
    else:
        print_with_delay("Thanks for playing. Goodbye!")
        input("Press Enter to exit...")

start_game()
