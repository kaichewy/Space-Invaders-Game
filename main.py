from turtle import Turtle, Screen
from spaceship import Spaceship
from bullet import Bullet
from enemy import EnemyManager
from scoreboard import ScoreBoard
import random

screen = Screen()
screen.register_shape('img/ship.gif')
screen.register_shape('img/alien.gif')
spaceship = Spaceship()
enemy_manager = EnemyManager()
scoreboard = ScoreBoard()
screen.bgpic('img/STARWARS_BACKGROUND.gif')
screen.tracer(0)
enemy_manager.create_enemy()
screen.onkeypress(spaceship.move_left, "Left")
screen.onkeypress(spaceship.move_right, "Right")
screen.onkey(spaceship.shoot, "q")
screen.listen()

game_is_on = True
i = 0.1

while game_is_on:
    screen.update()
    for enemy in enemy_manager.enemy_list:
        random_number = random.randint(1, 10000)
        enemy.goto(enemy.xcor() + i, enemy.ycor())
        if enemy.xcor() > 300 or enemy.xcor() < -300:
            i = -1 * i
        if random_number == 1:
            enemy_manager.enemy_shoot(enemy)

    for enemy_bullet in enemy_manager.enemy_bullet_list:
        enemy_bullet.goto(enemy_bullet.xcor(), enemy_bullet.ycor() - 0.4)
        for bullet in spaceship.bullet_list:
            if enemy_bullet.distance(bullet) < 5:
                spaceship.bullet_list.remove(bullet)
                bullet.ht()
                bullet.goto(1000, 1000)
                enemy_manager.enemy_bullet_list.remove(enemy_bullet)
                enemy_bullet.ht()
                enemy_bullet.goto(1000, 1000)
        if enemy_bullet.distance(spaceship) < 10:
            scoreboard.game_over()
            game_is_on = False

    for bullet in spaceship.bullet_list:
        bullet.travel_up()
        if bullet.ycor() > 350:
            spaceship.bullet_list.remove(bullet)
            bullet.ht()

        for enemy in enemy_manager.enemy_list:
            if bullet.distance(enemy) <= 16:
                enemy.ht()
                bullet.ht()
                enemy.goto(500, 500)
                enemy_manager.enemy_list.remove(enemy)

    if not enemy_manager.enemy_list:
        scoreboard.level_up()
        enemy_manager.y_number += 1
        enemy_manager.x_number += 1
        enemy_manager.create_enemy()


screen.exitonclick()
