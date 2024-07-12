# main.py

import os
import time
from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

def main():
    menu = Menu()
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker({
        "essence_of_firewhiskey": 300,
        "ground_dragon_claw": 200,
        "moonlight_pumpkin_extract": 100,
        "frothed_unicorn_milk": 150,
        "crushed_pixie_wings": 100,
        "liquid_inferno_essence": 300,
        "dragon_breath_froth": 200,
        "powdered_phoenix_feather": 100,
    })

    print("Welcome, welcome, to the illustrious Three Broomsticks! 🍺🪄")

    while True:
        menu.display_menu()
        choice = money_machine.validate_integer_input("\nPlease select from amongst our phenomenal potions (1-3) or enter 0 to depart: ")

        if choice == 0:
            print("\nFare thee well, kind traveler. Until our paths converge once more! ✨")
            break

        try:
            drink_name = list(menu.drinks.keys())[choice - 1]
            drink = menu.get_drink(drink_name)
            change = money_machine.process_payment(drink.cost_knuts)
            if change >= 0:
                coffee_maker.make_drink(drink)
                show_status = input("\nWould you like to witness the grandeur of our machine? (yes/no): ").strip().lower()
                if show_status == "yes":
                    coffee_maker.display_status()
                return_menu = input("\nDo you yearn for more magical experiences? (yes/no): ").strip().lower()
                if return_menu != "yes":
                    print("\nThank you for gracing us with your presence. May your days be filled with magic and wonder! ✨")
                    break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
            else:
                print("\nPray, select again. The world of magic awaits!")
        except IndexError:
            print("\nYour selection is but a figment of your imagination. Please select a valid option.")
        except KeyboardInterrupt:
            print("\nAh, a swift exit! Until our paths converge once more. Farewell!")
            break

if __name__ == "__main__":
    main()
