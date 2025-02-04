from turtle import Turtle

#create a paddle
class Paddle(Turtle):
    def __init__(self, pos_tuple):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(pos_tuple)
        self.setheading(270)
        self.shapesize(stretch_wid=1, stretch_len= 5)
        self.color("white")

    def move_up(self):
        self.backward(20)

    def move_down(self):
        self.forward(20)














