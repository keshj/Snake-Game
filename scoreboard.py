from turtle import Turtle
ALIGNMENT = 'center'
FONT = 'Courier'
FONT_SIZE = 20
FONT_TYPE = 'bold'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.increment_score()

    def increment_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_TYPE))
