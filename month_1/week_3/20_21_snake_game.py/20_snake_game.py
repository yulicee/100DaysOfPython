from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Very Hungry Snake Game")
screen.tracer(0)

# Create snake, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen to keyboard inputs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Add countdown function
def countdown():
    counter = Turtle()
    counter.hideturtle()
    counter.color("white")
    counter.penup()
    counter.goto(0, 0)
    for i in range(3, 0, -1):
        counter.write(f"{i}", align="center", font=("Arial", 48, "normal"))
        screen.update()
        time.sleep(1)
        counter.clear()
    counter.write("Go!", align="center", font=("Arial", 48, "normal"))
    screen.update()
    time.sleep(1)
    counter.clear()

# Initial setup
initial_speed = 0.2  # Slower initial speed
speed = initial_speed

# Countdown before game starts
countdown()

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        # Increase speed as the score increases
        speed = initial_speed * (0.9 ** scoreboard.score)
    
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
