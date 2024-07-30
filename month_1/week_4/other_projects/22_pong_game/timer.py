from turtle import Turtle

class Timer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 240)  
        self.elapsed_time = 0
        self.update_time_display()

    def update_time(self, delta_time):
        """Update the elapsed time and display it."""
        self.elapsed_time += delta_time
        self.update_time_display()

    def update_time_display(self):
        """Update the displayed time."""
        minutes = int(self.elapsed_time // 60)
        seconds = int(self.elapsed_time % 60)
        self.clear()
        self.write(f"Time: {minutes:02}:{seconds:02}", align="center", font=("Courier", 18, "normal"))  
