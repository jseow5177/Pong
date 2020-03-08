import turtle

# Paddle B
paddle_b = turtle.Turtle() 
paddle_b.speed(0) 
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup() 
paddle_b.goto(350, 0)

def paddle_b_up():
    y = paddle_b.ycor() # return the current y coordinate
    y += 20 # add 20 pixels
    paddle_b.sety(y) # set new coordinate

def paddle_b_down():
    y = paddle_b.ycor() # return the current y coordinate
    y -= 20 # add 20 pixels
    paddle_b.sety(y) # set new coordinate