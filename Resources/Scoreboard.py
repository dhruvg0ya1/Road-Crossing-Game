from turtle import Turtle
FONT = ("Comic Sans MS", 10, "normal")
GAME_OVER_FONT = ('Elephant', 30, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-370, 180)
        self.score = 0
        self.color('white')
        self.write(f'Score: {self.score}', False, 'center', FONT)
        
    def inc(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', False, 'center', FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', False, 'center', GAME_OVER_FONT)