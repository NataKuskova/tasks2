# env/bin/python
# Kuskova Natalia
import turtle
import re


my_turtle = turtle.Turtle()
my_win = turtle.Screen()


def get_color(i):
    colors = ['Light Slate Blue', 'Sky Blue', 'Lime Green',
              'Blue', 'Peru', 'Firebrick', 'Pink']
    if i > len(colors) - 1:
        return get_color(i - len(colors))
    else:
        return colors[i]


def repetition_frequency(text):
    string = text.split()
    string_qty = {}
    for i in string:
        string_qty[i] = len(re.findall(i, text))
    return string_qty


def create_diagram_sectors(frequency):
    radius = 120
    total = sum(frequency.values())
    i = 0
    for key, value in iter(frequency.items()):
        percent = value * 100.0 / total
        angle = percent * 360.0 / 100.0
        my_turtle.fillcolor(get_color(i))
        my_turtle.pencolor(get_color(i))
        my_turtle.begin_fill()
        my_turtle.forward(radius)
        my_turtle.left(90)
        my_turtle.circle(radius, angle)
        my_turtle.left(90)
        my_turtle.forward(radius)
        my_turtle.left(180)
        my_turtle.end_fill()
        i += 1


def create_legend(frequency):
    i = 0
    distance_y = 100
    for key, value in iter(frequency.items()):
        my_turtle.hideturtle()
        my_turtle.penup()
        my_turtle.goto(160, distance_y)
        my_turtle.pendown()
        my_turtle.dot(20, get_color(i))
        my_turtle.color(get_color(i))
        my_turtle.penup()
        my_turtle.goto(175, distance_y - 8)
        my_turtle.pendown()
        my_turtle.write(repr(key) + " - " + repr(value) + " time(-s)", False,
                        align="left", font=("Arial", 12, "normal"))
        distance_y -= 30
        i += 1


def draw_diagram_sectors(text):
    my_turtle.speed('normal')

    frequency = repetition_frequency(text)
    create_diagram_sectors(frequency)
    create_legend(frequency)

    my_win.exitonclick()


def draw_diagram_rays(text):
    my_turtle.speed('normal')
    radius = 120
    frequency = repetition_frequency(text)
    angle = 360.0 / len(frequency)
    i = 0
    for key, value in iter(frequency.items()):
        my_turtle.pencolor(get_color(i))
        my_turtle.color(get_color(i))
        my_turtle.forward(radius)
        my_turtle.circle(4)
        if value > 1:
            j = 1
            while j < value:
                my_turtle.pencolor(get_color(j+2))
                my_turtle.color(get_color(j+2))
                my_turtle.forward(radius)
                my_turtle.circle(4)
                j += 1
            my_turtle.write(repr(key), False, align="right",
                            font=("Arial", 12, "normal"))
            my_turtle.left(180)
            my_turtle.penup()
            my_turtle.forward(radius * (j-1))
            my_turtle.pendown()
            my_turtle.right(90)
        else:
            my_turtle.write(repr(key), False, align="right",
                            font=("Arial", 12, "normal"))
            my_turtle.left(90)
        my_turtle.penup()
        my_turtle.circle(radius, angle)
        my_turtle.pendown()
        my_turtle.left(90)
        my_turtle.penup()
        my_turtle.forward(radius)
        my_turtle.pendown()
        my_turtle.left(180)
        i += 1
    my_turtle.hideturtle()
    my_win.exitonclick()


def draw_diagram(text, type_):
    if type_ == 'sectors':
        draw_diagram_sectors(text)
    elif type_ == 'rays':
        draw_diagram_rays(text)


if __name__ == "__main__":
    draw_diagram("hello world hello world hello hello world nice to meet you to nice", "sectors")
    # draw_diagram("hello to world hello world world nice to meet you real", "rays")
    turtle.done()