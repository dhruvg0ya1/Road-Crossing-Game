import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]

class Car():
    def __init__(self):
        self.cars = []
        self.move_dist = 5
        
    def create(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle('square')
            new_car.shape('square')
            new_car.shapesize(stretch_len = 2, stretch_wid = 1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(400, random.randint(-180, 180))
            self.cars.append(new_car)
        
    def move(self):
        for i in self.cars:
            i.backward(self.move_dist)
    
    def inc_speed(self):
        self.move_dist += self.move_dist
        