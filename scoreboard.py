from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score_write()

    def score_write(self):
        self.write(f"Score: {self.score}", align="center", font=("arial", 24, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GameOver", align="center", font=("arial", 24, "bold"))


    def update_score(self):
        self.score += 1
        self.clear()
        self.score_write()