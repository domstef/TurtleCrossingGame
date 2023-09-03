from turtle import Turtle


class Endscreen(Turtle):

    def __init__(self):
        super().__init__()

        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0,30)



    def game_over_lose(self):
        self.write("GAME OVER! \n \n YOU LOST!", align="center", font=("Arial", 24, "normal"))


    def game_over_won(self):
        self.write("GAME OVER \n \n YOU WON!", align="center", font=("Arial", 24, "normal"))

    def level(self, level):
        self.goto(250, 250)
        self.clear()
        self.write("Level {}".format(level), align="center", font=("Arial", 16, "normal"))

