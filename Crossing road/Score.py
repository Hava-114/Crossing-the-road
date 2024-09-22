from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.player=0
        self.player1=0

    def recreate(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"Player 1: {self.player}",align="center",font=("Courier", 18,"bold"))
        self.goto(200,250)
        self.write(f"Player 2: {self.player1}",align="center",font=("Courier", 18,"bold"))

    def increase(self):
        self.player +=1
        self.recreate()

    def increase2(self):
        self.player1 +=1
        self.recreate()

