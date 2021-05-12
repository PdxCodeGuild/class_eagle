
import random

def draw ():
    print ('''
    '  ____                      __
'     / __ \_________ __      __/ /
'    / / / / ___/ __ `/ | /| / / / 
'   / /_/ / /  / /_/ /| |/ |/ /_/  
'  /_____/_/   \__,_/ |__/|__(_)   
'                                  
''')
def win():
    print ('''



'  ___    __   _____              _____                                   
'  __ |  / /   ___(_)  _______    __  /_   ______     ________   _____  __
'  __ | / /    __  /   _  ___/    _  __/   _  __ \    __  ___/   __  / / /
'  __ |/ /     _  /    / /__      / /_     / /_/ /    _  /       _  /_/ / 
'  _____/      /_/     \___/      \__/     \____/     /_/        _\__, /  
'                                                                /____/   

''')

def loose():
    print ('''
'   ▒█████   █     █░ ▄████▄   ██░ ██  ▐██▌ 
'  ▒██▒  ██▒▓█░ █ ░█░▒██▀ ▀█  ▓██░ ██▒ ▐██▌ 
'  ▒██░  ██▒▒█░ █ ░█ ▒▓█    ▄ ▒██▀▀██░ ▐██▌ 
'  ▒██   ██░░█░ █ ░█ ▒▓▓▄ ▄██▒░▓█ ░██  ▓██▒ 
'  ░ ████▓▒░░░██▒██▓ ▒ ▓███▀ ░░▓█▒░██▓ ▒▄▄  
'  ░ ▒░▒░▒░ ░ ▓░▒ ▒  ░ ░▒ ▒  ░ ▒ ░░▒░▒ ░▀▀▒ 
'    ░ ▒ ▒░   ▒ ░ ░    ░  ▒    ▒ ░▒░ ░ ░  ░ 
'  ░ ░ ░ ▒    ░   ░  ░         ░  ░░ ░    ░ 
'      ░ ░      ░    ░ ░       ░  ░  ░ ░    
'                    ░                      
''') 
   

def title():
    print('''


'               ██▀███   ▒█████                ██████  ██░ ██  ▄▄▄       ███▄ ▄███▓             ▄▄▄▄    ▒█████                     
'              ▓██ ▒ ██▒▒██▒  ██▒            ▒██    ▒ ▓██░ ██▒▒████▄    ▓██▒▀█▀ ██▒            ▓█████▄ ▒██▒  ██▒                   
'              ▓██ ░▄█ ▒▒██░  ██▒            ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ▓██    ▓██░            ▒██▒ ▄██▒██░  ██▒                   
'              ▒██▀▀█▄  ▒██   ██░              ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ▒██    ▒██             ▒██░█▀  ▒██   ██░                   
'              ░██▓ ▒██▒░ ████▓▒░            ▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒▒██▒   ░██▒            ░▓█  ▀█▓░ ████▓▒░                   
'              ░ ▒▓ ░▒▓░░ ▒░▒░▒░             ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ░  ░            ░▒▓███▀▒░ ▒░▒░▒░                    
'                ░▒ ░ ▒░  ░ ▒ ▒░             ░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░░  ░      ░            ▒░▒   ░   ░ ▒ ▒░                    
'                ░░   ░ ░ ░ ░ ▒              ░  ░  ░   ░  ░░ ░  ░   ▒   ░      ░                ░    ░ ░ ░ ░ ▒                     
'                 ░         ░ ░                    ░   ░  ░  ░      ░  ░       ░                ░          ░ ░                     
'                                                                                                    ░                             
'   █    ██  ██▓  ▄▄▄█████▓ ██▓ ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓▓█████               █████▒██▓  ▄████  ██░ ██ ▄▄▄█████▓▓█████  ██▀███  
'   ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓█   ▀             ▓██   ▒▓██▒ ██▒ ▀█▒▓██░ ██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
'  ▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒███               ▒████ ░▒██▒▒██░▄▄▄░▒██▀▀██░▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
'  ▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄             ░▓█▒  ░░██░░▓█  ██▓░▓█ ░██ ░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
'  ▒▒█████▓ ░██████▒▒██▒ ░ ░██░▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒            ░▒█░   ░██░░▒▓███▀▒░▓█▒░██▓  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
'  ░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░             ▒ ░   ░▓   ░▒   ▒  ▒ ░░▒░▒  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
'  ░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░░  ░      ░  ▒   ▒▒ ░   ░     ░ ░  ░             ░      ▒ ░  ░   ░  ▒ ░▒░ ░    ░     ░ ░  ░  ░▒ ░ ▒░
'   ░░░ ░ ░   ░ ░   ░       ▒ ░░      ░     ░   ▒    ░         ░                ░ ░    ▒ ░░ ░   ░  ░  ░░ ░  ░         ░     ░░   ░ 
'     ░         ░  ░        ░         ░         ░  ░           ░  ░                    ░        ░  ░  ░  ░            ░  ░   ░     
'                                                                                                                                  

  ''')
  
title()
roshambo = ["paper", "rock", "scissors"]
player=input("paper rock sissors? 1 2 3 throw!")
comp = random.choice(roshambo)

if player == comp:
    draw()
else:
    if player == "paper" and  "rock" == comp:
        win()
    if player == "paper" and "scissors" == comp: 
        loose()

    if player == "rock" and "scissors" == comp:
        win()
    if player == "rock" and "paper" == comp:
        loose()

    if player == "scissors" and "paper" == comp:
        win()
    if  player == "scissors" and comp == "rock":
        loose()

 