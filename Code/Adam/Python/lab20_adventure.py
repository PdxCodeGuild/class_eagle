'''
Lab 20: Adventure
Build a simple board game that runs on the terminal
'''

# Represent the board using a list of lists.
# Use two ints to represent that player's position on the board.
# Prompt the user for a command at every iteration of the game loop.

import textwrap
import random
import colorama
import time
import sys
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# functions
def delay_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def battle_damage():
    damage = random.int(1, 12)
    return damage



# Variables
timer = 0
fire_hp = 20
greta_hp = 30
water_lvl = 1
width = 12  # the width of the board
height = 10  # the height of the board
plot = 'Climate Change is attacking the Camp!\nWe must take action!'
sun = Back.LIGHTBLUE_EX + Fore.LIGHTYELLOW_EX + '\u2600'
cloud = Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX + '\u2601'
player = Fore.LIGHTBLUE_EX + Back.LIGHTGREEN_EX + '\u26F9'
fire = Back.LIGHTGREEN_EX + '🔥'
tree = Back.LIGHTGREEN_EX + '🌲'
lake = Back.LIGHTGREEN_EX + '🔵'
sky_tree = Back.LIGHTBLUE_EX + '🌲'
horizon = sky_tree*12
water = '💧'
health = '💗'
grass = Fore.LIGHTGREEN_EX + '\u2593'
camp = Back.LIGHTGREEN_EX + '\u26FA'
controls = Back.LIGHTBLUE_EX + Fore.BLACK + \
f'''    {cloud}   Commands   {sun}    
         [w] = up       
 [a] = left [d] = right 
        [s] = down      
      [e] = Action      
{horizon}'''
title = Back.LIGHTBLUE_EX + Fore.BLACK + f'''
   Greta Goes Camping!  '''

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        if j == 0 or j == 11:
            board[i].append(tree)
        else:
            board[i].append(grass)  # append an empty space to the board

# define the player position
player_i = 1
player_j = 2

# camp position
camp_i = 1
camp_j = 1

# fixed fire position
fire_i = random.randint(1, height - 2)
fire_j = random.randint(1, width - 2)
board[fire_i][fire_j] = fire

# lake position
lake_i = random.randint(1, height - 2)
lake_j = random.randint(1, width - 2)
board[lake_i][lake_j] = lake

# add 4 enemies in random locations
# for i in range(4):
#     # fire_num += 1
#     fire_i = random.randint(1, height - 2)
#     fire_j = random.randint(1, width - 2)
#     board[fire_i][fire_j] = fire
#     # enemies.append({'fire':fire_num, 'fire_i': fire_i, 'fire_j': fire_j, })

delay_print(plot)
print(title)
print(controls)
# loop until the user says 'done' or dies
while True:
    timer += 1
    # if timer%2

    # check if the player is on the same space as an fire
    if board[player_i][player_j] == fire:
        print(Fore.RED + 'FIRE!')
        action = input('What will you do? ')
        if action == 'e':
            water_lvl = -1
            print('The fire is extinguished.')
            board[player_i][player_j] = grass  # remove the fire from the board
        else:
            print('You faught the good fight.')
            break
    elif board[player_i][player_j] == lake:
        print(Fore.BLUE + 'Water! Precious Water!')
        action = input('What will you do? ')
        if action == 'e':
            water_lvl = 3
            print('You gather water with your handy bucket.')
            board[player_i][player_j] = grass  # remove the fire from the board
        else:
            print('Failure is not an option!')
            continue

    # print out the board
    for i in range(height):
        for j in range(width):
            if i == player_i and j == player_j: # if we're at the player location, print the player icon
                print(player, end= grass)
            elif i == camp_i and j == camp_j:   # if we're at the camp location, print the camp icon
                print(camp, end= '')
            elif i == fire_i and j == fire_j:
                print(fire, end= '')
            elif i == lake_i and j == lake_j:
                print(lake, end= '')
            else:
                print(board[i][j], end= grass)  # otherwise print the board square
        print()
    
    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command in ['left', 'a']:
        player_j -= 1  # move left
    elif command in ['right', 'd']:
        player_j += 1  # move right
    elif command in ['up', 'w']:
        player_i -= 1  # move up
    elif command in ['down', 's']:
        player_i += 1  # move down