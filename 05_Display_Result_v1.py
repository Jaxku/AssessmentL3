"""
This displays the result of the quiz in a new window
Only one verison needed as it is a basic function
"""

import requests
import tkinter as tk
from tkinter import Canvas, messagebox, Label


def display_result(self):
    # To display the result using messagebox
    correct, wrong, score_percent = self.quiz.get_score()

    correct = f"Correct: {correct}"
    wrong = f"Wrong: {wrong}"

    # Calculate the percentage of correct answers
    result = f"Score: {score_percent}%"

    # Show a message box to display the result
    messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")

