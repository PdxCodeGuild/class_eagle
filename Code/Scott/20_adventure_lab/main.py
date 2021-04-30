import map_gen as m
import random as r
import player as p
import locations as loc
import os

path = r'Code\Scott\20_adventure_lab\map.txt'
user_map = m.mapfile_import(path)
map_dim = [21, 22] # y, x # Max dimensions (inclusive)

# How map coords work
# [0, 0]           [0, 22]
#
#            *
#
#[21, 0]           [21, 22]     

player_inventory = [] # Ended up not using (not enough time :( )
player_pos = [] # y, x

rand_spawn_y = 0
rand_spawn_x = 0

while True: # keep generating random starting positions until we aren't on water
    rand_spawn_y = r.randint(1, map_dim[0] - 1) # rand y val
    rand_spawn_x = r.randint(1, map_dim[1] - 1) # rand x val
    if m.get_terrain_type(user_map, [rand_spawn_y, rand_spawn_x]) == '*': # if we are on water
        continue # do loop again
    else: # if we aren't on water
        break # leave loop

player_pos = [rand_spawn_y, rand_spawn_x] # assign position to the rand values

while True:
    # os.system('cls||clear')
    print('\n\n')
    view = p.print_pos(user_map, player_pos)
    m.map_print_w_player(view, [1, 1])
    p.print_terrain_on(user_map, player_pos)

    p.decision(user_map, player_pos) # Do the decision for the next turn LAST