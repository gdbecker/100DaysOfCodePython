from turtle import Turtle

STARTING_POSITION = (0, -220)
STARTING_SPEED = 6
MOVE_DISTANCE = 20
UP_RIGHT = 45
UP_LEFT = 135
DOWN_LEFT = 225
DOWN_RIGHT = 315

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.rate = STARTING_SPEED
        self.speed(self.rate)
        self.refresh()

    def refresh(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    # def increase_speed(self):
    #     self.raste += 0.5
    #     self.speed(self.rate)

    def bounce_up_down(self):
        if self.heading() == UP_RIGHT:
            self.setheading(DOWN_RIGHT)
        elif self.heading() == UP_LEFT:
            self.setheading(DOWN_LEFT)
        elif self.heading() == DOWN_RIGHT:
            self.setheading(UP_RIGHT)
        elif self.heading() == DOWN_LEFT:
            self.setheading(UP_LEFT)

    def bounce_left_right(self):
        if self.heading() == UP_RIGHT:
            self.setheading(UP_LEFT)
        elif self.heading() == UP_LEFT:
            self.setheading(UP_RIGHT)
        elif self.heading() == DOWN_RIGHT:
            self.setheading(DOWN_LEFT)
        elif self.heading() == DOWN_LEFT:
            self.setheading(DOWN_RIGHT)