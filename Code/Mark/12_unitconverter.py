import os
import time
from colorama import Fore, Back, Style

# sweet ascii art!
print(Fore.YELLOW + Back.BLUE + '''

            _____ _   _______ ___________              
           /  ___| | | | ___ \  ___| ___ \             
           \ `--.| | | | |_/ / |__ | |_/ /             
            `--. \ | | |  __/|  __||    /              
           /\__/ / |_| | |   | |___| |\ \              
           \____/ \___/\_|   \____/\_| \_|             
                                                       
                                                       
               _   _ _   _ _____ _____                 
              | | | | \ | |_   _|_   _|                
              | | | |  \| | | |   | |                  
              | | | | . ` | | |   | |                  
              | |_| | |\  |_| |_  | |                  
               \___/\_| \_/\___/  \_/                  
                                                       
                                                       
 _____ _____ _   _ _   _ ___________ _____ ___________ 
/  __ \  _  | \ | | | | |  ___| ___ \_   _|  ___| ___ \\
| /  \/ | | |  \| | | | | |__ | |_/ / | | | |__ | |_/ /
| |   | | | | . ` | | | |  __||    /  | | |  __||    / 
| \__/\ \_/ / |\  \ \_/ / |___| |\ \  | | | |___| |\ \ 
 \____/\___/\_| \_/\___/\____/\_| \_| \_/ \____/\_| \_|
                                                       
''')
print(Style.RESET_ALL)

# get_distance takes the information provided by the user and converts to the requested unit
def get_distance(unit1, distance, unit2):
    # dictionary with the unit conversions 
    unit_values = {
    "ft": 0.3048,
    "m": 1,
    "mi": 1609.34,
    "NM": 1852,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254,
    "cm": 0.01,
    "mm": 0.001
    }
    # converting original unit to meters
    meters = distance*unit_values[unit1]
    # using the previous result to convert to our new unit
    output = meters/unit_values[unit2]
    return output


while True:
    # asking what unit the user is converting from
    unit1 = input('Which unit would you like to convert from: ')
    # asking the distance for the previous unit
    distance = float(input(f'What is the distance in {unit1}: '))
    # asking for the unit the user would like to convert too
    unit2 = input('Which unit would you like to convert to: ')

    # clearing the screen of the previous information
    os.system('cls')
    # adding time and statment for a little suspense
    print('Beep boop beep...converting units')
    time.sleep(6)
    # clearing the screen for proper presentation
    os.system('cls')

    # present the results to the user
    print('\n')
    print(Fore.YELLOW+Back.BLUE+f'{distance} {unit1} is {get_distance(unit1,distance,unit2)} {unit2}')
    print(Style.RESET_ALL+'\n')

    # asking if they would like to conver another unit
    answer = input('Would you like to convert another unit? ')
    if answer != 'yes':
        break

# Saying goodbye with some awesome ascii art!
print(Fore.YELLOW+Back.BLUE+'''
                Thank you for using the:               
            _____ _   _______ ___________              
           /  ___| | | | ___ \  ___| ___ \             
           \ `--.| | | | |_/ / |__ | |_/ /             
            `--. \ | | |  __/|  __||    /              
           /\__/ / |_| | |   | |___| |\ \              
           \____/ \___/\_|   \____/\_| \_|             
                                                       
                                                       
               _   _ _   _ _____ _____                 
              | | | | \ | |_   _|_   _|                
              | | | |  \| | | |   | |                  
              | | | | . ` | | |   | |                  
              | |_| | |\  |_| |_  | |                  
               \___/\_| \_/\___/  \_/                  
                                                       
                                                       
 _____ _____ _   _ _   _ ___________ _____ ___________ 
/  __ \  _  | \ | | | | |  ___| ___ \_   _|  ___| ___ \\
| /  \/ | | |  \| | | | | |__ | |_/ / | | | |__ | |_/ /
| |   | | | | . ` | | | |  __||    /  | | |  __||    / 
| \__/\ \_/ / |\  \ \_/ / |___| |\ \  | | | |___| |\ \ 
 \____/\___/\_| \_/\___/\____/\_| \_| \_/ \____/\_| \_|
                                                       
                    Goodbye!                           
''')
print(Style.RESET_ALL)