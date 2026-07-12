from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):

        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(height=300, width=250, bg="white", highlightthickness=0)

        self.canvas.grid(row=1, column=0, columnspan=2)

        self.tick_image = PhotoImage(file="images/true.png")
        self.cross_image = PhotoImage(file="images/false.png")

        self.tick_button = Button(image=self.tick_image)
        self.cross_button = Button(image=self.cross_image)

        self.tick_button.grid(row=2, column=0, highlightthickness=0)
        self.cross_button.grid(row=2, column=1, highlightthickness=0)

        self.window.mainloop()
