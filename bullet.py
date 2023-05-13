from turtle import Turtle
import time


class Bullet(Turtle):
    def __init__(self, spaceship_xcor, spaceship_ycor):
        super().__init__()
        self.penup()
        self.ht()
        self.shape("square")
        self.shapesize(0.75, 0.25)
        self.color("red")
        self.goto(spaceship_xcor, spaceship_ycor)
        self.showturtle()

    def travel_up(self):
        self.goto(self.xcor(), self.ycor() + 0.4)

    def travel_down(self):
        self.goto(self.xcor(), self.ycor() - 0.4)


