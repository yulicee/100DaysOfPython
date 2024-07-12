# money_machine.py

import time

class MoneyMachine:
    GALLEON_TO_SICKLE = 17
    SICKLE_TO_KNUT = 29

    def __init__(self):
        self.total_profit_knuts = 0

    def validate_integer_input(self, prompt):
        while True:
            try:
                user_input = int(input(prompt))
                if user_input < 0:
                    raise ValueError("Input must be a positive magical number.")
                return user_input
            except ValueError as e:
                print(f"Oops! {e}. Please enter a valid positive magical number.")

    def process_payment(self, cost_knuts):
        print(f"\nThe cost? A mere {cost_knuts // (self.GALLEON_TO_SICKLE * self.SICKLE_TO_KNUT)} Galleons, {(cost_knuts % (self.GALLEON_TO_SICKLE * self.SICKLE_TO_KNUT)) // self.SICKLE_TO_KNUT} Sickles, and {cost_knuts % self.SICKLE_TO_KNUT} Knuts, good Sir or Madam.")
        galleons = self.validate_integer_input("Enter the Galleons: ")
        sickles = self.validate_integer_input("Enter the Sickles: ")
        knuts = self.validate_integer_input("Enter the Knuts: ")

        total_paid_knuts = galleons * self.GALLEON_TO_SICKLE * self.SICKLE_TO_KNUT + sickles * self.SICKLE_TO_KNUT + knuts
        change = total_paid_knuts - cost_knuts

        if change < 0:
            print("Insufficient funds, you say? Please, provide the exact amount.")
            return self.process_payment(cost_knuts)
        else:
            change_galleons = change // (self.GALLEON_TO_SICKLE * self.SICKLE_TO_KNUT)
            change_sickles = (change % (self.GALLEON_TO_SICKLE * self.SICKLE_TO_KNUT)) // self.SICKLE_TO_KNUT
            change_knuts = change % self.SICKLE_TO_KNUT
            print(f"Your generosity knows no bounds! Change to return: {change_galleons} Galleons, {change_sickles} Sickles, and {change_knuts} Knuts.")
            time.sleep(2)

            return change
