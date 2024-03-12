from turtle import Turtle

FONT = ("Courier", 24, "normal")
START_POSITION = (-280, 265)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(START_POSITION)
        self.level = 1
        self.update_scoreboard()

    def add_point(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=FONT)
