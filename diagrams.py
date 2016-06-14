# env/bin/python
import turtle
import re


my_turtle = turtle.Turtle()
my_win = turtle.Screen()


def repetition_frequency(text):
    string = text.split()
    string_qty = {}
    for i in string:
        string_qty[i] = len(re.findall(i, text))
    return string_qty


def draw_diagram_sectors(text, type_):
    my_turtle.speed('normal')
    colors = ['Light Slate Blue', 'Sky Blue', 'Lime Green',
              'Blue', 'Peru', 'Firebrick', 'Pink']
    radius = 120
    frequency = repetition_frequency(text)
    total = sum(frequency.values())
    i = 0
    for key, value in iter(frequency.items()):
        percent = value * 100.0 / total
        angle = percent * 360.0 / 100.0
        if i <= len(colors):
            my_turtle.fillcolor(colors[i])
            my_turtle.pencolor(colors[i])
        else:
            my_turtle.fillcolor(colors[0])
            my_turtle.pencolor(colors[0])
        my_turtle.begin_fill()
        my_turtle.forward(radius)
        my_turtle.left(90)
        my_turtle.circle(radius, angle)
        my_turtle.left(90)
        my_turtle.forward(radius)
        my_turtle.left(180)
        my_turtle.end_fill()
        i += 1
    j = 0
    d = 100
    for key, value in iter(frequency.items()):
        my_turtle.hideturtle()
        my_turtle.penup()
        my_turtle.goto(160, d)
        my_turtle.pendown()
        if j <= len(colors):
            my_turtle.dot(20, colors[j])
            my_turtle.color(colors[j])
        else:
            my_turtle.dot(20, colors[0])
            my_turtle.color(colors[0])
        my_turtle.penup()
        my_turtle.goto(175, d-8)
        my_turtle.pendown()
        my_turtle.write(repr(key) + " - " + repr(value) + " time(-s)", False, align="left",
                        font=("Arial", 12, "normal"))
        d -= 30
        j += 1
    my_win.exitonclick()


def draw_diagram_rays(text, type_):
    my_turtle.speed('normal')
    colors = ['Light Slate Blue', 'Sky Blue', 'Lime Green',
              'Blue', 'Peru', 'Firebrick', 'Pink']
    colors2 = ['Peach Puff 3', 'Dark Slate Gray',
               'Light Slate Gray', 'Cornflower Blue',
               'Dark Khaki', 'Rosy Brown', 'Tomato']
    radius = 120
    frequency = repetition_frequency(text)
    angle = 360.0 / len(frequency)
    i = 0
    for key, value in iter(frequency.items()):
        if i <= len(colors):
            my_turtle.pencolor(colors[i])
            my_turtle.color(colors[i])
        else:
            my_turtle.pencolor(colors[0])
            my_turtle.color(colors[0])
        my_turtle.forward(radius)
        my_turtle.circle(4)
        if value > 1:
            j = 1
            while j < value:
                if j <= len(colors):
                    my_turtle.pencolor(colors2[j])
                    my_turtle.color(colors2[j])
                else:
                    my_turtle.pencolor(colors2[0])
                    my_turtle.color(colors2[0])
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
        draw_diagram_sectors(text, type_)
    elif type_ == 'rays':
        draw_diagram_rays(text, type_)


if __name__ == "__main__":
    draw_diagram("hello world hello world hello hello world nice to meet you to nice", "sectors")
    # draw_diagram("hello to world hello world world nice to meet you real", "rays")
    turtle.done()