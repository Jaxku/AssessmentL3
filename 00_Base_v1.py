"""
Base v1
"""

import requests
import tkinter as tk
from tkinter import Canvas, Label, StringVar, messagebox

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url="https://raw.githubusercontent.com/Jaxku/AssessmentL3/main/RawQuestionData.py", params=parameters)
question_data = response.json()["results"]


class Question:
    def __init__(self, question: str, correct_answer: str, choices: list):
        self.question = question
        self.correct_answer = correct_answer
        self.choices = choices


class QuizOperation:

    def __int__(self, questions):
        # This class is used to create the quiz operation
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def anymore_questions(self):
        # This function checks if the quiz has more questions
        return self.question_no < len(self.questions)


    def next_question(self):
       # This function gets the next question in the quiz

        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        q_text = self.current_question.question_text
        return f"Q.{self.question_no}: {q_text}"

    def check_answer(self, user_answer):
        # This function checks if the user's answer is correct via class system

        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def get_score(self):
        # This function gets the score of the user, in later verisons this will
        # write to a text file.

        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return (self.score, wrong, score_percent)


def next_button(self):
    """To show feedback for each answer and keep checking for more questions"""

    # Check if the answer is correct
    if self.quiz.check_answer(self.user_answer.get()):
        self.feedback["fg"] = "green"
        self.feedback["text"] = 'Correct answer! \U0001F44D'
    # If the answer is wrong
    else:
        self.feedback['fg'] = 'red'
        self.feedback['text'] = ('\u274E Incorrect! \n'
                                     f'The right answer is: '
                                 f'{self.quiz.current_question.correct_answer}'
                                 f'\nYou selected: {self.user_answer.get()}')

    if self.quiz.has_more_questions():
        # Moves to next to display next question and its options
        self.display_question()
        self.display_options()
    else:
        # if no more questions, then it displays the score
        self.display_result()

        # destroys the self.window
        self.window.destroy()


    def display_result(self):
        # To display the result using messagebox
    correct, wrong, score_percent = self.quiz.get_score()

    correct = f"Correct: {correct}"
    wrong = f"Wrong: {wrong}"

    # Calculate the percentage of correct answers
    result = f"Score: {score_percent}%"

    # Show a message box to display the result
    messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")


class QuizGUI:
    def __init__(self, quiz: QuizOperation):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title("iQuiz Application")
        self.window.geometry("800x600")

        # Display the title
        self.display_title()

        # Display question area
        self.canvas = Canvas(self.window, width=800, height=250)
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        # Display options
        self.opts = []
        self.display_options()

        # User answer variable
        self.user_answer = StringVar()

        # Feedback label
        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.grid(row=5, column=0, columnspan=2)

        # Next and Quit buttons
        self.buttons()

        # Mainloop
        self.window.mainloop()

    def display_title(self):
        title = Label(self.window, text="iQuiz Application",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=10)

    def display_question(self):
        self.canvas.delete("question")
        q_text = self.quiz.next_question()
        self.canvas.create_text(400, 125, text=q_text, width=680,
                                fill="black", font=('Helvetica', 15, 'bold'), tag="question")

    def display_options(self):
        self.opts.clear()
        choices = self.quiz.current_question.choices
        for i, choice in enumerate(choices):
            rb = tk.Radiobutton(self.window, text=choice, variable=self.user_answer,
                                value=choice, font=('Helvetica', 12))
            self.opts.append(rb)
            rb.grid(row=3+i, column=0, columnspan=2)

    def buttons(self):
        next_button = tk.Button(self.window, text="Next", command=self.check_answer)
        next_button.grid(row=4+len(self.opts), column=0, pady=20)
        quit_button = tk.Button(self.window, text="Quit", command=self.window.destroy)
        quit_button.grid(row=4+len(self.opts), column=1, pady=20)

    def check_answer(self):
        selected_answer = self.user_answer.get()
        if self.quiz.check_answer(selected_answer):
            self.quiz.score += 1
            self.feedback.config(text="Correct!", fg="green")
        else:
            self.feedback.config(text="Wrong!", fg="red")

        if self.quiz.anymore_questions():
            self.display_question()
            self.display_options()
        else:
            score, wrong, percent = self.quiz.get_score()
            self.feedback.config(text=f"Quiz Ended!\nScore: {score}/{self.quiz.question_no}\n"
                                       f"Wrong: {wrong}\nPercent: {percent}%")

        def display_title(self):  # Display title
            title = Label(self.window, text="Maori Quiz",
                              width=50, bg="green", fg="white", font=("ariel", 20, "bold"))
            title.place(x=0, y=2)
