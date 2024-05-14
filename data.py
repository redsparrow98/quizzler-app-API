import requests


# assign the parameters for the quizz API
parameters = {
    "amount": 10,
    "type": "boolean"
}

# Request a response from the API and save the result key values from the API as data
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()["results"]

# set the questions_data to be the data from the api
question_data = data
