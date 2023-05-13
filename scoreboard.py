from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(-350, -260)
        self.level = 1
        self.pencolor("white")
        self.write(f"LEVEL {self.level}", font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(-165, 0)
        self.write("GAME OVER", font=('Arial', 40, 'normal'))

    def level_up(self):
        self.level = self.level + 1
        self.clear()
        self.write(f"LEVEL {self.level}", font=('Arial', 20, 'normal'))
