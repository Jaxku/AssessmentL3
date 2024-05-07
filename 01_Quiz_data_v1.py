import requests

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
