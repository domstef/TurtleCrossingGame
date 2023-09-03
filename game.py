from turtle import Screen
from player import Player
from car import Car
from endscreen import Endscreen
import time


def quit_game():
    global running
    running = False

POSITIONS = list(range(-200, 200, 66))

SCREEN = Screen()
SCREEN.title("Turtle Crossing Game")

SCREEN.bgpic("road.png")
SCREEN.setup(800, 600)
SCREEN.tracer(0)
SCREEN.listen()
SCREEN.onkeypress(quit_game, "q")





class Game:

    def __init__(self):
        self.start = time.time()
        self.level = 1
        self.car_positions_choice = list(range(-200, 200, 66))
        self.game_on = True
        self.starting_pos = (0, -250)
        self.player = Player(self.starting_pos)
        self.traffic = []
        self.prompt = Endscreen()

        self.generate_street()
        SCREEN.onkeypress(key="Up", fun=self.player.move_up)
        SCREEN.onkeypress(key="Down", fun=self.player.move_down)
        SCREEN.update()

    def generate_street(self):
        for _ in range(7):

            car = Car(self.car_positions_choice)
            self.traffic.append(car)

    def add_car_on_street(self):
        for _ in range(6):
            car = Car(self.car_positions_choice)
            self.traffic.append(car)

    def generate_pos(self):
        self.car_positions_choice = list(range(-200, 200, 66))


    def detect_collision(self):
        for car in self.traffic:
            if self.player.distance(car) < 21:
                self.game_over_prompt = Endscreen().game_over_lose()
                self.game_on = False

    def game(self):

        while self.game_on:
            self.prompt.level(self.level)
            time.sleep(0.001)
            for car in self.traffic:
                car.move()
            self.stop = time.time()
            self.detect_collision()
            if self.stop-self.start > 5-self.level:
                self.generate_pos()
                self.add_car_on_street()
                self.stop = 0
                self.start = time.time()
            self.is_street_crossed()


            SCREEN.update()


    def is_street_crossed(self):
        if self.player.ycor() > 250:
            self.level +=1
            self.go_to_beginning()
            print("Level {}".format(self.level))

    def go_to_beginning(self):
        self.player.goto(0, -250)

    def exit_player(self):


        SCREEN.exitonclick()
        self.game_on = False


running = True

game = Game()

game.game()
    


SCREEN.exitonclick()

