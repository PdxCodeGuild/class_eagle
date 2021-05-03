width = 10  # the width of the board
height = 10  # the height of the board

player_i= 5
player_j =5
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
for j in range(width):  # loop over the columns
    board[i].append(' ')  # append an empty space to the board
print (board)

for i in range(height):
    for j in range(width):
        # if we're at the player location, print the player icon
        if i == player_i and j == player_j:
            print('☺', end=' ')
        else:
            print(board[i][j], end=' ')  # otherwise print the board square
    print()
