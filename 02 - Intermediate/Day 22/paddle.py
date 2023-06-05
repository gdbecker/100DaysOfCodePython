from turtle import Turtle

STARTING_POSITIONS = [(350, 40), (350, 20), (350, 0), (350, -20), (350, -40)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

# Commented out my first attempt (based on Snake game with multiple turtles)
# Angela's was simplier haha

class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_position)
        # self.segments = []
        # self.create_paddle()
        # self.head = self.segments[0]
        # self.end = self.segments[-1]

    '''
    def create_paddle(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    '''

    '''
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    '''

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        '''
        self.head.setheading(UP)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        '''

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        '''
        self.end.setheading(DOWN)
        for seg_num in range(0, len(self.segments) - 1, 1):
            new_x = self.segments[seg_num + 1].xcor()
            new_y = self.segments[seg_num + 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.end.forward(MOVE_DISTANCE)
        '''