import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape ("turtle")
    brad.color ("blue")
    brad.speed(2)

    n = 0
    while (n < 4):
        brad.forward(100)
        brad.right (90)
        n = n + 1
draw_square()

def draw_circle():
    angie = turtle.Turtle ()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
draw_circle()

def draw_triangle():
    jane = turtle.Turtle ()
    jane.shape ("turtle")
    jane.color ("black")
    jane.speed (2)

    x = 0
    while (x < 3):
        jane.forward(100)
        jane.right(45)
        x = x +1
draw_triangle()

window.exitonclick()


