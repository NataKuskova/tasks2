# env/bin/python
import turtle

a = turtle.Turtle()


def draw_turtle(x, y):

    a.penup()
    a.goto(x,y)
    a.pendown()
    a.forward(100)
    a.right(145)
    a.forward(60)
    a.right(70)
    a.forward(60)
    a.right(180)
    a.forward(60)
    a.left(35)
    a.forward(50)
    a.right(90)
    a.forward(200)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(200)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(200)
    a.right(90)
    a.forward(50)
    a.left(35)
    a.forward(60)
    a.left(145)
    a.forward(100)
    a.left(145)
    a.forward(60)
    a.right(145)


if __name__ == "__main__":
    #draw_turtle(-200,200)
    #draw_turtle(100, 100)
    x = -200
    y = -100
    while x < 200:
        draw_turtle(x, y)
        x += 150
        y += 150
    turtle.done()
