
from turtle import Turtle

# Constants for text alignment and font style
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")

class Scoreboard(Turtle):
    """
    A Scoreboard class that manages and displays the score
    and high score for a Turtle graphics-based game.
    """

    def __init__(self):
        super().__init__()
        self.score = 0

        #reading high score from file
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.penup()

        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        """
        Clears and updates the scoreboard display with the
        current score and high score.
        """
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        """
                Increases the current score by 1 and updates the display.
                """
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def reset(self):
        """
        Resets the score. If the current score is higher than
        the high score, updates the high score in both memory
        and 'data.txt'.
        """

        if self.score > self.high_score:
            self.high_score = self.score
            #writing high score to file
            with open ("data.txt", "w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)