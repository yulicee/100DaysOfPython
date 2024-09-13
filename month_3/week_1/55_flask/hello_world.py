from flask import Flask

app = Flask(__name__)

# Define the make_bold decorator
def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

# Define the make_emphasis decorator
def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

# Define the make_underline decorator
def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGc2NXE5bnMxNDYxYmV6ZGQ3Y2ZubWFodGJ2NjVvd2poZTZnNzNqcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/11s7Ke7jcNxCHS/200.webp" width=200>'

# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"

# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
