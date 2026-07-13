import html

from data import get_question_bank


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number:02}: {q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        return user_answer.lower() == correct_answer.lower()

    def refresh_question_bank(self):
        self.question_number = 0
        self.score = 0
        self.question_list = get_question_bank()
        self.current_question = None
