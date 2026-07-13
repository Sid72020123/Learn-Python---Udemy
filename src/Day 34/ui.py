from tkinter import *
from tkinter import messagebox

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 00 / 00", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question here...",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.tick_image = PhotoImage(file="images/true.png")
        self.cross_image = PhotoImage(file="images/false.png")

        self.cross_button = Button(
            image=self.cross_image, highlightthickness=0, command=self.cross_pressed
        )
        self.tick_button = Button(
            image=self.tick_image, highlightthickness=0, command=self.tick_pressed
        )

        self.cross_button.grid(row=2, column=0)
        self.tick_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self._update_score_label()
        if not self.quiz.still_has_questions():
            messagebox.showinfo(
                title="Quizzler: Question Set Complete!",
                message=f"Question Set Complete!\n\nYour score was {self.quiz.score:02} / {self.quiz.question_number:02}",
            )
            self.quiz.refresh_question_bank()
            self._update_score_label()

        question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question)

    def _update_score_label(self):
        self.score_label.config(
            text=f"Score: {self.quiz.score:02} / {self.quiz.question_number:02}"
        )

    def _check_answer(self, t):
        is_correct = self.quiz.check_answer(t)
        if is_correct:
            self.quiz.score += 1
        self.get_next_question()

    def tick_pressed(self):
        self._check_answer("True")

    def cross_pressed(self):
        self._check_answer("False")
