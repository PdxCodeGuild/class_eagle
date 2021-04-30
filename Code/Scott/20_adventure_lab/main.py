import map_gen as m
import random as r

path = r'Code\Scott\20_adventure_lab\map.txt'
user_map = m.mapfile_import(path)
m.map_print(user_map)
map_dim = [21, 22] # y, x

class Player:
    def __init__(self):
        self.inventory = []
        self.pos = [] # y, x

    def print_pos(self):
        output = [
            [user_map[self.pos[0]-1][self.pos[1]+1], user_map[self.pos[0]  ][self.pos[1]+1], user_map[self.pos[0]+1][self.pos[1]+1]],
            [user_map[self.pos[0]-1][self.pos[1]  ], user_map[self.pos[0]  ][self.pos[1]  ], user_map[self.pos[0]+1][self.pos[1]  ]],
            [user_map[self.pos[0]-1][self.pos[1]-1], user_map[self.pos[0]  ][self.pos[1]-1], user_map[self.pos[0]+1][self.pos[1]-1]]]
        return output

player = Player()
player.pos.append(r.randint(1, map_dim[0]-1))
player.pos.append(r.randint(1, map_dim[1]-1))
print(player.pos)
view = player.print_pos()
m.map_print_w_player(user_map, player.pos)
print()
m.map_print_w_player(view, [1, 1])
