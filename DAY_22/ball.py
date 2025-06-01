from turtle import Turtle
BALL_MOVE_STEP = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.move_x_sign = 1
        self.move_y_sign = 1
        self.move_speed = 0.1

    def bounce_x(self):
        self.increase_speed()
        self.move_x_sign *= -1

    def bounce_y(self):
        self.move_y_sign *= -1

    def move(self):
        new_x = self.xcor() + BALL_MOVE_STEP * self.move_x_sign
        new_y = self.ycor() + BALL_MOVE_STEP * self.move_y_sign
        self.goto(x=new_x, y=new_y)
        if self.ycor() >= 281 or self.ycor() <= -281:
            self.bounce_y()

    def reset_position(self):
        self.move_speed = 0.1
        self.bounce_x()
        self.home()

    def increase_speed(self):
        self.move_speed *= 0.9
