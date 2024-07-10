from calc_art import logo
import random

def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

def exit_calculator():
  print("Thanks for using the wackiest calculator in town! Have a great day! 🎉")
  exit()

def calculator():
  print(logo)
  print("Welcome to the wackiest calculator in town! 🎉")

  num1 = float(input("Enter the first number (be honest, we won't judge): "))
  for symbol in operations:
    print(symbol)
  
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation from the symbols above (choose wisely): ")
    num2 = float(input("Enter the second number (make it count): "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"Did you know? {random.choice(['Elephants can’t jump.', 'Bananas are berries, but strawberries aren’t!', 'Octopuses have three hearts.'])}")
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    next_step = input(f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, or 'exit' to leave the calculator: ").lower()
    if next_step == 'y':
      num1 = answer
      print("Alright, let's keep the fun going! 🎢")
    elif next_step == 'n':
      should_continue = False
      print("Time for a fresh start! 🚀")
      calculator()
    elif next_step == 'exit':
      should_continue = False
      exit_calculator()

calculator()
