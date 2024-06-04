"""
This code repersents the next button
This button will check the results of the user's answer
and move to the next question
"""

import requests
import tkinter as tk
from tkinter import Canvas, Label, StringVar


def next_btn(self):
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
