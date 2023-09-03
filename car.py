from turtle import Turtle
import random

class Car(Turtle):

    def __init__(self, positions):
        super().__init__()
        self.penup()
        self.car_parts = []
        self.my_color = random.choice(["yellow", "gold", "orange", "red",
                                    "maroon", "violet", "magenta", "purple",
                                    "navy", "blue", "skyblue", "cyan", "turquoise",
                                    "lightgreen", "green"])
        self.shape("square")
        self.shapesize(1,3)
        self.setheading(180)
        self.color(self.my_color)
        self.positions = positions
        self.speed = random.randint(1,3)

        y = random.choice(self.positions)

        self.positions.remove(y)
        self.goto(440, y)


    def move(self):

        self.forward(self.speed)
