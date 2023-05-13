import random
from turtle import Turtle
from bullet import Bullet


class EnemyManager:
    def __init__(self):
        self.positions = []
        self.enemy_list = []
        self.x_number = 5
        self.y_number = 1

    def create_enemy(self):
        x = -200
        for i in range(self.x_number):
            x += 60
            y = 300
            for e in range(self.y_number):
                y -= 30
                self.positions.append((x, y))

        for position in self.positions:
            enemy = Turtle()
            enemy.color("white")
            enemy.shape('img/alien.gif')
            enemy.shapesize(1, 1)
            enemy.penup()
            enemy.ht()
            enemy.goto(position)
            enemy.showturtle()
            self.enemy_list.append(enemy)
            self.enemy_bullet_list = []

    def enemy_shoot(self, random_enemy):
        bullet = Bullet(random_enemy.xcor(), random_enemy.ycor())
        bullet.setheading(180)
        self.enemy_bullet_list.append(bullet)


