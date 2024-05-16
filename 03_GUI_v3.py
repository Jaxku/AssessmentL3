"""
Adds the addition of the GUI to the quiz application, adds to first verison
still not working as intended, will be fixed in later verisons
"""

import requests  # To handle HTTP requests, if needed
import tkinter as tk  # For GUI creation
from tkinter import Canvas, Label, StringVar, Radiobutton  # Specific tkinter components for convenience

class QuizGUI:
    def __init__(self, quiz):
        """
        Initialize the Quiz GUI.

        :param quiz: An instance of the QuizOperation class that contains quiz logic and data.
        """
        self.quiz = quiz  # Store the quiz instance
        self.window = tk.Tk()  # Create the main window
        self.window.title("Maori Quiz!")  # Set the window title
        self.window.geometry("800x600")  # Set the window size

        # Display the title
        self.display_title()

        # Set up the canvas for the question text
        self.canvas = Canvas(self.window, width=800, height=250)
        self.question_text = self.canvas.create_text(
            400, 125, text="Question", width=680,
            fill="black", font=('Arial', 15, 'bold'),
            tag="question"
        )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)

        # Display the first question
        self.display_question()

        # Set up the radio buttons for the options
        self.opts = self.radio_buttons()
        self.display_options()

        # Variable to store the user's answer
        self.user_answer = StringVar()

        # Label to give feedback on the user's answer
        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.grid(row=5, column=0, columnspan=2)

        # Set up the Next and Quit buttons
        self.buttons()

        # Start the main loop
        self.window.mainloop()

    def display_title(self):
        """
        Display the title of the quiz application.
        """
        title = Label(self.window, text="iQuiz Application",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=10)

    def display_question(self):
        """
        Display the next question on the canvas.
        """
        self.canvas.delete("question")  # Remove the previous question
        q_text = self.quiz.next_question()  # Get the next question
        self.canvas.create_text(
            400, 125, text=q_text, width=680,
            fill="black", font=('Arial', 15, 'bold'),
            tag="question"
        )

    def radio_buttons(self):
        """
        Create radio buttons for the quiz options.

        :return: A list of radio buttons.
        """
        choice_list = []  # Initialize the list for radio buttons
        y_pos = 220  # Starting y-position for the first radio button

        for _ in range(4):  # Create 4 radio buttons
            radio_btn = Radiobutton(
                self.window, text="", variable=self.user_answer,
                value='', font=("ariel", 14)
            )
            choice_list.append(radio_btn)  # Add the radio button to the list
            radio_btn.place(x=200, y=y_pos)  # Place the radio button in the window
            y_pos += 40  # Move the y-position for the next radio button

        return choice_list

    def display_options(self):
        """
        Display the options for the current question.
        """
        self.user_answer.set(None)  # Deselect any previously selected option
        self.opts.clear()  # Clear the current list of radio buttons

        choices = self.quiz.current_question.choices  # Get the current question choices
        for i, choice in enumerate(choices):  # Create a radio button for each choice
            rb = tk.Radiobutton(
                self.window, text=choice, variable=self.user_answer,
                value=choice, font=('Helvetica', 12)
            )
            self.opts.append(rb)  # Add the radio button to the list
            rb.grid(row=3+i, column=0, columnspan=2)  # Place the radio button in the grid

    def buttons(self):
        """
        Create the Next and Quit buttons.
        """
        next_button = tk.Button(self.window, text="Next", command=self.check_answer)
        next_button.grid(row=4+len(self.opts), column=0, pady=20)

        quit_button = tk.Button(self.window, text="Quit", command=self.window.destroy)
        quit_button.grid(row=4+len(self.opts), column=1, pady=20)

    def check_answer(self):
        """
        Check the user's answer and update the quiz state.
        """
        selected_answer = self.user_answer.get()  # Get the selected answer
        if self.quiz.check_answer(selected_answer):  # Check if the answer is correct
            self.quiz.score += 1  # Increment the score if correct
            self.feedback.config(text="Correct!", fg="green")
        else:
            self.feedback.config(text="Wrong!", fg="red")

        if self.quiz.anymore_questions():  # Check if there are more questions
            self.display_question()  # Display the next question
            self.display_options()  # Display the options for the next question
        else:
            score, wrong, percent = self.quiz.get_score()  # Get the final score
            self.feedback.config(text=f"Quiz Ended!\nScore: {score}/{self.quiz.question_no}\n"
                                       f"Wrong: {wrong}\nPercent: {percent}%")

# Assuming the class QuizOperation is defined elsewhere and passed into QuizGUI
# class QuizOperation:
#     def next_question(self):
#         pass
#     def check_answer(self, answer):
#         pass
#     def anymore_questions(self):
#         pass
#     def get_score(self):
#         pass

# Example usage
# quiz = QuizOperation()
# quiz_gui = QuizGUI(quiz)
