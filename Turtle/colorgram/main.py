import random
import colorgram as c
import turtle as t

def generate_color_list(image_extract):
    number_extract = int(input("How many colors to extract?: "))
    colors = c.extract(image_extract, number_extract)
    rgb_colors = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g ,b)
        if r >= 240 and g >= 240 and b >= 240:
            continue
        rgb_colors.append(new_color)

    return rgb_colors

def painting(rows, columns, space, colors, size, x, y):
    for row in range(rows):
        for column in range(columns):
            dot_painter.dot(size, random.choice(colors))
            dot_painter.forward(space)
        y += space
        dot_painter.setposition(x, y)

dot_painter = t.Turtle()
t.colormode(255)
dot_painter.hideturtle()
dot_painter.penup()
dot_painter.speed("fastest")

image = input("Extract from which image?: ")
color_list = generate_color_list(image)

dot_size = int(input("Select a dot size (5-20): "))
n_rows = int(input("How many rows would you like?: "))
n_columns = int(input("How many columns would you like?: "))
spacing = int(input("How much spacing do you want?: "))

x_position = -(((dot_size * n_columns)+(spacing*(n_columns-1)))/2)
y_position = -(((dot_size * n_rows)+(spacing*(n_rows-1)))/2)
dot_painter.setposition(x_position, y_position)

painting(n_rows, n_columns, spacing, color_list, dot_size, x_position, y_position)

screen = t.Screen()
screen.exitonclick()