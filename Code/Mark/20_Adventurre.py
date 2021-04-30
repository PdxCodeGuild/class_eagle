import random
import os


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

# add 4 enemies in random locations
for i in range(6):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '§'

player_life = 3
life_bar = 'Ω'*player_life
# loop until the user says 'done' or dies
while True:
    print(f'Player Life: {life_bar}')
    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'left':
        player_j -= 1  # move left
    elif command == 'right':
        player_j += 1  # move right
    elif command == 'up':
        player_i -= 1  # move up
    elif command == 'down':
        player_i += 1  # move down

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            user_attack = random.randint(1,10)
            enemy_attack = random.randint(1,10)
            if user_attack > enemy_attack:
                print('you\'ve slain the enemy')
                board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('The enemy successfully counter-attacked!')
            player_life -= 1
            if player_life == 0:
                print('You have been slain by the enemy ')
                break
    # clearing the screen of the previous data
    os.system('cls')


    # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('♿', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()