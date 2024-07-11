import time

# Conversion constants for wizard currency
GALLEON_TO_SICKLE = 17
SICKLE_TO_KNUT = 29

# Menu of magical drinks with ingredients, cost, and units
MENU = {
    "butterbrew": {
        "ingredients": {
            "essence_of_firewhiskey": 50,
            "ground_dragon_claw": 18,
        },
        "cost_knuts": 105,  # Total cost in Knuts
        "unit": {
            "essence_of_firewhiskey": "ml",
            "ground_dragon_claw": "g",
        }
    },
    "pumpkin_latte": {
        "ingredients": {
            "moonlight_pumpkin_extract": 200,
            "frothed_unicorn_milk": 150,
            "crushed_pixie_wings": 24,
        },
        "cost_knuts": 174,  # Total cost in Knuts
        "unit": {
            "moonlight_pumpkin_extract": "units",
            "frothed_unicorn_milk": "units",
            "crushed_pixie_wings": "units",
        }
    },
    "dragonfire_cappuccino": {
        "ingredients": {
            "liquid_inferno_essence": 250,
            "dragon_breath_froth": 100,
            "powdered_phoenix_feather": 24,
        },
        "cost_knuts": 203,  # Total cost in Knuts
        "unit": {
            "liquid_inferno_essence": "ml",
            "dragon_breath_froth": "ml",
            "powdered_phoenix_feather": "g",
        }
    }
}

# Initial profit and available resources
total_profit_knuts = 0
initial_resources = {
    "essence_of_firewhiskey": 300,
    "ground_dragon_claw": 200,
    "moonlight_pumpkin_extract": 100,
    "frothed_unicorn_milk": 150,
    "crushed_pixie_wings": 100,
    "liquid_inferno_essence": 300,
    "dragon_breath_froth": 200,
    "powdered_phoenix_feather": 100,
}
resources = initial_resources.copy()

def validate_integer_input(prompt):
    """Validates and returns an integer input from the user."""
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 0:
                raise ValueError("Input must be a positive magical number.")
            return user_input
        except ValueError as e:
            print(f"Oops! {e}. Please enter a valid positive magical number.")

def display_menu():
    """Displays the menu options to the user."""
    print("\nWe are grateful you have chosen our humble establishment! 🍺🪄")
    print("Behold our magical menu:")
    for idx, (drink, details) in enumerate(MENU.items(), start=1):
        cost_galleons = details["cost_knuts"] // (GALLEON_TO_SICKLE * SICKLE_TO_KNUT)
        cost_sickles = (details["cost_knuts"] % (GALLEON_TO_SICKLE * SICKLE_TO_KNUT)) // SICKLE_TO_KNUT
        cost_knuts = details["cost_knuts"] % SICKLE_TO_KNUT
        print(f"{idx}. {drink.capitalize()} - {cost_galleons} Galleons, {cost_sickles} Sickles, {cost_knuts} Knuts")

def calculate_min_refill(drink_choice):
    """Calculate and display the minimum refill amount required based on selected drink."""
    drink_name = list(MENU.keys())[drink_choice]
    ingredients = MENU[drink_name]["ingredients"]

    print("\nHmm... I sense a need for replenishment:")
    for item, quantity in ingredients.items():
        if resources[item] < quantity:
            refill_amount = quantity - resources[item]
            print(f"We're running low on {item.replace('_', ' ')}... {refill_amount} {MENU[drink_name]['unit'][item]} should suffice.")

def process_payment(cost_knuts):
    """Processes the payment from the user and returns the change."""
    print(f"\nThe cost? A mere {cost_knuts // (GALLEON_TO_SICKLE * SICKLE_TO_KNUT)} Galleons, {(cost_knuts % (GALLEON_TO_SICKLE * SICKLE_TO_KNUT)) // SICKLE_TO_KNUT} Sickles, and {cost_knuts % SICKLE_TO_KNUT} Knuts, good sir or madam.")
    galleons = validate_integer_input("Enter the Galleons: ")
    sickles = validate_integer_input("Enter the Sickles: ")
    knuts = validate_integer_input("Enter the Knuts: ")

    total_paid_knuts = galleons * GALLEON_TO_SICKLE * SICKLE_TO_KNUT + sickles * SICKLE_TO_KNUT + knuts
    change = total_paid_knuts - cost_knuts

    if change < 0:
        print("Insufficient funds, you say? Please, provide the exact amount.")
        return process_payment(cost_knuts)
    else:
        change_galleons = change // (GALLEON_TO_SICKLE * SICKLE_TO_KNUT)
        change_sickles = (change % (GALLEON_TO_SICKLE * SICKLE_TO_KNUT)) // SICKLE_TO_KNUT
        change_knuts = change % SICKLE_TO_KNUT
        print(f"Your generosity knows no bounds! Change to return: {change_galleons} Galleons, {change_sickles} Sickles, and {change_knuts} Knuts.")
        time.sleep(2)

        return change

def make_drink(choice):
    """Prepares and serves the selected drink."""
    drink_name = list(MENU.keys())[choice]
    ingredients = MENU[drink_name]["ingredients"]
    cost_knuts = MENU[drink_name]["cost_knuts"]

    print(f"\nOne {drink_name.capitalize()} coming right up!")
    time.sleep(2)  # Simulate preparation time

    # Check if all required ingredients are available
    if all(resources[item] >= quantity for item, quantity in ingredients.items()):
        # Deplete resources
        for item, quantity in ingredients.items():
            resources[item] -= quantity
        print(f"Here is your {drink_name.capitalize()}! Enjoy your magical concoction. 🌟")
        time.sleep(2)
        return cost_knuts
    else:
        print("Alas! We're fresh out of ingredients for that brew.")
        calculate_min_refill(choice)
        refill_choice = input("Would you like to refill any of the above ingredients? (yes/no): ").strip().lower()
        if refill_choice == "yes":
            refill_resources(ingredients, drink_name)
            # Try making the drink again after refill
            return make_drink(choice)
        else:
            print("Let's whisk you back to the menu, shall we?")
            time.sleep(2)
            return 0

def refill_resources(ingredients, drink_name):
    """Refills the necessary resources based on user input."""
    print("\nRefilling resources...")
    for item, quantity in ingredients.items():
        if resources[item] < quantity:
            refill_amount = validate_integer_input(f"Enter the amount to refill {item.replace('_', ' ')} ({MENU[drink_name]['unit'][item]}): ")
            resources[item] += refill_amount
    print("Resources have been replenished. Onward with the magic!")
    time.sleep(2)

def display_machine_status():
    """Displays the current status of the coffee machine."""
    total_galleons = total_profit_knuts // (GALLEON_TO_SICKLE * SICKLE_TO_KNUT)
    total_sickles = (total_profit_knuts % (GALLEON_TO_SICKLE * SICKLE_TO_KNUT)) // SICKLE_TO_KNUT
    total_knuts = total_profit_knuts % SICKLE_TO_KNUT

    print("\nBehold! The current state of our magical apparatus:")
    print(f"Total Profit: {total_galleons} Galleons, {total_sickles} Sickles, and {total_knuts} Knuts")
    print("Resources at hand:")
    for item, quantity in resources.items():
        print(f"{item.replace('_', ' ')}: {quantity} units")
    time.sleep(3)

# Main program loop
print("Welcome, welcome, to the illustrious Three Broomsticks! 🍺🪄")
while True:
    display_menu()
    choice = validate_integer_input("\nPlease select from amongst our phenomenal potions (1-3) or enter 0 to depart: ")

    if choice == 0:
        print("\nFare thee well, kind traveler. Until our paths converge once more! ✨")
        break

    try:
        drink_cost = MENU[list(MENU.keys())[choice - 1]]["cost_knuts"]
        change = process_payment(drink_cost)
        if change >= 0:
            total_profit_knuts += drink_cost
            make_drink(choice - 1)
            show_status = input("\nWould you like to witness the grandeur of our machine? (yes/no): ").strip().lower()
            if show_status == "yes":
                display_machine_status()
            return_menu = input("\nDo you yearn for more magical experiences? (yes/no): ").strip().lower()
            if return_menu != "yes":
                print("\nThank you for gracing us with your presence. May your days be filled with magic and wonder! ✨")
                break
        else:
            print("\nPray, select again. The world of magic awaits!")
    except IndexError:
        print("\nYour selection is but a figment of your imagination. Please select a valid option.")
    except KeyboardInterrupt:
        print("\nAh, a swift exit! Until our paths converge once more. Farewell!")
        break
