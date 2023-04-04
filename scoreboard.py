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
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
            self.write(f"Score:{self.current_score}  High_Score: {self.high_score}",
                       align="center", font=("Arial", 14, "normal"))

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.clear()
        self.current_score = 0
        self.write(f"Score:{self.current_score}  High_Score: {self.high_score}",
                   align="center", font=("Arial", 14, "normal"))

    def score_count(self):
        self.current_score += 1
        self.speed("fastest")
        self.clear()
        self.write(f"Score:{self.current_score}  High_Score: {self.high_score}",
                   align="center", font=("Arial", 14, "normal"))
