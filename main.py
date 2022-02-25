import turtle as t
import colorgram
import random


# rgb_colors = []
# colors = colorgram.extract("colorfulpic.jpeg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

tim = t.Turtle()
t.colormode(255)
color_list = [(62, 15, 28), (222, 146, 94), (165, 74, 39), (148, 17, 35), (22, 42, 60), (54, 96, 129), (131, 69, 90),
              (241, 208, 108), (155, 26, 14), (73, 28, 14), (219, 84, 56), (56, 121, 90), (93, 178, 209),
              (245, 228, 162), (111, 187, 151), (27, 48, 36), (199, 79, 99), (67, 163, 129), (37, 173, 194),
              (109, 233, 215), (48, 56, 102), (194, 131, 154), (104, 113, 177), (167, 138, 57), (78, 232, 242),
              (21, 82, 97), (33, 84, 62), (175, 240, 200), (86, 73, 25), (240, 173, 151)]


def draw_painting(num_dots):
    tim.hideturtle()
    tim.penup()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    tim.speed("fastest")
    for dot_count in range(1, num_dots + 1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


draw_painting(100)
screen = t.Screen()
screen.exitonclick()

