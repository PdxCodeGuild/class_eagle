
# Lab 19 Trivia API
# In this lab an API is used to create a True/False trivia game

import requests
import json
import html

############################## Version 1 ############################

def version1():
    # Requesting data from api
    url = 'https://opentdb.com/api.php?amount=10&category=18&type=boolean'
    response = requests.get(url)
    data = response.json()

    # Game opener
    print('\nWelcome to Computer Science trivia! to play, answer the following questions with True or False \n')
    print('Answers other than "True" or "False" will be counted as wrong!\n')


    # Game running
    # this body of code prints the question, asks for and compares user input to the correct answer
    # score is changed accordingly
    score = 0
    for i in range(10):
        print(f'Question:{i+1}') 
        print(html.unescape(data['results'][i]['question']))
        answer = input('True or False? ')
        answer = answer.title()
        if answer == data['results'][i]['correct_answer']:
            print('You got it!')
            score += 1
            print(f'Score: {score}')
            print('\n')
        elif answer != data['results'][i]['correct_answer']: #since the only options are true or false != is used here
            print('Wrong!')
            print('\n')
        while i == 9:
            print(f'You got {score} questions correct!')    
            print('\n')
        


############################# VERSION 2 (UNFINISHED) ##############################

categories = [
    { 'parameter': 'any', 'name': 'Any Category' },
    { 'parameter': '9', 'name': 'General Knowledge' },
    { 'parameter': '10', 'name': 'Entertainment: Books' },
    { 'parameter': '11', 'name': 'Entertainment: Film' },
    { 'parameter': '12', 'name': 'Entertainment: Music' },
    { 'parameter': '13', 'name': 'Entertainment: Musicals &amp; Theatres' },
    { 'parameter': '14', 'name': 'Entertainment: Television' },
    { 'parameter': '15', 'name': 'Entertainment: Video Games' },
    { 'parameter': '16', 'name': 'Entertainment: Board Games' },
    { 'parameter': '17', 'name': 'Science &amp; Nature' },
    { 'parameter': '18', 'name': 'Science: Computers' },
    { 'parameter': '19', 'name': 'Science: Mathematics' },
    { 'parameter': '20', 'name': 'Mythology' },
    { 'parameter': '21', 'name': 'Sports' },
    { 'parameter': '22', 'name': 'Geography' },
    { 'parameter': '23', 'name': 'History' },
    { 'parameter': '24', 'name': 'Politics' },
    { 'parameter': '25', 'name': 'Art' },
    { 'parameter': '26', 'name': 'Celebrities' },
    { 'parameter': '27', 'name': 'Animals' },
    { 'parameter': '28', 'name': 'Vehicles' },
    { 'parameter': '29', 'name': 'Entertainment: Comics' },
    { 'parameter': '30', 'name': 'Science: Gadgets' },
    { 'parameter': '31', 'name': 'Entertainment: Japanese Anime &amp; Manga' },
    { 'parameter': '32', 'name': 'Entertainment: Cartoon &amp; Animations' }
]

# true/false game, see version 1 for more info
def true_false(info,num):
    print('\nWelcome to Ultimate Trivia! to play, answer the following questions with True or False \n')
    print('Answers other than "True" or "False" will be counted as wrong!\n')
    score = 0
    for i in range(num):
        print(f'Question:{i+1}')
        print(html.unescape(info['results'][i]['question']))
        answer = input('True or False? ')
        answer = answer.title()
        if answer == info['results'][i]['correct_answer']:
            print('You got it!')
            score += 1
        elif answer != info['results'][i]['correct_answer']:
            print('Wrong!')
            print('\n')
        while i == num - 1:
            print(f'\nYour score is {score} out of {num}!')    
            print('\n')
            break

# multiple choice game unfinished
def multiple_choice(info):
    print('Welcome to multiple choice trivia!')

# After receiving user desired game parameters we send a request using them, game type is ran depending on user input
def run_game(questions, category, difficulty, q_type):
    if difficulty == 'any':
        difficulty = ''
    url = f'https://opentdb.com/api.php?amount={questions}&category={category}&difficulty={difficulty}&type={q_type}'
    response = requests.get(url)
    data = response.json()
    if q_type == 'boolean':
        true_false(data,questions)
    else:
        multiple_choice(data)
        
# This function starts the game and asks user for inputs to pass through to game functions
def run():
    num_questions = int(input('How many questions would you like? \n'))
    for num in categories:
        print(num['parameter'],' : ', num['name'])
    cat = input('\nChoose a category by entering the corresponding number, or enter "any". ')
    diff = input('Do you want the questions to be easy, medium, hard, or any difficulty? ')
    ques = input('Do you want boolean (true or false) or multiple (multiple choice) questions? ')
    run_game(num_questions, cat, diff, ques)


def repl():
    run_again = 'y'
    while run_again == 'y':
        run()
        run_again = input('Would you like to play again? y/n ')

version1()