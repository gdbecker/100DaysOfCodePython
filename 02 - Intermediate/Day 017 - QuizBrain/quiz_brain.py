from question_model import Question

class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        question = self.questions_list[self.question_number]
        num = self.question_number + 1
        answer = input(f"Q{num}: {question.text} (True/False) ")
        self.question_number += 1
        self.check_answer(answer, question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score: {self.score}/{self.question_number}.\n")

    def still_has_questions(self):
        num_questions = len(self.questions_list) - 1

        if self.question_number >= num_questions:
            print("You've completed the quiz!")
            print(f"Final score: {self.score}/{self.question_number}!")
            return False
        else:
            return True

