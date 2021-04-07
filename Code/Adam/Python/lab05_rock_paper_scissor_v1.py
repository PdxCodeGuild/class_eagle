

# Lab 5: Rock, Paper, Scissor
# Let's play rock-paper-scissors with the computer.
# 1 - Ask the user for their choice (rock, paper, scissors)
# 2 - The computer will randomly choose rock, paper or scissors
# 3 - Determine who won and tell the user


import random

options = ['rock', 'paper', 'scissor']

# users_choice = input('\nEnter rock, paper, or scissors: ').lower()
users_choice = 'rock' # for testing

comp_choice = random.choice(options)

# print(users_choice)
# print(comp_choice)

print(f'\nPlayer: {users_choice} | Computer: {comp_choice} \n')

if users_choice == comp_choice:
    print('It\'s a Draw! \n')
elif users_choice == 'rock' and comp_choice != 'paper':
    print('You Win! \n')
elif users_choice == 'paper' and comp_choice != 'scissor':
    print('You Win! \n')
elif users_choice == 'scissor' and comp_choice != 'rock':
    print('You Win! \n')
else:
    print('You Lose! \n')
