import random
import os
from colorama import Fore,Back, Style





width = 15  # the width of the board
height = 15  # the height of the board


def print_board(board):
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print(Back.GREEN+'😎', end=' ')
            else:
                print(Back.GREEN+board[i][j], end=' ')
        print(Style.RESET_ALL) 

def battle(player_life,life_bar):

    enemy_life = 3
    weapons = ['sword','magic','shield']
    while True:
        enemy_lifebar = '💜'*enemy_life
        print(enemy_lifebar)
        print(life_bar)
        user_weapon = input('Choose your weapon[sword, shield, magic]:')
        enemy_weapon = random.choice(weapons)
        if user_weapon == enemy_weapon:
            print('Draw! These sworn enemies are so evenly match! The battle continues!')
            continue
        elif user_weapon == "sword":
            if enemy_weapon == "magic":
                print('You hit the enemy.')
                enemy_life -= 1
            elif enemy_weapon == "shield":
                print('The enemy has hit you.')
                player_life -=1
        elif user_weapon == "magic":
            if enemy_weapon == "shield":
                print('You hit the enemy.')
                enemy_life -= 1
            elif enemy_weapon == "sword":
                print('The enemy has hit you.')
                player_life -=1
        elif user_weapon == "shield":
            if enemy_weapon == "sword":
                print('You hit the enemy.')
                enemy_life -= 1
            elif enemy_weapon == "magic":
                print('The enemy has hit you.')
                player_life -=1
        if enemy_life == 0:
            return 'win'
        elif player_life == 0:
            return 'lose'
        

            




landscape = ['🌲',' ']
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(random.choice(landscape))  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4

# add 4 enemies in random locations
for i in range(4):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = '👹'

player_life = 3
life_bar = '💗'*player_life
# loop until the user says 'done' or dies
while True:

    print_board(board)
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
    if board[player_i][player_j] == '👹':
        print('you\'ve encountered an enemy!')
        result = battle(player_life, life_bar)
        if result == 'win':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '  # remove the enemy from the board
            print('Hit [ENTER] to continue')
        elif result == 'lose':
            print('💀You have been slain by the enemy!💀')
            break
    # clearing the screen of the previous data
    os.system('cls')












