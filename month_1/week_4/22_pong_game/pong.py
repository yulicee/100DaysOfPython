import time
from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from countdown import Countdown
from timer import Timer  

# Setup screen
screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create paddles, ball, scoreboard, countdown, and timer
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
countdown = Countdown()
timer = Timer()  

# Game state
is_paused = False
game_started = False
start_time = time.time()  

def toggle_pause():
    global is_paused
    if is_paused:
        is_paused = False
        clear_pause_menu()
    else:
        is_paused = True
        show_pause_menu()

def show_pause_menu():
    """Display the pause menu with resume and quit options."""
    pause_menu.clear()
    pause_menu.write("Paused. Press 'space' to resume or 'q' to quit.", align="center", font=("Courier", 18, "normal"))
    screen.onkeypress(resume_game, "space")  
    screen.onkeypress(quit_game, "q")  

def clear_pause_menu():
    """Clear the pause menu from the screen."""
    pause_menu.clear()
    screen.onkeypress(toggle_pause, "space")  

def resume_game():
    """Resume the game if spacebar is pressed while paused."""
    global is_paused
    is_paused = False
    clear_pause_menu()

def quit_game():
    screen.bye()

def check_collision(ball, paddle):
    """Checks for collision between the ball and the paddle."""
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    ball_radius = ball.shapesize()[0] * 10 / 2
    ball_left = ball_x - ball_radius
    ball_right = ball_x + ball_radius
    ball_top = ball_y + ball_radius
    ball_bottom = ball_y - ball_radius

    paddle_x = paddle.xcor()
    paddle_y = paddle.ycor()
    paddle_width = paddle.shapesize()[1] * 10 / 2
    paddle_height = paddle.shapesize()[0] * 10 / 2
    paddle_left = paddle_x - paddle_width
    paddle_right = paddle_x + paddle_width
    paddle_top = paddle_y + paddle_height
    paddle_bottom = paddle_y - paddle_height

    if (ball_right > paddle_left and
        ball_left < paddle_right and
        ball_top > paddle_bottom and
        ball_bottom < paddle_top):
        return True

    return False

def handle_collision(ball, paddle):
    """Handle ball collision with the paddle."""
    if ball.x_move > 0:  
        ball.setx(paddle.xcor() - (ball.shapesize()[0] * 10 / 2 + paddle.shapesize()[1] * 10 / 2))
    elif ball.x_move < 0:  
        ball.setx(paddle.xcor() + (ball.shapesize()[0] * 10 / 2 + paddle.shapesize()[1] * 10 / 2))

    ball.bounce_x()

def start_game():
    global game_started
    game_started = True

countdown.start_game = start_game  
countdown.show_countdown()  

pause_menu = Turtle()
pause_menu.hideturtle()
pause_menu.penup()
pause_menu.color("white")
pause_menu.goto(0, 0)

screen.listen()
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(toggle_pause, "space")  
screen.onkeypress(quit_game, "q")

# Main game loop
last_update_time = time.time()  
while True:
    screen.update()  

    current_time = time.time()
    delta_time = current_time - last_update_time  
    last_update_time = current_time

    if game_started and not is_paused:
        ball.move() 
        
        if check_collision(ball, left_paddle):
            handle_collision(ball, left_paddle)
        
        if check_collision(ball, right_paddle):
            handle_collision(ball, right_paddle)
        
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.bounce_y()

        if ball.xcor() > 400:
            ball.reset_position()
            scoreboard.l_point()  

        if ball.xcor() < -400:
            ball.reset_position()
            scoreboard.r_point()  

        timer.update_time(delta_time) 
