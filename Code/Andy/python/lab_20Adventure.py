import random
import json
import requests
import html

def sphinx():
    # Requesting data from api
    url = 'https://opentdb.com/api.php?amount=1&difficulty=easy&type=boolean'
    response = requests.get(url)
    data = response.json()

    # Game opener
    print('\nAnswer the following question with True or False \n')
    print('Answers other than "True" or "False" will be counted as wrong!\n')

    # Game running
    # this body of code prints the question, asks for and compares user input to the correct answer
    # score is changed accordingly
    score = 0
    for i in range(1):
        print(html.unescape(data['results'][i]['question']))
        answer = input('True or False? ')
        answer = answer.title()
        if answer == data['results'][i]['correct_answer']:
            score += 1
            print('\n')
            return True
        elif answer != data['results'][i]['correct_answer']: #since the only options are true or false != is used here
            print('Wrong!')
            print('\n')
            return False


width = 10  # the width of the board
height = 10  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4

# add enemies in random locations
for i in range(3):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = 'd'

# add enemies in random locations
for i in range(3):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = 's'
'''
# add enemies in random locations
for i in range(2):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = 'l'
'''

print('You\'ve been dropped in a dungeon full of monsters! Bargain your way out!')

# loop until the user says 'done' or dies
while True:

    count = 0
    command = input('WASD + enter to move. Enter any movement to start ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'a':
        player_j -= 1  # move left
    elif command == 'd':
        player_j += 1  # move right
    elif command == 'w':
        player_i -= 1  # move up
    elif command == 's':
        player_i += 1  # move down

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == 'd':
        print('you\'ve encountered a dragon! luckily it has a crippling gambling addiction. ')
        guess = input('If you win a coin flip it will leave you alone! heads or tails? ')
        guess = guess.title()
        choices = ['Heads','Tails']
        coin = random.choice(choices)
        if guess == coin:
            print('Good guess!')
            board[player_i][player_j] = ' '  # remove the enemy from the board
            count += 1
        else:
            print(f'It wasn\'t {guess}, you were mauled by the dragon :( GAME OVER ')
            break
    elif board[player_i][player_j] == 's':
        print('You\'ve come across a Sphinx! Answer the question correctly to continue your journey.')
        win = sphinx()
        if win == True:
            print('Nice answer! the sphinx left. ')
            board[player_i][player_j] = ' '  # remove the enemy from the board
            count += 1
        else:
            print('You answered incorrectly and the sphinx had a nice lunch. \n')
            print('Game Over...')
            break

    elif count == 8:
        print('Congratulations! You\' cleared out the dungeon! ')        
        break
            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('⋆', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
    
        print()
