from turtle import Turtle
# Constants for initial setup and movement
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    """
    A Snake class that represents the snake in the Snake game.
    Handles creation, movement, growth, direction changes,
    and reset after collisions.
    """
    def __init__(self):


        self.segments = []

        self.createSnake()
        self.head = self.segments[0]
    def createSnake(self):
        """
        Creates the initial snake body using predefined starting positions.
        """

        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        """
        Adds a new segment to the snake body at the given position.
        """

        x_axis = 0
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)
        x_axis -= 20

    def extend(self):
        """
        Extends the snake by adding a new segment
        at the position of the last segment.
        """

        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Moves the snake forward by making each segment follow
        the segment in front of it. The head moves forward by a fixed distance.
        """

        # Move each segment to the position of the one in front
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Move the head forward
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Changes direction to UP if not currently moving DOWN."""

        if self.segments[0].heading() !=   DOWN:
            self.segments[0].setheading(UP)


    def down(self):
        """Changes direction to DOWN if not currently moving UP."""

        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)



    def left(self):

        """Changes direction to LEFT if not currently moving RIGHT."""

        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)



    def right(self):
        """Changes direction to RIGHT if not currently moving LEFT."""

        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def reset_snake(self):
        """
        Resets the snake after a collision.
        Moves old segments off-screen, clears the segment list,
        and creates a new snake at the starting position.
        """

        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]
