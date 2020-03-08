import turtle

# Ball
ball = turtle.Turtle() 
ball.speed(0) 
ball.shape("circle")
ball.color("white")
ball.penup() 
ball.goto(0, 0)
ball.dx = 0.15 # Change in x coordinate = 0.2 pixels
ball.dy = 0.15