import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's speed to slow
t.speed(1)

# Draw the face
t.penup()
t.goto(-100, 100)
t.pendown()
t.circle(100)

# Draw the nose
t.penup()
t.goto(0, 50)
t.pendown()
t.left(60)
t.forward(50)
t.right(120)
t.forward(50)

# Draw the mouth
t.penup()
t.goto(-50, 0)
t.pendown()
t.circle(25)

# Draw the eyes
t.penup()
t.goto(-60, 130)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(60, 130)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
