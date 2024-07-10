class CaesarCipher:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def caesar(self, text, shift, direction):
        shift %= 26
        if direction == "decode":
            shift = -shift
        transformed_text = ""
        for char in text:
            if char.isalpha():
                idx = (self.alphabet.index(char) + shift) % 26
                transformed_text += self.alphabet[idx]
            else:
                transformed_text += char
        return transformed_text

    def run_cipher(self):
        print("Welcome to the Caesar Cipher Funhouse!\n")
        while True:
            direction = self.get_input("Type 'encode' to encrypt your message, or 'decode' to decrypt it:\n", ['encode', 'decode'])
            if not direction:
                break
            text = self.get_input("Enter your message:\n")
            if not text:
                break
            shift = self.get_positive_integer_input("Enter the shift number:\n")
            if not shift:
                break
            result = self.caesar(text.lower(), shift, direction)
            print(f"\nHere's the {direction}d result: {result}\n")
            choice = self.get_input("Want to go again? Type 'yes' to continue, 'no' to exit:\n", ['yes', 'no'])
            if choice == 'no':
                print("\nGoodbye! Hope you had fun ciphering and deciphering!\n")
                break
            print("\nAlright, let's do this again!\n")

    @staticmethod
    def get_input(prompt, valid_options=None):
        while True:
            user_input = input(prompt).lower()
            if valid_options and user_input not in valid_options:
                print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")
            else:
                return user_input

    @staticmethod
    def get_positive_integer_input(prompt):
        while True:
            user_input = input(prompt)
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Invalid input. Please enter a valid positive integer.")

# Usage
if __name__ == "__main__":
    cipher = CaesarCipher()
    cipher.run_cipher()
