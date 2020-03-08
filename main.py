import turtle
from paddle_a import (paddle_a, paddle_a_up, paddle_a_down)
from paddle_b import (paddle_b, paddle_b_up, paddle_b_down)
from ball import ball
from pen import pen

# Create a screen
wn = turtle.Screen() 
# Set window title
wn.title("Pong by Jonathan")
# Set window background color
wn.bgcolor("black")
# Set window size (window center is 0, 0)
wn.setup(width = 800, height = 600)
# Stops the window from updating. Speeds up game
wn.tracer(0)
# Starting score
scoreA = 0
scoreB = 0

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

# Paddle surface
paddle_a_surface = -340 # paddle_a center is at 350. It's horizontal length is 20.
paddle_a_middle = -350
paddle_b_surface = 340 
paddle_b_middle = 350

# Show score
pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier, 24"))

# Main game loop
while True:
    # Update screen
    wn.update()

    # Paddle a current y position
    paddle_a_top = paddle_a.ycor() + 60 # ycor() gives center coordinate of the paddle
    paddle_a_bottom = paddle_a.ycor() - 60

    # Paddle b current y position
    paddle_b_top = paddle_b.ycor() + 60
    paddle_b_bottom = paddle_b.ycor() - 60

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

    # Player A wins
    if ball.xcor() > right_border_limit:
        ball.goto(0, 0) # Restart
        ball.dx *= -1
        scoreA += 1
        pen.clear() # Clear screen first before writing again
        pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier, 24"))
    
    # Player B wins
    if ball.xcor() < left_border_limit:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier, 24"))

    # Collide with paddle_a
    if (ball.xcor() < paddle_a_surface and ball.xcor() > paddle_a_middle) and (ball.ycor() < paddle_a_top and ball.ycor() > paddle_a_bottom):
        ball.setx(paddle_a_surface)
        ball.dx *= -1
    
    # Collide with paddle_b
    if (ball.xcor() > paddle_b_surface and ball.xcor() < paddle_b_middle) and (ball.ycor() < paddle_b_top and ball.ycor() > paddle_b_bottom):
        ball.setx(paddle_b_surface)
        ball.dx *= -1
