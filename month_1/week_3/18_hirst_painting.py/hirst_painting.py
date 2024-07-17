# import colorgram

#  rgb_colors = []
# colors = colorgram.extract('image.jpg', 50)
# for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [
    (237, 238, 243), 
    (239, 238, 234), 
    (235, 240, 237), 
    (241, 233, 238), 
    (192, 156, 118), 
    (131, 160, 181), 
    (123, 90, 73), 
    (59, 101, 130), 
    (134, 73, 87), 
    (236, 205, 107), 
    (135, 167, 150), 
    (183, 142, 154), 
    (135, 23, 48), 
    (67, 113, 91), 
    (191, 99, 84), 
    (25, 53, 79), 
    (73, 33, 47), 
    (137, 150, 92), 
    (64, 48, 40), 
    (43, 59, 108), 
    (161, 107, 117), 
    (35, 56, 49), 
    (92, 150, 116), 
    (215, 179, 189), 
    (73, 145, 175), 
    (16, 94, 103), 
    (162, 201, 213), 
    (223, 176, 169), 
    (96, 49, 46), 
    (96, 129, 164), 
    (26, 90, 85), 
    (182, 189, 207), 
    (174, 202, 191), 
    (71, 67, 50), 
    (232, 205, 14)
]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0: 
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()