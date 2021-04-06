import random

rpc = ['rock','paper','scissors']

print("""    ____             __      ____                           _____      _                          
   / __ \____  _____/ /__   / __ \____ _____  ___  _____   / ___/_____(_______________  __________
  / /_/ / __ \/ ___/ //_/  / /_/ / __ `/ __ \/ _ \/ ___/   \__ \/ ___/ / ___/ ___/ __ \/ ___/ ___/
 / _, _/ /_/ / /__/ ,<    / ____/ /_/ / /_/ /  __/ /      ___/ / /__/ (__  (__  / /_/ / /  (__  ) 
/_/ |_|\____/\___/_/|_|  /_/    \__,_/ .___/\___/_/      /____/\___/_/____/____/\____/_/  /____/  
                                    /_/ 
""")


def rock_paper_scissors(user,computer): # a function to decide the winner
    if user == computer:
        return 'tie'
    elif user == "rock":
        if computer == "paper":
            return 'lose'
        elif computer == "scissors":
            return 'win'
    elif user == "scissors":
        if computer == "rock":
            return 'lose'
        elif computer == "paper":
            return 'win'
    elif user == "paper":
        if computer == "rock":
            return 'win'
        elif computer == "scissors":
            return 'lose'





while True:
    comp = random.choice(rpc) # Using random for the computers answer

    u_rpc = input('Make your choice: ')
    if u_rpc not in rpc: # ensuring the user picks a valid choice
        print('Please enter a valid choice!')
        continue
    print(f"""
    You chose {u_rpc}
    The computer chose {comp}
    """)
    result = rock_paper_scissors(u_rpc, comp) 
    if result == "win":
        print('Congratulations! You won!')
    elif result == "lose":
        print('Unfortunatly, you lost. Better luck next time!')
    else:
        print("It's a tie!")
    


    answer = input('Would you like to play again?[yes/no] ')
    if answer != 'yes':
        print('Thank you, goodbye!')
        break
        
    
