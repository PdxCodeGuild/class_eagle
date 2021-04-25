from random import *
import string

 # Somme more awesome ascii art!
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

# Used a function to do the password generation once values are provided

def pass_gen(upper,lower,num,special):
    password = []
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
    
# using a while loop for REPL
while True:

    upper = int(input('How many upper case letters? '))
    lower = int(input('How many lower case letters? '))
    num = int(input('How many numbers would you like? '))
    special = int(input('How many special characters? '))

    # Used to ensure the selected character values matches the requested length

    
    print(f'You shiny new password is: {pass_gen(upper,lower,num,special)}')

    # asks the user if they would like to generate another

    answer = input("""
Would you like to generate another?
[yes/no] 
""")
    if answer != 'yes':
        print('''
Thank you for using the Password Generator 9000!
Goodbye!
        ''')
        break
        



