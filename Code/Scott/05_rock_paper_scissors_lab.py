import random as rand
import os
import time
from art import *

actions = ['rock', 'paper', 'scissors']
bot_choice = rand.randint(0, 2)
scores = [0, 0]
round_count = 0

def ShootAnim(a, b, c):
        actions_anim = ['👊', '✋', '✌']
        actions_obj = ['🗿', '📃', '✂️']

        os.system('cls||clear')
        print(text2art('      '))
        print('''
                ✊                      ✊
                        R E A D Y ?
        ''')
        time.sleep(1)

        os.system('cls||clear')
        print(text2art('ROCK'))
        print('''
                                       
                ✊                      ✊
        ''')
        time.sleep(1)

        os.system('cls||clear')
        print(text2art('      '))
        print('''
                ✊                      ✊
                       
        ''')
        time.sleep(1)

        os.system('cls||clear')
        print(text2art('PAPER'))
        print('''
                                       
                ✊                      ✊
        ''')
        time.sleep(1)

        os.system('cls||clear')
        print(text2art('      '))
        print('''
                ✊                      ✊
                       
        ''')
        time.sleep(1)

        os.system('cls||clear')
        print(text2art('SCISSORS'))
        print('''
                                     
                ✊                      ✊
        ''')
        time.sleep(1)

        os.system('cls||clear')
        print(text2art('      '))
        print('''
                ✊                      ✊
                       
        ''')
        time.sleep(1)

        os.system('cls||clear')
        print(text2art('     '))
        print('''
                                     
                ✊                      ✊
        ''')
        time.sleep(1)

        os.system('cls||clear')
        print(text2art('SHOOT!'))
        print(f'''
                                      
                {actions_anim[a]}                      {actions_anim[b]}


        ''')
        time.sleep(1)

        os.system('cls||clear')
        print(text2art('SHOOT!'))
        print(f'''
                                      
                {actions_anim[a]}                      {actions_anim[b]}

                {actions_obj[a]}                      {actions_obj[b]}
        ''')

        os.system('cls||clear')
        print(text2art('SHOOT!'))
        print(f'''
                                      
                {actions_anim[a]}                      {actions_anim[b]}

                {actions_obj[a]}                      {actions_obj[b]}
        ''')
        message = f'You chose {actions[user_choice]}, the bot chose {actions[bot_choice]}'
        for char in message:
            print(char, end='', flush=True)
            time.sleep(.05)
        time.sleep(1)

        
        os.system('cls||clear')
        print(text2art('SHOOT!'))
        print(f'''
                                      
                {actions_anim[a]}                      {actions_anim[b]}

                {actions_obj[a]}                      {actions_obj[b]}
        ''')
        if c == 1:
            message_2 = 'You won!'
        elif c == 0:
            message_2 = 'It\'s a tie...'
        elif c == -1:
            message_2 = 'The Bot won!'

        for char in message_2:
            print(char, end='', flush=True)
            time.sleep(.05)


def RoundLogic(a, b):
    if bot_choice == 0 and user_choice == 2:
        scores[1] += 1
        return -1
    elif user_choice == 0 and bot_choice == 2:
        scores[0] += 1
        return 1
    else:
        if bot_choice > user_choice:
            scores[1] += 1
            return -1
        elif user_choice > bot_choice:
            scores[0] += 1
            return 1
        else:
            scores[0] += 1
            scores[1] += 1
            return 0


while True: #REPL for repeating rounds
    while True: #REPL for input of rock, paper, scissors
        user_choice = input('Rock, paper, or scissors?: ').lower()
        if user_choice == actions[0] or user_choice == actions[1] or user_choice == actions[2]:
            break
        else:
            print('invalid choice')

    user_choice = actions.index(user_choice)
    round_win = RoundLogic(user_choice, bot_choice)
    ShootAnim(user_choice, bot_choice, round_win)


    round_count += 1
    print(f'''
    ===============================
        S C O R E B O A R D
            You: {scores[0]} | Bot: {scores[1]}
        Rounds Played: {round_count}
    ===============================
    ''')

    while True: #REPL for play again input
        go_again = input('play again? (y/n) ').lower()
        if go_again == 'y' or go_again == 'n':
            break
        else:
            print('invalid choice')
    os.system('cls||clear')
    if go_again == 'n':
        print(f'''
            F I N A L   S C O R E
        ===============================
            S C O R E B O A R D
             You: {scores[0]} | Bot: {scores[1]}
            Rounds Played: {round_count}
        ===============================
        ''')
        message_3 = 'Well played human!'
        for char in message_3:
            print(char, end='', flush=True)
            time.sleep(.1)
        time.sleep(.5)
        message_4 = '\nGoodbye!'
        for char in message_4:
            print(char, end='', flush=True)
            time.sleep(.1)
        break
    else:

        print('next round!')