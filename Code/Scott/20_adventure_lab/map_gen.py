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

import re # For Regex
from colorama import Fore, Back, Style, init # Colorama
from termcolor import colored # Uses colorama to convert into just strings I can write

def mapfile_import(path): # returns array of arrays of all spaces from file
    regex_blanks = r'\S+' # For line breaks and spaces
    map_rows = []
    map_x = []
    map_out = []

    with open(path, 'r') as f: # Open the file...
        map_data = f.read() # ...Read it and save it to a variable...
                            # ...Close the file (Closes because of with keyword)

    map_data = str(map_data) # convert to string
    map_rows = re.findall(regex_blanks, map_data) # Remove the line breaks and spaces

    for row in map_rows: # For every row
        map_x = [] # Reset what's in the row
        for char in row: # For every character in that row
            map_x.append(char) # add that characther to the list of the row
        map_out.append(map_x)  # add the lists of rows into one larger list ## map_out[y_coord][x_coord]
    return map_out 

def map_print(map_in): # prints the given list of lists into a map
    init() # Inits colorama lib
    for j in range(len(map_in)): # For every row 
        for i in range(len(map_in[j])): # For every index in specified row
            if map_in[j][i] == '*':  # for water
                print(colored( 'ω', 'blue', 'on_blue'), end = "") 
            elif map_in[j][i] == 'c': # for coasts
                print(colored( '*', 'yellow', 'on_yellow'), end = "")
            elif map_in[j][i] == 'd': # for deserts
                print(colored( '^', 'white', 'on_yellow'), end = "")
            elif map_in[j][i] == 'm': # for mountains
                print(colored( 'Δ', 'white', 'on_grey'), end = "")
            elif map_in[j][i] == 'g': # for grasslands
                print(colored( '*', 'green', 'on_green'), end = "")
            elif map_in[j][i] == 'f': # for forests
                print(colored( '⍋', 'grey', 'on_green'), end = "")
            elif map_in[j][i] == 't': # for towns
                print(colored( '⌂', 'white', 'on_green'), end = "")
            elif map_in[j][i] == 'C': # For castles
                print(colored( '⛫', 'white', 'on_green'), end = "")
        print()

def map_print_w_player(map_in, pos): # prints the given list of lists into a map, with a marker at a given position
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
            
            if map_in[j][i] == 't':
                print(colored( '⌂', 'white', 'on_green'), end = "")
            elif map_in[j][i] == 'C':
                print(colored( '⛫', 'white', 'on_green'), end = "")
        print()

def get_terrain_type(map_in, pos): # Returns terrain type at given position on given map
    return str(map_in[pos[0]][pos[1]])

def get_towns(map_in):
    output = []
    for j in range(len(map_in)):
        for i in range(len(map_in[j])):
            if map_in[j][i] == 't':
                output.append([j, i])
    return output