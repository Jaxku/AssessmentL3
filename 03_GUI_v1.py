"""
Adds the addition of the GUI to the quiz application, this is the first version
"""

import requests
import tkinter as tk
from tkinter import Canvas, Label, StringVar


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
                                fill="black", font=('Arial', 15, 'bold'),
                                tag="question")

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
