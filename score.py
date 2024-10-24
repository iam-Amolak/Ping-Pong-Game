from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,0)

    def game_over(self):
        self.write("! ! GAME OVER ! !", False, "center", ("Comic Sans MS", 30, "bold"))
