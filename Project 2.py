# Project 2. Part 2.
import turtle as t

t.speed(0)
t.bgcolor("white")

def draw_pizza():
    # Pizza crust
    t.begin_fill()
    t.color('dark orange')
    t.penup()
    t.goto(10, -70)
    t.pendown()
    t.circle(120)
    t.end_fill()

    # Pizza crust
    t.color('brown')
    t.penup()
    t.goto(10, -50)
    t.pendown()
    t.pensize(5)
    t.circle(100)

    # Pizza base
    t.color("orange")
    t.penup()
    t.goto(10, -50)
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # Pepperoni
    t.penup()
    t.color("red")
    pepperoni_positions = [(30, 40), (-20, 60), (60, 60), (-40, 0), (0, 0), (40, 0)]
    for x, y in pepperoni_positions:
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.penup()

    # Olives
    t.color("green")
    olive_positions = [(0, 100), (40, 75), (-20, 20), (30, 0), (-30, 35), (30, -20), (-20, 20)]
    t.width(2)
    for x, y in olive_positions:
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.left(90)
        for _ in range(2):
            t.circle(10, 90)
            t.circle(10, 90)
        t.end_fill()
        t.penup()

    # SLICES!
    t.color('white')
    t.pensize(3)
    t.penup()
    t.goto(10, 50)
    t.pendown()
    for _ in range(10):
        t.forward(120)
        t.right(360/10)
        t.penup()
        t.goto(10, 50)
        t.pendown()

# Coke
def draw_coke():
    t.speed(0)  
    t.pensize(1)  

    # Bottom of the can
    t.penup()
    t.goto(199, -40)
    t.pendown()
    t.pensize(5)
    t.pencolor('black')
    t.circle(26)
    t.pensize(1)
    t.color("red")
    t.begin_fill()
    t.circle(26)
    t.end_fill()

    # Can body
    t.penup()
    t.goto(200, 50)
    t.pendown()
    t.pensize(5)
    t.pencolor('black')
    for _ in range(4):
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.pensize(1)
    t.color("red")
    t.penup()
    t.goto(200, 50)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()

    # Top of the can
    t.penup()
    t.goto(199, 50)
    t.pendown()
    t.pensize(5)
    t.pencolor('black')
    t.circle(26)
    t.pensize(1)
    t.pencolor('red')
    t.begin_fill()
    t.circle(26) 
    t.end_fill()

    # Logo
    t.penup()
    t.goto(225, -10)
    t.pendown()
    t.color("black")
    t.write("Coke", align="center", font=("Arial", 12, "bold"))

    t.penup()
    t.goto(0, 0)
    t.pendown()

    t.done()

draw_pizza()
draw_coke()

t.exitonclick()