"""
Based off of V1 this verison checks if the user's answer is correct and updates the score
"""

import requests
import tkinter as tk
from tkinter import Canvas, Label, StringVar


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
