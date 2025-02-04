from turtle import Turtle

FONT = ("Courier", 80, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100,200)
        self.write(self.r_score, align="center", font=FONT)

    def add_point(self,left_or_right):
        if left_or_right == "left":
            self.l_score += 1
        elif left_or_right == "right":
            self.r_score += 1





























