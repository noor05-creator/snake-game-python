from turtle import Turtle
import random
class Food(Turtle):
    """
      A class to represent the food object in the game.

      Inherits from the Turtle class and creates a small circular
      blue food item that randomly appears at different positions
      on the screen.
      """

    def __init__(self):
        super() .__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        """
        Move the food to a new random location on the screen.

        The new position is chosen within the screen boundaries
        (-280 to 280 in both X and Y directions).
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
