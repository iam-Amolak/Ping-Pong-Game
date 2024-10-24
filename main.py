from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("PING PONG")
screen.tracer(0)

paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_on = True
gameOver = Score()

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_bally()

    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_ballx()

    if ball.xcor() > 380 or ball.xcor() < -400:
        game_on = False
        continue
        
gameOver.game_over()
screen.exitonclick()