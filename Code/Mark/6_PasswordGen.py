from random import *
import string

print("""
         _ (`-.   ('-.     .-')    .-')    (`\ .-') /`           _  .-') _ .-') _                      ('-.      .-') _  ('-. _  .-')    ('-.    .-') _              _  .-')   
  ( (OO  ) ( OO ).-.( OO ). ( OO ).   `.( OO ),'          ( \( -O ( (  OO) )                   _(  OO)    ( OO ) _(  OO( \( -O )  ( OO ).-(  OO) )            ( \( -O )  
 _.`     \ / . --. (_)---\_(_)---\_,--./  .--.  .-'),-----.,------.\     .'_         ,----.   (,------,--./ ,--,(,------,------.  / . --. /     '._ .-'),-----.,------.  
(__...--'' | \-.  \/    _ |/    _ ||      |  | ( OO'  .-.  |   /`. ,`'--..._)       '  .-./-') |  .---|   \ |  |\|  .---|   /`. ' | \-.  \|'--...__( OO'  .-.  |   /`. ' 
 |  /  | .-'-'  |  \  :` `.\  :` `.|  |   |  |,/   |  | |  |  /  | |  |  \  '       |  |_( O- )|  |   |    \|  | |  |   |  /  | .-'-'  |  '--.  .--/   |  | |  |  /  | | 
 |  |_.' |\| |_.'  |'..`''.)'..`''.|  |.'.|  |_\_) |  |\|  |  |_.' |  |   ' |       |  | .--, (|  '--.|  .     |(|  '--.|  |_.' |\| |_.'  |  |  |  \_) |  |\|  |  |_.' | 
 |  .___.' |  .-.  .-._)   .-._)   |         |   \ |  | |  |  .  '.|  |   / :      (|  | '. (_/|  .--'|  |\    | |  .--'|  .  '.' |  .-.  |  |  |    \ |  | |  |  .  '.' 
 |  |      |  | |  \       \       |   ,'.   |    `'  '-'  |  |\  \|  '--'  /       |  '--'  | |  `---|  | \   | |  `---|  |\  \  |  | |  |  |  |     `'  '-'  |  |\  \  
 `--'      `--' `--'`-----' `-----''--'   '--'      `-----'`--.----.---.----.   .----.---.----.`------`--'  `--' `------`--' '--' `--' `--'  `--'       `-----'`--' '--' 
                                                             /  ,.  \ /  ..  \ /  ..  \ /  ..  \                                                                         
                                                            |  |  \  .  /  \  .  /  \  .  /  \  .                                                                        
                                                             '  `-'  |  |  '  |  |  '  |  |  '  |                                                                        
                                                              `- /  ''  \  /  '  \  /  '  \  /  '                                                                        
                                                               ,'  /  \  `'  / \  `'  / \  `'  /                                                                         
                                                              `---'    `---''   `---''   `---''              

""")



def pass_gen(length,upper,lower,num,special):
    password = []
    while len(password) != length:
        for x in range(upper):
            password.append(choice(string.ascii_uppercase))
        for y in range(lower):
            password.append(choice(string.ascii_lowercase))
        for z in range(num):
            password.append(choice(string.digits))
        for i in range(special):
            password.append(choice(string.punctuation))
    shuffle(password)
    password = "".join(password)
    return password
    

while True:

    length = int(input("How long would you like your password? "))
    upper = int(input('How many upper case letters? '))
    lower = int(input('How many lower case letters? '))
    num = int(input('How many numbers would you like? '))
    special = int(input('How many special characters? '))

    if (upper+lower+num+special) > length:
        print('The amount of characters you chose exceeds the requested length! Please reenter your information!')
        continue
    password = pass_gen(length,upper,lower,num,special)

    print(f'You shiny new password is: {password}')

    answer = input("""
Would you like to generate another?
[yes/no] """)
    if answer != 'yes':
        print('''
    Thank you for using the Password Generator 9000!
        Goodbye!
        ''')
        break
        



