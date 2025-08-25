from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):


        self.segments = []

        self.createSnake()
        self.head = self.segments[0]
    def createSnake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        x_axis = 0
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)
        x_axis -= 20

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() !=   DOWN:
            self.segments[0].setheading(UP)
        # if self.segments[0].heading() == 0:
        #     self.segments[0].left(90)
        # elif self.segments[0].heading() == 180:
        #     self.segments[0].right(90)


    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
        # if self.segments[0].heading() == 0:
        #     self.segments[0].right(90)
        # elif self.segments[0].heading() == 180:
        #     self.segments[0].left(90)


    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

        # if self.segments[0].heading() == 90:
        #     self.segments[0].left(90)
        # elif self.segments[0].heading() == 270:
        #     self.segments[0].right(90)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
        # if self.segments[0].heading() == 90:
        #     self.segments[0].right(90)
        # elif self.segments[0].heading() == 270:
        #     self.segments[0].left(90)
    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]
