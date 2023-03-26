from turtle import Turtle


class ScoreCard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.hideturtle()
        self.speed("fastest")
        self.goto(0, 280)
        self.current_score = 0
        self.write(f"Score:{self.current_score}", True, align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.pencolor("red")
        self.write("Game Over!", True, align="center", font=("Arial", 24, "bold"))

    def score_count(self):
        self.current_score += 1
        self.speed("fastest")
        self.clear()
        self.write(f"Score:{self.current_score}", False, align="center", font=("Arial", 12, "normal"))
