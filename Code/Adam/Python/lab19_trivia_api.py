'''
Lab 19: Trivia API

Use the Open Trivia Database API to a write a quiz program.
'''

import html
import requests
import textwrap

url = 'https://opentdb.com/api.php?amount=10&category=18&type=boolean'

# Send a request to the following url
response = requests.get(url)
# this will return a list of 10 true/false computer questions.
data = response.json()
results = data['results']

score = 0   # keep track of the score
counter = 0
num_of_questions = len(results)

print('\nReady for a quiz?')

for key in results:
    print('-'*79)
    counter += 1
    question = textwrap.fill(key['question'], 79)  # questions will wrap if too long
    correct_answer = key['correct_answer']  # will compare correct answer to user_anser
    user_answer = input(f'\n{counter}) {question} True/False: ')    # Ask the user each question and save their answer
    if correct_answer == user_answer:   # if the answers match increment the score
        score += 1
    
print(f'\nYou got {score} out of {num_of_questions}\n')     # At the end show them how many they got correct/incorrect