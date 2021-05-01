import map_gen as m
import locations as loc

def print_terrain_on(in_map, pos): # Get the terrain we're on and output a string describing it
    ter_type = m.get_terrain_type(in_map, pos) # get type key from map_gen module
    if ter_type == '*':
        print('') # Should be impossible
    elif ter_type == 'c':
        print('You\'re on the coast')
    elif ter_type == 'd':
        print('You\'re in the desert')
    elif ter_type == 'm':
        print('You\'re in the mountains')
    elif ter_type == 'g':
        print('You\'re in the grassland')
    elif ter_type == 'f':
        print('You\'re in the forest')
    elif ter_type == 't':
        print('You have entered a town')
    elif ter_type == 'C':
        print('You have come across a castle')

def view_map(in_map): # Just runs map_print from the map_gen module
    print('\n====================\n')
    m.map_print(in_map)
    print('\n====================\n')

    # The following four move_{n/s/e/w}(): functions all function the same
    # don't move that direction if there's water (natural boundary)
    # and leave the function
    # if there is no water, move the player that direction,
    # then leave the function

def move_n(in_map, pos):
    if m.get_terrain_type(in_map, [pos[0] - 1, pos[1]]) == '*':
        print("You can't go that way you don't know how to swim!")
        return
    else:
        pos[0] -= 1
        return pos
    
def move_s(in_map, pos):
    if m.get_terrain_type(in_map, [pos[0] + 1, pos[1]]) == '*':
        print("You can't go that way you don't know how to swim!")
        return
    else:
        pos[0] += 1
        return pos
    
def move_e(in_map, pos):
    if m.get_terrain_type(in_map, [pos[0], pos[1] + 1]) == '*':
        print("You can't go that way you don't know how to swim!")
        return
    else:
        pos[1] += 1
        return pos

def move_w(in_map, pos):
    if m.get_terrain_type(in_map, [pos[0], pos[1] - 1]) == '*':
        print("You can't go that way you don't know how to swim!")
        return
    else:
        pos[1] -= 1
        return pos

def print_pos(in_map, pos): # Prints the players location and the positions all around the player for a limited view
    output = [
        [in_map[pos[0]-1][pos[1]-1], in_map[pos[0]-1][pos[1]  ], in_map[pos[0]-1][pos[1]+1]],
        [in_map[pos[0]  ][pos[1]-1], in_map[pos[0]  ][pos[1]  ], in_map[pos[0]  ][pos[1]+1]],
        [in_map[pos[0]+1][pos[1]-1], in_map[pos[0]+1][pos[1]  ], in_map[pos[0]+1][pos[1]+1]]]
    return output

def decision(in_map, pos): # Place decision repl inside function
    while True: # All on seperate print statements so it's easy to add onto later
        print('What would you like to do?')
        print('1 to view your map')
        if m.get_terrain_type(in_map, pos) == 't':
            print('2 to enter the town menu')
        print('n/s/e/w to move in that direction')
        user_input = input() 
        user_input = str(user_input)
        user_input.lower()
        # Each condition just calls a function from within the Player class
        if user_input == '1':
            view_map(in_map)
            break
        elif user_input == '2' and m.get_terrain_type(in_map, pos) == 't':
            loc.town_menu()
            break
        elif user_input == 'n':
            move_n(in_map, pos)
            break
        elif user_input == 's':
            move_s(in_map, pos)
            break
        elif user_input == 'e':
            move_e(in_map, pos)
            break
        elif user_input == 'w':
            move_w(in_map, pos)
            break
        else:
            print('Invalid input')
            m.map_print_w_player(print_pos(in_map, pos), [1, 1])
            continue
