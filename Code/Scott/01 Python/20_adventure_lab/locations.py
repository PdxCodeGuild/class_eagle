import map_gen as m
import os

def town_menu():
    while True:
        print('''
                =======================
                    WELCOME   TO
                    THE TOWN!!
                
                   1: Talk to a villager
                   2: Leave town
                 =======================''')
        user_input = input()
        if user_input == '1':
            print('Hey Stranger! What are you doing here in our quant village? ')
        elif user_input == '2':
            break
        else:
            print('Invalid Input')
            continue
