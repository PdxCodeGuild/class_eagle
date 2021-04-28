import requests
import json
import html

url = 'https://opentdb.com/api.php?amount=10&category=18&type=boolean'
response = requests.get(url)
data = response.json()

print('\nWelcome to Computer Science trivia! to play, answer the following questions with True or False \n')
print('Answers other than "True" or "False" will be counted as wrong!\n')

score = 0
for i in range(10):
    print(f'Question:{i+1}')
    print(html.unescape(data['results'][i]['question']))
    answer = input('True or False? ')
    if answer == data['results'][i]['correct_answer']:
        print('You got it!')
        score += 1
        print(f'Score: {score}')
        print('\n')
    elif answer != data['results'][i]['correct_answer']:
        print('Wrong!')
        print('\n')
    while i == 9:
        print(f'You got {score} questions correct!')    
        print('\n')
        break
    