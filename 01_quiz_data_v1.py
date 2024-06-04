"""
This file is used to get the quiz data from the API.
"""
import requests

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url="https://raw.githubusercontent.com/Jaxku/AssessmentL3/main/RawQuestionData.py", params=parameters)
question_data = response.json()["results"]
