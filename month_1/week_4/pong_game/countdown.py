from turtle import Turtle

class Countdown(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.messages = ["Ready", "Set", "Go"]
        self.current_message = 0

    def show_countdown(self):
        """Displays countdown messages before the game starts."""
        self.clear()
        if self.current_message < len(self.messages):
            self.write(self.messages[self.current_message], align="center", font=("Courier", 36, "normal"))
            self.current_message += 1
            self.getscreen().ontimer(self.show_countdown, 1000)  
        else:
            self.clear()
            self.getscreen().ontimer(self.start_game, 1000)  

    def start_game(self):
        """Starts the game after countdown."""
        self.clear()
