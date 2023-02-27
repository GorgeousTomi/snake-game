from turtle import Turtle

with open("data.txt") as reading:
    content = reading.read()

ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(content)
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(arg=f"Score : {self.score}  High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as writing:
                writing.write(str(self.high_score))
        # self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.reset()
        self.update_score_board()


