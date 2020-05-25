import turtle

window = turtle.Screen()
window.title("Pong game By Efe")
window.bgcolor("Black")
window.setup(width=800, height=600)

# Score
score1 = 0
score2 = 0

stick1 = turtle.Turtle()
stick1.speed(0)
stick1.shape("square")
stick1.color("white")
stick1.shapesize(stretch_wid=5, stretch_len=1)
stick1.penup()
stick1.goto(-350, 0)

stick2 = turtle.Turtle()
stick2.speed(0)
stick2.shape("square")
stick2.color("white")
stick2.shapesize(stretch_wid=5, stretch_len=1)
stick2.penup()
stick2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(10)

ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1 vs Player 2 ", align="center", font=("Courier", 24, "normal"))

# Scoreboard
penscore = turtle.Turtle()
penscore.speed(0)
penscore.color("white")
penscore.penup()
penscore.hideturtle()
penscore.goto(-20, 230)
penscore.write("0        0", align="center", font=("Courier", 24, "normal"))


def moveStick1up():
    y = stick1.ycor()
    y += 20
    stick1.sety(y)


def moveStick1down():
    y = stick1.ycor()
    y -= 20
    stick1.sety(y)


def moveStick2up():
    y = stick2.ycor()
    y += 20
    stick2.sety(y)


def moveStick2down():
    y = stick2.ycor()
    y -= 20
    stick2.sety(y)


window.listen()  # Listen keyboard input
window.onkeypress(moveStick1up, "w")  # Move stick1 with keyboard
window.onkeypress(moveStick1down, "s")

window.onkeypress(moveStick2up, "Up")  # Move stick2 with keyboard
window.onkeypress(moveStick2down, "Down")

while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check for ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        penscore.clear()
        penscore.write("{}        {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        penscore.clear()
        penscore.write("{}        {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # Border check for stick1
    if stick1.ycor() > 260:
        stick1.sety(260)

    if stick1.ycor() < -240:
        stick1.sety(-240)

    # Border check for stick2
    if stick2.ycor() > 260:
        stick2.sety(260)

    if stick2.ycor() < -240:
        stick2.sety(-240)

    # Stick and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < stick2.ycor() + 40 and ball.ycor() > stick2.ycor() - 40):

        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < stick1.ycor() + 40 and ball.ycor() > stick1.ycor() - 40):

        ball.setx(-340)
        ball.dx *= -1
