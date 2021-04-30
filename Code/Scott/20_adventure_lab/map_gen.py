# KEY for txt file
# 
# * = water
# c = coast
# d = desert
# m = mountain
# g = grassland
# f = forest
# r = road
# t = town
# C = castle

import re
from colorama import Fore, Back, Style, init
from termcolor import colored

def mapfile_import(path): # returns array of arrays of all spaces
    regex_blanks = r'\S+'
    map_rows = []
    map_x = []
    map_out = []

    with open(path, 'r') as f:
        map_data = f.read()

    map_data = str(map_data)
    map_rows = re.findall(regex_blanks, map_data)

    for row in map_rows:
        map_x = []
        for char in row:
            map_x.append(char)
        map_out.append(map_x)  ## map_out[y_coord][x_coord]
    return map_out

def map_print(map_in):
    init() # Inits colorama lib
    for j in range(len(map_in)):
        for i in range(len(map_in[j])):
            if map_in[j][i] == '*':
                print(colored( 'ω', 'blue', 'on_blue'), end = "")
            elif map_in[j][i] == 'c':
                print(colored( '*', 'yellow', 'on_yellow'), end = "")
            elif map_in[j][i] == 'd':
                print(colored( '^', 'white', 'on_yellow'), end = "")
            elif map_in[j][i] == 'm':
                print(colored( 'Δ', 'white', 'on_grey'), end = "")
            elif map_in[j][i] == 'g':
                print(colored( '*', 'green', 'on_green'), end = "")
            elif map_in[j][i] == 'f':
                print(colored( '⍋', 'grey', 'on_green'), end = "")
            elif map_in[j][i] == 'r':
                print(colored( '▮', 'grey', 'on_green'), end = "")
            elif map_in[j][i] == 't':
                print(colored( '⌂', 'white', 'on_green'), end = "")
            elif map_in[j][i] == 'C':
                print(colored( '⛫', 'white', 'on_green'), end = "")
        print()

def map_print_w_player(map_in, pos):
    init() # Inits colorama lib
    for j in range(len(map_in)):
        for i in range(len(map_in[j])):
            if pos[1] == i and pos[0] == j:
                print(colored('•', 'red', 'on_white'), end = "")
                continue
            if map_in[j][i] == '*':
                print(colored( 'ω', 'blue', 'on_blue'), end = "")
            elif map_in[j][i] == 'c':
                print(colored( '*', 'yellow', 'on_yellow'), end = "")
            elif map_in[j][i] == 'd':
                print(colored( '^', 'white', 'on_yellow'), end = "")
            elif map_in[j][i] == 'm':
                print(colored( 'Δ', 'white', 'on_grey'), end = "")
            elif map_in[j][i] == 'g':
                print(colored( '*', 'green', 'on_green'), end = "")
            elif map_in[j][i] == 'f':
                print(colored( '⍋', 'grey', 'on_green'), end = "")
            elif map_in[j][i] == 'r':
                print(colored( '▮', 'grey', 'on_green'), end = "")
            elif map_in[j][i] == 't':
                print(colored( '⌂', 'white', 'on_green'), end = "")
            elif map_in[j][i] == 'C':
                print(colored( '⛫', 'white', 'on_green'), end = "")
        print()

# TODO: Fix
# def blown_up_view(map_in):
#     init()

#     for j in range(len(map_in)):
#         for i in range(len(map_in[j])):
#             # if pos[1] == i and pos[0] == j:
#             #     print(colored('•', 'red', 'on_white'), end = "")
#             if map_in[j][i] == '*':
#                 print(colored( 'ωωω\n   \nωωω', 'blue', 'on_blue'), end = "")
#             elif map_in[j][i] == 'c':
#                 print(colored( '___\n___\n___', 'yellow', 'on_yellow'), end = "")
#             elif map_in[j][i] == 'd':
#                 print(colored( '___\n^^^\n___', 'white', 'on_yellow'), end = "")
#             elif map_in[j][i] == 'm':
#                 print(colored( '''^
#                                  / \
#                                 /   \
#                                      ''', 'white', 'on_grey'), end = "")
#             elif map_in[j][i] == 'g':
#                 print(colored( ' * \n  *\n   ', 'red', 'on_green'), end = "")
#             elif map_in[j][i] == 'f':
#                 print(colored( '⍋⍋⍋\n⍋⍋⍋\n⍋⍋⍋', 'grey', 'on_green'), end = "")
#             elif map_in[j][i] == 'r':
#                 print(colored( '▮▮▮\n▮▮▮\n▮▮▮', 'grey', 'on_green'), end = "")
#             elif map_in[j][i] == 't':
#                 print(colored( '⌂  ⌂\n⌂  \n  ⌂', 'white', 'on_green'), end = "")
#             elif map_in[j][i] == 'C':
#                 print(colored( '⌂⌂ \n ⛫⌂\n ⌂ ', 'white', 'on_green'), end = "")
#         print()