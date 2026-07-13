from data import get_question_bank
from quiz_brain import QuizBrain
from ui import QuizInterface

quiz = QuizBrain(get_question_bank())
quiz_ui = QuizInterface(quiz)
