import turtle 

win = turtle.Screen()
win.setup(800,600)
win.bgcolor("blue")
win.title("Pong-Game")
win.tracer(0)

# left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("black")
left_paddle.shapesize(stretch_wid=5,stretch_len=1)
left_paddle.penup()
left_paddle.goto(-390,0)

# right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("black")
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.penup()
right_paddle.goto(380,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = .5
ball.dy = .5

#Logic for Left paddle
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+ 20)
def left_paddle_down():
    left_paddle.sety(left_paddle.ycor()- 20)

win.listen()
win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")

# Logic for right paddle
def right_paddle_up():
    right_paddle.sety(right_paddle.ycor()+ 20)
def right_paddle_down():
    right_paddle.sety(right_paddle.ycor()- 20)

win.listen()
# win.onkeypress(right_paddle_up, "Up")
# win.onkeypress(right_paddle_down, "Down")


while True:
    win.update()
    # ball movement 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ ball.dy)
    if ball.ycor()>=290:
        ball.dy *= -1
    elif ball.ycor()<=-290:
        ball.dy *= -1