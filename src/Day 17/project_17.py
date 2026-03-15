# --- Project 17 ---

from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

qb = QuizBrain(question_bank)

while qb.still_has_questions():
    qb.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {qb.score:02}/{qb.question_number:02}")
