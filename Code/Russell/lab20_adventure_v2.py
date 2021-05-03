import random
import colorama
from colorama import Fore, Back, Style
import pyfiglet
from pyfiglet import Figlet
colorama.init(autoreset=True)

custom_fig = Figlet(font='shadow')



def rps_game(score, c_score):
    if score == c_score:
        result = "It's a TIE!"

    elif score == 'rock' and c_score == 'paper':
        result = "Paper covers rock. You lose!"
    elif score == 'rock' and c_score == 'scissors':
        result = "Rock crushes scissors. You win!"
    elif score == 'paper' and c_score == 'rock':
        result = "Paper covers rock. You win!"
    elif score == 'paper' and c_score == 'scissors':
        result = "Scissors cut paper. You lose!"  
    elif score == 'scissors' and c_score == 'rock':
        result = "Rock crushes scissors. You lose!"
    elif score == 'scissors' and c_score == 'paper':
        result = "Scissors cut paper. You win!"
    return result
#Go back and import this from another file 

width = 20  # the width of the board
height = 20  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(Back.LIGHTGREEN_EX + Style.DIM + ' ')  # append an empty space to the board

# define the player position
player_i = 4
player_j = 4

# add 4 enemies in random locations
for i in range(4):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = u'\u2620'

for i in range(3):
    enemy2_i = random.randint(0, height - 1)
    enemy2_j = random.randint(0,width -1)
    if board[i][j] != u'\u2620':
        board[enemy2_i][enemy2_j] = '*'


# loop until the user says 'done' or dies
while True:

    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == 'l':
        player_j -= 1  # move left
    elif command == 'r':
        player_j += 1  # move right
    elif command == 'u':
        player_i -= 1  # move up
    elif command == 'd':
        player_i += 1  # move down

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == u'\u2620':
        print(custom_fig.renderText('You\'ve encountered an enemy!'))
        player_m = input('choose rock, paper, or scissors ')
        monster_m = 'paper'
        match_result = (rps_game(player_m,monster_m))
        Fore.LIGHTYELLOW_EX + Style.BRIGHT + match_result
        print(match_result)

     

        if match_result == 'Scissors cut paper. You win!':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '   
        else:
            print('you hestitated and were slain')
            break

    if board[player_i][player_j] == '*':
        print(custom_fig.renderText('You\'ve encountered an enemy!'))
        player_m = input('choose rock, paper, or scissors ')
        monster_m = 'scissors'
        match_result = (rps_game(player_m,monster_m))
        print(match_result)

        if match_result == "Rock crushes scissors. You win!":
            print(pyfiglet.figlet_format('you\'ve slain the enemy', font = "slant"  ))
            board[player_i][player_j] = ' '   
        else:
            print('you hestitated and were slain')
            break





            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + '☺', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()




