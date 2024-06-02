"""

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
    """Class to handle the quiz operations or the brains of the quiz."""

    def __init__(self, questions):
        """Initialize the quiz operation with a list of questions."""
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def anymore_questions(self):
        """Check if there are more questions in the quiz."""
        return self.question_no < len(self.questions)

    def next_question(self):
        """Get the next question in the quiz."""
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        return f"Q.{self.question_no}: {self.current_question.question}"

    def check_answer(self, user_answer):
        """Check if the user's answer is correct."""
        correct_answer = self.current_question.correct_answer
        return user_answer.lower() == correct_answer.lower()

    def get_score(self):
        """Get the final score."""
        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return self.score, wrong, score_percent




