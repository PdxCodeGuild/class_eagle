import requests
import html
from random import *
import json
# some sweet ascii art
print('''          Let's play:
------------------------------------------------------
 ______     __  __     ______   ______     ______      
/\  ___\   /\ \/\ \   /\  == \ /\  ___\   /\  == \     
\ \___  \  \ \ \_\ \  \ \  _-/ \ \  __\   \ \  __<     
 \/\_____\  \ \_____\  \ \_\    \ \_____\  \ \_\ \_\   
  \/_____/   \/_____/   \/_/     \/_____/   \/_/ /_/   
 ______   ______     __     __   __   __     ______    
/\__  _\ /\  == \   /\ \   /\ \ / /  /\ \   /\  __ \   
\/_/\ \/ \ \  __<   \ \ \  \ \ \\'/   \ \ \  \ \  __ \  
   \ \_\  \ \_\ \_\  \ \_\  \ \__|    \ \_\  \ \_\ \_\ 
    \/_/   \/_/ /_/   \/_/   \/_/      \/_/   \/_/\/_/ 
------------------------------------------------------                                                       
''')







# Function for the trivia itself
def quiz(selected_amount,selected_category,selected_difficulty,selected_type):

    response = requests.get('https://opentdb.com/api.php?', params={'amount': selected_amount, 'category': selected_category, 'difficulty': selected_difficulty, 'type':selected_type})
    trivia = response.text
    trivia = json.loads(trivia)

    # conditional in case there are no results from the response
    if trivia['response_code'] == 1:
        return 'No results'

    score = 0
    # using a for loop to iteratate through the data and present the Q+A
    for i in range(len(trivia['results'])):
        # printing out the current score to the user
        print(f'Current Score: {score}/{selected_amount}')

        # creating a blank list for the answers
        answer_list = []
        correct_answer = trivia['results'][i]['correct_answer']
        incorrect_answers = trivia['results'][i]['incorrect_answers']
        print('\n')

        # presenting the question to the user
        print(f"Question: {html.unescape(trivia['results'][i]['question'])}")

        # appending the answers to the blank list
        answer_list.append(correct_answer)
        for answers in incorrect_answers:
            answer_list.append(answers)

        # shuffling the answers
        shuffle(answer_list)

        # Presenting the answers for the user to choose from
        for i in range(len(answer_list)):
            print(f'{i}. {html.unescape(answer_list[i])}')

        # checking to see if the user answered correctly and adding onto the score if they are correct
        user_answer = input('Answer: ')
        print('-------------------------')
        print(f'Correct answer: {correct_answer}')
        if user_answer == correct_answer:
            score += 1
    return score

difficulties = [
    { 'parameter': 'Hit [Enter]', 'name': 'Any'},
    { 'parameter': 'easy', 'name': 'Easy' },
    { 'parameter': 'medium', 'name': 'Medium' },
    { 'parameter': 'hard', 'name': 'Hard' }
]
types = [
    { 'parameter': 'Hit [Enter]', 'name': 'Any'},
    { 'parameter': 'multiple', 'name': 'Multiple Choice' },
    { 'parameter': 'boolean', 'name': 'True / False' }
]
 
categories = [
    { 'parameter': 'Hit [Enter]', 'name': 'Any'},
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



while True:

    print('\n')
    # using for loops to present the options for trivia and asking the user to pick from them

    for i in range(len(categories)):
        print(f"{categories[i]['parameter']}. {html.unescape(categories[i]['name'])}")
    selected_category = input('Enter a trivia category[enter the corresponding number]: ')

    print("-------------------------------------------------------------------------------------------")
    for i in range(len(difficulties)):
        print(f"For {difficulties[i]['name']} enter {difficulties[i]['parameter']}")
    selected_difficulty = input('Select your difficulty: ')
    print("-------------------------------------------------------------------------------------------")
    for i in range(len(types)):
        print(f"For {types[i]['name']} enter {types[i]['parameter']}")
    selected_type = input('Select your trivia type: ')
    print("-------------------------------------------------------------------------------------------")
    selected_amount = int(input('How many questions would you like? '))


    # sending the user choices to the function 
    final_score = quiz(selected_amount,selected_category,selected_difficulty,selected_type)

    if final_score == 'No results':
        print('\n')
        print("-------------------------------------------------------------------------------------------")
        print(f'Sorry but there were no results with that criteria.')
        print("-------------------------------------------------------------------------------------------")
    else:
        # presenting the final score to the user
        print('\n')
        print("-------------------------------------------------------------------------------------------")
        print(f'Final Score is: {final_score}/{selected_amount}')
        print("-------------------------------------------------------------------------------------------")

    play_again = input('Would you like to try again? ')
    if play_again != 'yes':
        break
print('\n')
# some more awesome ascii art to say goodbye
print('''     Thank you for playing:
---------------------------------------------------
 ______     __  __     ______   ______     ______      
/\  ___\   /\ \/\ \   /\  == \ /\  ___\   /\  == \     
\ \___  \  \ \ \_\ \  \ \  _-/ \ \  __\   \ \  __<     
 \/\_____\  \ \_____\  \ \_\    \ \_____\  \ \_\ \_\   
  \/_____/   \/_____/   \/_/     \/_____/   \/_/ /_/   
 ______   ______     __     __   __   __     ______    
/\__  _\ /\  == \   /\ \   /\ \ / /  /\ \   /\  __ \   
\/_/\ \/ \ \  __<   \ \ \  \ \ \\'/   \ \ \  \ \  __ \  
   \ \_\  \ \_\ \_\  \ \_\  \ \__|    \ \_\  \ \_\ \_\ 
    \/_/   \/_/ /_/   \/_/   \/_/      \/_/   \/_/\/_/ 
------------------------------------------------------
''')

