'''
Lab 19: Trivia API

Use the Open Trivia Database API to a write a quiz program.
'''

import html
import requests
import textwrap

difficulties = [
    { 'parameter': 'any', 'name': 'Any Difficulty'},
    { 'parameter': 'easy', 'name': 'Easy' },
    { 'parameter': 'medium', 'name': 'Medium' },
    { 'parameter': 'hard', 'name': 'Hard' }
]
types = [
    { 'parameter': 'any', 'name': 'Any Type'},
    { 'parameter': 'multiple', 'name': 'Multiple Choice' },
    { 'parameter': 'boolean', 'name': 'True / False' }
]
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

print('\nReady for a quiz?')
# Part 2

# Prompt the user for each of these parameters: difficulty, types, categories
difficulty_choice = input('''
How difficult would you like your quiz to be;
easy, medium, hard, or random?  ''')

types_choice = input('''
What type of questions would you like:
multiple choice, true or false, or a random type?  ''')

category_choice = input('''
What category would you like:
''')

# Include them in the request to get the list of questions
response = requests.get(    # request returns a list of 10 true/false computer questions.
    'https://opentdb.com/api.php?amount=10',     # Send a request to the following url
    params={
        'difficulties': difficulties,
        'types': types,
        'categories': categories,
    })    
data = response.json()
results = data['results']   # list of dictionaries
score = 0   # keep track of the score
counter = 0  # to track the number of questions asked
num_of_questions = len(results)

for key in results:
    print('-'*79)   # print a dividing line between questions
    counter += 1    # increment the counter
    question = textwrap.fill(html.unescape(key['question']), 79)  # wrap text and decode text
    correct_answer = key['correct_answer']  # will compare correct answer to user_anser
    user_answer = input(f'\n{counter}) {question} True/False: ').title()   # Ask the user each question and save their answer
    if correct_answer == user_answer:   # if the answers match increment the score
        score += 1
    
print(f'\nYou got {score} out of {num_of_questions}\n')     # At the end show them how many they got correct/incorrect
