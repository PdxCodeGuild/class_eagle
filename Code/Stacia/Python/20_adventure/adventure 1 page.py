

# info to be pulled from
import random
height = 10
width = 10
# out of bounds warnings
s_error = 0
n_error = 0
e_error = 0
w_error = 0

east_bound = {
    0: "The forrest to the west is impenitrably thick, legends say it is full of beasts and maddness",
    1: "The forrest is silent and you find your breath matching the langour of the humid breaze",
    2: "You've atunned with the thrum of the forrest its endlessness stretches before you with fearal clarity",
    3: "the last of your thoughts fade as it is replaced with a hunger for the scent of your prey"}

north_bounds = {
    0: "The air grows thin and your view is obscured by a thick haze",
    1: "You feel light and gidy skipping from stone to stone trusting that with each leap a new stone will be beneath your feet when it is time to land",
    2: " Memories of the tales of the faye wild envelope you",
    3: " Somehow your different, somehow your a new your free of your corpereal form, you are a endless twisting mist whispered on a breeze spanning the collective imagination of The Dreamers."}


west_bounds = {
    0: "You trace your hands across the smooth etchings in an onyx wall that spans endlessly before and behind you.",
    1: "The Keepers who guard the wall work tirelessly etching.",
    2: "Well you could always try and climb the Wall....",
    3: "You find hold in the slight indentations of the etchings, which warm and glow with your touch, your body feals heavy as your slowly engulfed in the wall."}

south_bounds = {

    0: "The Southern Sea spans endlessly into the horizon before you.",
    1: "The fisher folk starre at you unblinkingly as a hag stares into the sun moaning",
    2: "The sun sets as you stare into the ocean the tide rises",
    3: "The Tide tucks in you into an endless sleep as your eyes are affixed to the black horrizion."}


mon1_x= random.randint(1, 10)
mon1_y = random.randint(1, 10)
frostmonsters =[]
location={
    x = 0;
    y = 0;
}

# intialize map
# player moves
# check for sister.
# import string
player_x = 3
player_y = 3
direction = "start"


game = "on"

chill=0

board = []
for y in range(height):
    board.append([])
    for x in range(width):
        board[y].append("_")
for i in range(4):
    mon_x = random.randint(0, height - 1)
    mon_y = random.randint(0, width - 1)
    board[mon_y][mon_x] = "^"

sis_x=random.randint(0,height -1)
sis_y=random.randint(0,height -1)
board[sis_y][sis_x] = "S"

frosttimer= random.randint(1,5)
fc= 0
print("Its been a bitter winter. Your sister Yurriel has wandered into the woods in search of fire woods. Your parents have always told you to never enter the woods, but they haven't been home in days.")
while game != "over":
    fc+=1
    if fc == frosttimer:
        mon_x = random.randint(0, height - 1)
        mon_y = random.randint(0, width - 1)
        board[mon_y][mon_x] = "^"
        fc = 0
    for y in range(len(board)):
        for x in range(len(board[y])):
            if y == player_y and x == player_x:
                print('X', end=" ")
            else:
                print(board[y][x], end=" ")
        print()

    
    direction = input("where would you like to go? or type done to give up")
    

    if direction == "south":
        player_y += 1

        if player_y > 10:

            print(south_bounds[s_error])
            s_error += 1
            player_y = 10
        if s_error == 4:
            game = over

    if direction == "north":
        player_y -= 1

        if player_y < 0:
            player_y = 0
            print(north_bounds[n_error])
            n_error += 1
            if n_error == 4:
                game = "over"
                player_y = 0

    if direction == "east":
        player_x += 1
        if player_x > 10:
            player_x = 10
            print(east_bounds[e_error])
            e_error += 1
            if e_error > 4:
                game = "over"

    if direction == "west":
        player_x -= 1
        if player_x < 0:
            print(west_bounds[w_error])
    # ******************************player location test********************
    # print (player_x)
    # print (player_y)
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # if monster

    if mon_x == player_x and mon_y == player_y:
        print("the seeping frost chills you to your bones")
        chill +=1
        if chill ==3:
            print("its so cold, maybe Yureil went home, she'll wake you any moment with the scent of a warm stew, just close your eyes for a little and rest")
            game == "over"
    if int(sis_x) == int(player_x) and int(sis_y) == int(player_y):
        print("You found her, now lets hope you can find home together")
        game = "over"
    if direction == "done":
        game == "over"