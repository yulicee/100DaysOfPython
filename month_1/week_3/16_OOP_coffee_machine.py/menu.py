# menu.py
from prettytable import PrettyTable

class Drink:
    def __init__(self, name, ingredients, cost_knuts, unit):
        self.name = name
        self.ingredients = ingredients
        self.cost_knuts = cost_knuts
        self.unit = unit

class Menu:
    def __init__(self):
        self.drinks = {
            "butterbrew": Drink(
                "Butterbrew",
                {"essence_of_firewhiskey": 50, "ground_dragon_claw": 18},
                105,
                {"essence_of_firewhiskey": "ml", "ground_dragon_claw": "g"}
            ),
            "pumpkin_latte": Drink(
                "Pumpkin Latte",
                {"moonlight_pumpkin_extract": 200, "frothed_unicorn_milk": 150, "crushed_pixie_wings": 24},
                174,
                {"moonlight_pumpkin_extract": "units", "frothed_unicorn_milk": "units", "crushed_pixie_wings": "units"}
            ),
            "dragonfire_cappuccino": Drink(
                "Dragonfire Cappuccino",
                {"liquid_inferno_essence": 250, "dragon_breath_froth": 100, "powdered_phoenix_feather": 24},
                203,
                {"liquid_inferno_essence": "ml", "dragon_breath_froth": "ml", "powdered_phoenix_feather": "g"}
            )
        }

    def get_drink(self, name):
        return self.drinks.get(name)

    def display_menu(self):
        table = PrettyTable()
        table.field_names = ["#", "Drink", "Cost (Galleons)", "Cost (Sickles)", "Cost (Knuts)"]
        for idx, drink in enumerate(self.drinks.values(), start=1):
            cost_galleons = drink.cost_knuts // (17 * 29)
            cost_sickles = (drink.cost_knuts % (17 * 29)) // 29
            cost_knuts = drink.cost_knuts % 29
            table.add_row([idx, drink.name, cost_galleons, cost_sickles, cost_knuts])
        print("\nWe are grateful you have chosen our humble establishment! 🍺🪄")
        print("Behold our magical menu:")
        print(table)
