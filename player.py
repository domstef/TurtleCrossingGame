from turtle import Turtle


class Player(Turtle):

    def __init__(self, starting_pos):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(starting_pos)
        self.shape("turtle")
        self.setheading(90)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)