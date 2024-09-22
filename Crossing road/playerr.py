from turtle import Turtle
class Player(Turtle):
    def __init__(self, pos,col):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.posi=pos
        self.goto(self.posi)
        self.color(col)
        

    def move_up(self):
        self.setheading(90)
        self.forward(10)

    def move_down(self):
        self.setheading(270)
        self.forward(10)

    def move_right(self):
        self.setheading(0)
        self.forward(10)
        
    def move_left(self):
        self.setheading(180)
        self.forward(10)

    def restart(self):
        self.goto(self.posi)
        
        
       
