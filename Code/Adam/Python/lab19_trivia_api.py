'''
Lab 19: Trivia API

Use the Open Trivia Database API to a write a quiz program.
'''

import html
import requests

url = 'https://opentdb.com/api.php?amount=10&category=18&type=boolean'

response = requests.get(url)
data = response.json()

print(data)