"""
This file contains the Question class which is used to create question objects.

"""

import requests

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
