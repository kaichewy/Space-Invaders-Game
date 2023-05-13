import time
from turtle import Turtle, Screen
from bullet import Bullet


class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("img/ship.gif")
        self.penup()
        self.ht()
        self.goto(0, -200)
        self.showturtle()
        self.bullet_list = []

    def move_left(self):
        self.goto(self.xcor() - 5, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + 5, self.ycor())

    def shoot(self):
        bullet = Bullet(self.xcor(), self.ycor())
        bullet.color("blue")
        self.bullet_list.append(bullet)


