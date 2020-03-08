import turtle
from paddle_a import (paddle_a_up, paddle_a_down)
from paddle_b import (paddle_b_up, paddle_b_down)
from ball import ball

# Create a screen
wn = turtle.Screen() 
# Set window title
wn.title("Pong by Jonathan")
# Set window background color
wn.bgcolor("black")
# Set window size (window center is 0, 0)
wn.setup(width=800, height=600)
# Stops the window from updating. Speeds up game
wn.tracer(0)

# Keyboard binding for paddle_a
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Set border limit
top_border_limit = wn.canvheight - 10
right_border_limit = wn.canvwidth - 10
bottom_border_limit = -wn.canvheight + 10
left_border_limit = -wn.canvwidth + 10

# Paddle top and bottom
# Note that both paddle_a and _b are the same
paddle_top = paddle_a.ycor() + 50 # ycor() gives center coordinate
paddle_bottom = paddle_a.ycor() - 50

# Paddle surface
paddle_a_surface = -340 # paddle_a center is at 350. It's horizontal length is 20.
paddle_b_surface = 340 

# Main game loop
while True:
    # Update screen
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > top_border_limit:
        ball.sety(top_border_limit)
        ball.dy *= -1 # Reverse direction

    if ball.ycor() < bottom_border_limit:
        ball.sety(bottom_border_limit)
        ball.dy *= -1

    if ball.xcor() > right_border_limit or ball.xcor() < left_border_limit:
        ball.goto(0, 0) # Restart
        ball.dx *= -1 
    
    # Collide with paddle_a
    if ball.xcor() < paddle_a_surface and (ball.ycor() < paddle_top and ball.ycor() > paddle_bottom):
        
