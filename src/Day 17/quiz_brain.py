from question_model import Question


class QuizBrain:
    def __init__(self, questions_list: list[Question]) -> None:
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        answer = (
            input(
                f"Q.{self.question_number+1:02}: {current_question.text} (True/False)?: "
            )
            .strip()
            .lower()
        )

        if answer in ["true", "t", "yes", "y"]:
            user_answer = "true"
        elif answer in ["false", "f", "no", "n"]:
            user_answer = "false"
        else:
            # print("\nYou've given the wrong input! Please try again...\n")
            user_answer = ""

        if user_answer == current_question.answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {current_question.answer}")
        print(f"Your current score is {self.score:02}/{self.question_number+1:02}.\n\n")

        self.question_number += 1
