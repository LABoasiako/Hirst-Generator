import colorgram
import random
import turtle as turtle_module


def color_extractor(image, num=30):
    rgb_colors = []
    colors = colorgram.extract(image, num)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    return rgb_colors


def color_palette(color):
    turtle_module.colormode(255)
    turtle = turtle_module.Turtle()
    turtle.penup()
    turtle.hideturtle()
    turtle.speed("fastest")
    turtle.setheading(225)
    turtle.forward(400)
    turtle.setheading(0)
    for num in range(1, 9):
        turtle.fillcolor(color[num -1])
        turtle.begin_fill()
        turtle.forward(100)
        turtle.setheading(90)
        turtle.forward(250)
        turtle.setheading(180)
        turtle.forward(100)
        turtle.setheading(270)
        turtle.forward(250)
        turtle.end_fill()
        turtle.setheading(0)
        turtle.forward(50)
        turtle.setheading(270)
        turtle.forward(20)
        turtle.write("R  G  B", align="center", font=('Arial', 12, 'bold'))
        turtle.forward(20)
        turtle.write(str(color[num -1]), align="center", font=('Arial', 12, 'bold'))
        turtle.setheading(90)
        turtle.forward(40)
        turtle.setheading(0)
        turtle.forward(100)

        if num % 4 == 0:
            turtle.setheading(90)
            turtle.forward(300)
            turtle.setheading(180)
            turtle.forward(400)

    screen = turtle_module.Screen()
    screen.exitonclick()


def hirst_drawing_creation(rgb_colors):
    turtle_module.colormode(255)
    turtle = turtle_module.Turtle()
    turtle.speed("fastest")
    turtle.penup()
    turtle.hideturtle()
    color_list = rgb_colors
    turtle.setheading(225)
    turtle.forward(250)
    turtle.setheading(0)
    number_of_dots = 100

    for dot_count in range(1, number_of_dots + 1):
        turtle.dot(20, random.choice(color_list))
        # turtle.write(random.choice(color_list))
        # print(random.choice(color_list))
        turtle.forward(50)

        if dot_count % 10 == 0:
            turtle.setheading(90)
            turtle.forward(50)
            turtle.setheading(180)
            turtle.forward(500)
            turtle.setheading(0)

    screen = turtle_module.Screen()
    screen.exitonclick()


# rgb_colors = color_extractor(image="image.jpg", num=60)
# hirst_drawing_creation(rgb_colors)
