from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

XPOS = 300
XNEG = -300
YPOS = 300
YNEG = -300


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segment = []
        self.segment2 = []
        self.segment_len = len(self.segment)
        self.snake_len = 3
        self.segment_position = 0
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for snakes in range(self.snake_len):
            new_segment = Turtle(shape="square")
            self.styling_snake(new_segment)
            new_segment.goto(x=self.segment_position, y=0)

    def styling_snake(self, new_segment):
        new_segment.color("white")
        new_segment.penup()
        self.segment_position -= 20
        self.segment.append(new_segment)

    def increase_snake(self):
        new_segment = Turtle(shape="square")
        self.styling_snake(new_segment)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def reset(self):
        for hiding in self.segment:
            hiding.hideturtle()
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        
    def passage(self):
        if self.head.xcor() > XPOS:
            for switch in self.segment:
                num_track = 0
                self.segment2.append(switch)
                self.segment2[num_track].goto(-300, self.head.ycor())
                num_track += 1

        elif self.head.xcor() < XNEG:
            for switch in self.segment:
                num_track = 0
                self.segment2.append(switch)
                self.segment2[num_track].goto(300, self.head.ycor())
                num_track += 1

        elif self.head.ycor() > YPOS:
            for switch in self.segment:
                num_track = 0
                self.segment2.append(switch)
                self.segment2[num_track].goto(self.head.xcor(), -300)
                num_track += 1

        elif self.head.ycor() < YNEG:
            for switch in self.segment:
                num_track = 0
                self.segment2.append(switch)
                self.segment2[num_track].goto(self.head.xcor(), 300)
                num_track += 1

        self.segment2 = []

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)
