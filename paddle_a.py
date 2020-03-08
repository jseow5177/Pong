import turtle

# Paddle A
paddle_a = turtle.Turtle() # Turtle object
paddle_a.speed(0) # Turns off turtle animation  
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Stretch into rectangle
paddle_a.color("white")
paddle_a.penup() # No drawing when moving
paddle_a.goto(-350, 0) # Starting position

def paddle_a_up():
    y = paddle_a.ycor() # return the current y coordinate
    y += 20 # add 20 pixels
    paddle_a.sety(y) # set new coordinate

def paddle_a_down():
    y = paddle_a.ycor() # return the current y coordinate
    y -= 20 # add 20 pixels
    paddle_a.sety(y) # set new coordinate