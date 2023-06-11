from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        # High score file
        f = open("data.txt")
        self.high_score = int(f.read())
        f.close()

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # game_over method is replaced with below
    def reset(self):
        if self.score > self.high_score:
            # High score file
            f = open("data.txt", "w")
            self.high_score = self.score
            f.write(f"{self.high_score}")
            f.close()

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()