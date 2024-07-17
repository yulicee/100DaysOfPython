from turtle import Turtle, Screen
import random
import time

def setup_turtle_race():
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.title("Turtle Race Game")
    return screen

def create_turtles(colors, y_positions):
    turtles = []
    for i in range(len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[i])
        turtles.append(new_turtle)
    return turtles

def display_finish_line():
    finish_line = Turtle()
    finish_line.penup()
    finish_line.goto(x=230, y=-100)
    finish_line.pendown()
    finish_line.goto(x=230, y=100)
    finish_line.hideturtle()

def countdown():
    countdown_turtle = Turtle()
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.goto(0, 0)
    for i in range(3, 0, -1):
        countdown_turtle.write(i, align="center", font=("Arial", 24, "normal"))
        time.sleep(1)
        countdown_turtle.clear()
    countdown_turtle.write("Go!", align="center", font=("Arial", 24, "normal"))
    time.sleep(1)
    countdown_turtle.clear()

def race(all_turtles):
    is_race_on = True
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                is_race_on = False
                return winning_color
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

def display_result(winning_color, user_bet, current_score, races_played):
    result_turtle = Turtle()
    result_turtle.hideturtle()
    result_turtle.penup()
    result_turtle.goto(0, 50)
    if winning_color == user_bet:
        result_turtle.write(f"You've won! The {winning_color} turtle is the winner!\nYour score: {current_score}\nRaces played: {races_played}\n\n", align="center", font=("Arial", 18, "normal"))
    else:
        result_turtle.write(f"You've lost! The {winning_color} turtle is the winner!\nYour score: {current_score}\nRaces played: {races_played}\n\n", align="center", font=("Arial", 18, "normal"))

def main():
    screen = setup_turtle_race()
    current_score = 0

    races = screen.numinput(title="Number of Races", prompt="How many races would you like to play?", minval=1, maxval=10)
    if races is None:
        screen.bye()
        return

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    color_options = ", ".join(colors)

    replay = True
    while replay:
        for race_number in range(int(races)):
            user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color ({color_options}): ")
            if user_bet is None:
                replay = False
                break

            y_positions = [-70, -40, -10, 20, 50, 80]
            all_turtles = create_turtles(colors, y_positions)
            display_finish_line()
            
            if user_bet:
                countdown()
                winning_color = race(all_turtles)
                if winning_color == user_bet:
                    current_score += 1

                display_result(winning_color, user_bet, current_score, race_number + 1)

                if race_number + 1 < races:
                    continue_game = screen.textinput(title="Next Race", prompt="Do you want to continue to the next race? (yes/no)").lower()
                    if continue_game != "yes":
                        replay = False
                        break
                else:
                    replay = screen.textinput(title="Game Over", prompt=f"Game over! Your final score: {current_score}\n\nDo you want to replay? (yes/no)").lower() == "yes"
                    if not replay:
                        break

                screen.clearscreen()

    screen.bye()

if __name__ == "__main__":
    main()
