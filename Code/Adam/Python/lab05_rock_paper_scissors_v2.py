

# Lab 5: Rock, Paper, Scissor
# Let's play rock-paper-scissors with the computer.
# 1 - Ask the user for their choice (rock, paper, scissors)
# 2 - The computer will randomly choose rock, paper or scissors
# 3 - Determine who won and tell the user
# 4 - Give the user the choice of playing another round.


import random
# import time 

options = ['rock', 'paper', 'scissor']


while True:
    # time(1)
    # print('Welcome to...')
    # time(1)
    # print('')
    play = input('Would you like to play a round of Rock, Paper, Scissor? ').lower()
    if play in ['yes', 'y']:
        users_choice = input('Enter rock, paper, or scissor: ').lower()

        comp_choice = random.choice(options)

        print(f'\nPlayer: {users_choice} | Computer: {comp_choice} \n')

        if users_choice == comp_choice:
            print('It\'s a tie! \n')
        elif users_choice == 'rock' and comp_choice != 'paper':
            print('You Win! \n')
        elif users_choice == 'paper' and comp_choice != 'scissor':
            print('You Win! \n')
        elif users_choice == 'scissor' and comp_choice != 'rock':
            print('You Win! \n')
        else:
            print('You Lose! \n')

    elif play in ['no', 'n']:
        print('\nGoodbye!\n')
        break

    else:
        print(f'{play} is not a valid response dummy.')


