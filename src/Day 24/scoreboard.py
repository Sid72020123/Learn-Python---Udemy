from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        highscore_file = open("highscore.txt", "r")
        self.highscore = int(highscore_file.read())
        highscore_file.close()
        self.display_score(0)

    def display_score(self, score):
        self.clear()
        self.goto(0, 260)
        if score >= self.highscore:
            self.highscore = score
            with open("highscore.txt", "w") as file:
                file.write(str(self.highscore))
        self.write(
            f"Score: {score:02}, HighScore: {self.highscore:02}",
            align=ALIGNMENT,
            font=FONT,
        )

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
