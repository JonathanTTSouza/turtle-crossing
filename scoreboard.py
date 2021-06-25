from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)

    def write_scoreboard(self, number_of_wins):
        self.clear()
        self.write(f"Level: {number_of_wins + 1}", move=False, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", move=False, font=FONT, align="center")

# Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful
# crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. If
# you get stuck, check the video walkthrough in Step 7.
