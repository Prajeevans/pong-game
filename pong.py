import turtle 


score_a = 0
score_b = 0


win = turtle.Screen()
win.setup(800,600)
win.bgcolor("blue")
win.title("Pong-Game")
win.tracer(0)

# Score board
pen = turtle.Turtle()
pen.speed()
pen.color("green")
pen.penup()
pen.goto(0,260)
pen.write(f"Player A: {score_a} Player B: {score_b}", align="Center", font=["ariel", 24, 'bold'])
pen.hideturtle()


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
ball.dx = .4
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
win.onkeypress(right_paddle_up, "i")
win.onkeypress(right_paddle_down, "k")


while True:
    win.update()
    # ball movement 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor()+ ball.dy)
    if ball.ycor()>=290:
        ball.sety(290)
        ball.dy *= -1
        
    elif ball.ycor()<=-290:
        ball.sety(-290)
        ball.dy *= -1

    # right and left wall
    if ball.xcor()>=380:
        ball.setx(380)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="Center", font=["ariel", 24, 'bold'])

    elif ball.xcor()<=-380:
        ball.setx(-380)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="Center", font=["ariel", 24, 'bold'])

    
    # paddle hit 
    if ball.xcor()> 370 and right_paddle.ycor() - 50< ball.ycor() < right_paddle.ycor()+50 :
        ball.setx(370)
        ball.dx *= -1
    if ball.xcor()<-370 and left_paddle.ycor() - 50< ball.ycor() < left_paddle.ycor()+50 :
        ball.setx(-370)
        ball.dx *= -1