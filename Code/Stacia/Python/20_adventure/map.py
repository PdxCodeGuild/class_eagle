
player_location =(y,x);

def map_initializer(width, height):


    board = []
    for y in range (height):
        board.append([])
        for x in range(width):
            board[y].append("_")
    return board


def show_map (board, player_y, player_x):
    print(board)
    for y in range (len(board)):
        for x in range (len(board[y])):
            if y == player_y and x == player_x:
                print ('X', end = " ")
            else:
                print (board[y][x], end = " ")
        print ()
    return board




map_i = map_initializer(10,10)
map = show_map(map_i, 3,5)
print (map)




















# out_of_bounds = [error_1, error_2, error_3, error_4]

# east ={
#     error_1: "The forrest to the west is impenitrably thick, legends say it is full of beasts and maddness",
#     error_2: "The forrest is silent and you find your breath matching the langour of the humid breaze",
#     error_3: "You've atunned with the thrum of the forrest its endlessness stretches before you with fearal clarity",
#     error_4: "the last of your thoughts fade as it is replaced with a hunger for the scent of your prey"}

# north ={
#     error_1 :"The air grows thin and your view is obscured by a thick haze",
#     error_2 : "You feel light and gidy skipping from stone to stone trusting that with each leap a new stone will be beneath your feet when it is time to land",
#     error_3 : " Memories of the tales of the faye wild envelope you",
#     errror_4 : " Somehow your different, somehow your a new your free of your corpereal form, you are a endless twisting mist whispered on a breeze spanning the collective imagination of The Dreamers."}
    

# west ={
#     error_1: "You trace your hands across the smooth etchings in an onyx wall that spans endlessly before and behind you.",
#     error_2: "The Keepers who guard the wall are.",
#     error_3: "Well you could always try and climb the Wall....",
#     error_3: "You find hold in the slight indentations of the etchings, which warm with your touch, your body feals heavy as your slowly engulfed in the wall."}

# south ={
#     error_1: "The Southern Sea spans endlessly into the horizon before you.",
#     error_2: "The fisher folk starre at you unblinkingly as a hag stares into the sun moaning",
#     error_3: "The sun sets as you stare into the ocean the tide rises",
#     error_4: "The Tide tucks in you into an endless sleep as your eyes are affixed to the black horrizion."}
# }


# def bounds_check ():
#     if x > 10:
#         player=out_ofbounds(east)
#     if y > 10:
#         player=out_ofbounds(north)
#     if x > 0:
#         player=out_ofbounds(west)
#     if y > 0:
#         player=out_ofbounds(south)

# def out_of_bounds(direction)
#     while player move = direction:
#         error = +1
#         error_message = "direction"[out_of_bounds[error]]
#         print error_message
#     if error = 4:
#         player == dead
#         return player

# def player_movement (location, direction)
#     location = location
#     if direction = north:
#         y += 1
#     if direction = south:
#         y -= 1
#     if direction = east:
#         x += 1
#     if direction = west:
#         x -= 1

# def player turn (location):
#     bounds_check(location):
#     # describe location
#     direction = input("venture forth?")

    


    
#     random_encounter(rand)

# def korgoth_movement ():
# def bandit_movement ():
# def merchant_movement ():




# korgoth_location = 
# bandit_location =
# merchent_location = 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Hard_coded_locations

# forrest_entry


# unicorn_glen



# caos_space
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# if location not in [Hard_coded_locations]







# def movement(): 

# while player !/ dead
#     turn += 1
    # if player = hold
    #     if player == rest:
            
    #     if player == captive:
    
    # if player !/ hold:
    #     player_turn()

    # if turn %% 10 == 0:
    # Korgoth_movement()

    # if turn %% 5 == 0
    # bandit_movement()
    
    # if turn %%30 == 0
    # merchent_movement()

    