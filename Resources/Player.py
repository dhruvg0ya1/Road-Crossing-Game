from turtle import Turtle
STARTING_POSITION = (0, -180)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('cyan')
        self.shapesize(stretch_len = 1, stretch_wid = 1)
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def up(self):
        self.forward(MOVE_DISTANCE)
        
    def finish(self):
        self.goto(STARTING_POSITION)