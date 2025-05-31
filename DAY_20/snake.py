from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTION_UP = 90
DIRECTION_DOWN = 270
DIRECTION_LEFT = 180
DIRECTION_RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]  # The head of the snake

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for si in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[si - 1].xcor()
            new_y = self.segments[si - 1].ycor()
            self.segments[si].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTION_DOWN:
            self.head.setheading(DIRECTION_UP)

    def down(self):
        if self.head.heading() != DIRECTION_UP:
            self.head.setheading(DIRECTION_DOWN)

    def left(self):
        if self.head.heading() != DIRECTION_RIGHT:
            self.head.setheading(DIRECTION_LEFT)

    def right(self):
        if self.head.heading() != DIRECTION_LEFT:
            self.head.setheading(DIRECTION_RIGHT)
