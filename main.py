from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

LEFT_PADDLE_POS = (-350,0)
RIGHT_PADDLE_POS = (350,0)

#setup screen for game
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle(LEFT_PADDLE_POS)
right_paddle = Paddle(RIGHT_PADDLE_POS)
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(fun= left_paddle.move_up, key="w")
screen.onkey(fun= left_paddle.move_down, key="s")
screen.onkey(fun= right_paddle.move_up, key= "Up")
screen.onkey(fun= right_paddle.move_down, key= "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #if ball hits floor or ceiling
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect left paddle scoring
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.add_point("left")
        scoreboard.update_scoreboard()

    #detect right paddle scoring
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.add_point("right")
        scoreboard.update_scoreboard()


screen.exitonclick()



























