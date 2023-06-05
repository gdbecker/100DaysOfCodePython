from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.lives = 2
        self.color("white")
        self.penup()
        self.goto(position)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.lives} lives left", align=ALIGNMENT, font=FONT)

    def decrease_lives(self):
        self.lives -= 1

    def game_won(self):
        self.clear()
        self.write("YOU WON!", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)