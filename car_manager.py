import random
from turtle import Turtle
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.x_move = 0
        self.move_speed = STARTING_MOVE_DISTANCE
        self.generate_car()

    def generate_car(self):
        new_x = 350 + STARTING_MOVE_DISTANCE + self.x_move
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(COLORS))
        car.setheading(180)
        car.goto(new_x, random.randint(-250, 250))
        self.cars.append(car)

    def move_cars(self):
        self.x_move += 30
        for i in self.cars:
            i.forward(self.move_speed)
        self.generate_car()

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
