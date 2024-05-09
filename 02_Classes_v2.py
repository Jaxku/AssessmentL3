"""
This file contains the Question class which is used to create question objects.
This verison has the main logic for the quiz operation through a class system,
Overall this is the backend system for the quiz operation and the front end is
the gui
"""

import requests

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url=
"https://raw.githubusercontent.com/Jaxku/AssessmentL3/main/RawQuestionData.py"
                        , params=parameters)
# Pulls the question data from the API or external online source
question_data = response.json()["results"]


class Question: # This class is used to create question objects
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



