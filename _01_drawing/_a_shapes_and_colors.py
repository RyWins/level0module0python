import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    my_turtle = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    turtle.shape('turtle')
    # Set your turtle's speed using .speed(2)
    turtle.speed(4)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    turtle.color('green')
    turtle.pencolor('blue')
    # Move your turtle forward using .forward(100)
    turtle.forward(100)
    # TEST    Did your turtle move forward? yes

    # Move your turtle left or right using .left(90) or .right(90)
    turtle.left(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    count = 0
while count < 4:
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    count + 2

    # TEST    Did your turtle draw a square? yes

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    turtle.goto(-100, -100)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    turtle.begin_fill()
    turtle.circle(90, steps=30)
    turtle.end_fill()
    # TEST    Did your turtle draw a circle? yes

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    turtle.goto(-300, -100)
    turtle.begin_fill()
    turtle.circle(90, steps=30)
    turtle.end_fill()

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
