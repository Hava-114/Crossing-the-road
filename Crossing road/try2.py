from turtle import Screen
from turtle import Turtle
from playerr import Player
from Car import Car_creater
from Score import Scoreboard
from turtle import time
#from winning import points


screen=Screen()

screen.setup(600,600)

screen.tracer(0)


player=Player((-100,-250),"blue")
player1=Player((100,-250),"red")
scoreboard=Scoreboard()

Cars=Car_creater()
scoreboard.recreate()
screen.update()


class points(Turtle):
    def __init__(self,user1,user2):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.userone=user1
        self.usertwo=user2
    def increase1(self):
        self.clear()
        self.goto(0,0)
        self.write(f"{self.userone} wins", align="center", font=("calibral",20,"bold"))
    def increase2(self):
        self.clear()
        self.goto(0,0)
        self.write(f"{self.usertwo} wins", align="center", font=("calibral",20,"bold"))

poi=points("Player 1","Player 2")

screen.listen()

screen.onkey(player1.move_up,"Up")
screen.onkey(player1.move_down,"Down")
screen.onkey(player1.move_left,"Left")
screen.onkey(player1.move_right,"Right")
screen.onkey(player.move_up,"w")
screen.onkey(player.move_down,"s")
screen.onkey(player.move_left,"a")
screen.onkey(player.move_right,"d")

var=True
while var:
    time.sleep(0.1)
    Cars.Creater()
    Cars.move()
    for car in Cars.all_cars:
        if player.distance(car)<20:
           
            player.restart()
            screen.update()
        if player1.distance(car)<20:
            player1.restart()
   
    screen.update()

    if player.ycor()>240:
        
        screen.clear()
        poi.increase1()
        time.sleep(5)
    

    if player1.ycor()>240:
        screen.clear()
        poi.increase2()
        time.sleep(5)
