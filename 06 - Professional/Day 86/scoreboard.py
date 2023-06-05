from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self, position, num_walls_left):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.update_scoreboard(num_walls_left)
        self.hideturtle()

    def update_scoreboard(self, num_walls_left):
        self.clear()
        self.write(f"{self.score} walls down | {num_walls_left} walls left", align=ALIGNMENT, font=FONT)

    def increase_score(self, num_walls_left):
        self.score += 1
        self.update_scoreboard(num_walls_left)

    def game_over(self):
        self.clear()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def game_won(self):
        self.clear()
        self.write("YOU WON!", align=ALIGNMENT, font=FONT)