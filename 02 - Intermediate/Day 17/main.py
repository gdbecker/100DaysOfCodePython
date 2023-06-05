# 100 Days of Code: Python
# May 13, 2022
# True/False quiz game with OOP

# Import classes
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

# Make question bank
question_bank = []
for q in question_data:
    new_question = Question(q["text"], q["answer"])
    question_bank.append(new_question)

# Make quiz brain
quiz = QuizBrain(question_bank)
quiz.next_question()

# Game loop
while quiz.still_has_questions():
    quiz.next_question()




