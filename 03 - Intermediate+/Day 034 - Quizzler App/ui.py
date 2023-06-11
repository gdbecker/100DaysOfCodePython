THEME_COLOR = "#375362"
FONT_NAME = "Arial"

# Make the app UI
# Import modules
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=(FONT_NAME, 10))
        self.score_label.grid(column=2, row=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", fill=THEME_COLOR, font=(FONT_NAME, 18, "italic"))
        self.canvas.grid(column=1, row=2, columnspan=2)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, command=self.true)
        self.true_button.grid(column=1, row=3, padx=20, pady=20)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, command=self.false)
        self.false_button.grid(column=2, row=3, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
        question_result = self.quiz.check_answer("True")
        if question_result == "Correct":
            self.score_label.config(text=f"Score: {self.quiz.score}")
        self.give_feedback(question_result)
        # self.get_next_question()

    def false(self):
        question_result = self.quiz.check_answer("False")
        if question_result == "Correct":
            self.score_label.config(text=f"Score: {self.quiz.score}")
        self.give_feedback(question_result)
        # self.get_next_question()

    def give_feedback(self, question_result):
        if question_result == "Correct":
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)