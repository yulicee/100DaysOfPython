# coffee_maker.py

import time
from prettytable import PrettyTable

class CoffeeMaker:
    def __init__(self, initial_resources):
        self.resources = initial_resources
        self.total_profit_knuts = 0

    def make_drink(self, drink):
        print(f"\nOne {drink.name} coming right up!")
        time.sleep(2)  # Simulate preparation time

        if all(self.resources[item] >= quantity for item, quantity in drink.ingredients.items()):
            for item, quantity in drink.ingredients.items():
                self.resources[item] -= quantity
            print(f"Here is your {drink.name}! Enjoy your magical concoction. 🌟")
            self.total_profit_knuts += drink.cost_knuts
            return drink.cost_knuts
        else:
            print("Alas! We're fresh out of ingredients for that brew.")
            self.calculate_min_refill(drink)
            refill_choice = input("Would you like to refill any of the above ingredients? (yes/no): ").strip().lower()
            if refill_choice == "yes":
                self.refill_resources(drink)
                return self.make_drink(drink)
            else:
                print("Let's whisk you back to the menu, shall we?")
                return 0

    def calculate_min_refill(self, drink):
        table = PrettyTable()
        table.field_names = ["Ingredient", "Required Amount", "Current Amount", "Unit"]
        for item, quantity in drink.ingredients.items():
            if self.resources[item] < quantity:
                refill_amount = quantity - self.resources[item]
                table.add_row([item.replace('_', ' '), refill_amount, self.resources[item], drink.unit[item]])
        print("\nHmm... I sense a need for replenishment:")
        print(table)

    def refill_resources(self, drink):
        print("\nRefilling resources...")
        for item, quantity in drink.ingredients.items():
            if self.resources[item] < quantity:
                refill_amount = self.validate_integer_input(f"Enter the amount to refill {item.replace('_', ' ')} ({drink.unit[item]}): ")
                self.resources[item] += refill_amount
        print("Resources have been replenished. Onward with the magic!")

    def display_status(self):
        total_galleons = self.total_profit_knuts // (17 * 29)
        total_sickles = (self.total_profit_knuts % (17 * 29)) // 29
        total_knuts = self.total_profit_knuts % 29

        table = PrettyTable()
        table.field_names = ["Ingredient", "Quantity"]
        for item, quantity in self.resources.items():
            table.add_row([item.replace('_', ' '), quantity])
        print("\nBehold! The current state of our magical apparatus:")
        print(table)
        print(f"Total Profit: {total_galleons} Galleons, {total_sickles} Sickles, and {total_knuts} Knuts")

    def validate_integer_input(self, prompt):
        while True:
            try:
                user_input = int(input(prompt))
                if user_input < 0:
                    raise ValueError("Input must be a positive magical number.")
                return user_input
            except ValueError as e:
                print(f"Oops! {e}. Please enter a valid positive magical number.")
