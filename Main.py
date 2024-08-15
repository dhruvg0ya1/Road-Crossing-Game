import time
from turtle import Screen
from Resources.Player import Player
from Resources.Car import Car
from Resources.Scoreboard import Scoreboard


s = Screen()
s.bgcolor('black')
s.setup(width=800, height=400)
s.title('Road Crossing')
s.tracer(0)

t = Player()
c = Car()
score = Scoreboard()

s.listen()
s.onkeypress(t.up, 'Up')


game_on = True
while game_on:
    time.sleep(0.1)
    s.update()
    c.create()
    c.move()


    if t.ycor() > 179:
        t.finish()
        c.inc_speed()
        score.inc()
    
    for i in c.cars:
        if i.distance(t) < 30:
            game_on = False
            score.game_over()
        




















s.exitonclick()