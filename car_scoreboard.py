from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 270)
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("game over!", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=("Arial", 15, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
