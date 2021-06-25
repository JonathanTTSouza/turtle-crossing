from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(x=300, y=random.randint(-250, 250))

    def car_move(self, number_of_wins=0):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE - (MOVE_INCREMENT * number_of_wins/3)
        self.goto(x=new_x, y=self.ycor())




# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of
# the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our
# little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video
# walkthrough in Step 4.

# Detect when the turtle player collides with a car and stop the game if this happens. If you get stuck, check the
# video walkthrough in Step 5.

