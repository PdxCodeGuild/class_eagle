import random

rpc = ['rock','paper','scissors','lizard','spock']

print("""                             
    ____             __      ____                           _____      _                          
   / __ \____  _____/ /__   / __ \____ _____  ___  _____   / ___/_____(_______________  __________
  / /_/ / __ \/ ___/ //_/  / /_/ / __ `/ __ \/ _ \/ ___/   \__ \/ ___/ / ___/ ___/ __ \/ ___/ ___/
 / _, _/ /_/ / /__/ ,<    / ____/ /_/ / /_/ /  __/ /      ___/ / /__/ (__  (__  / /_/ / /  (__  ) 
/_/ |_|\____/\___/_/|__  /__    \__,_/ .___/\___/__   ________/\___/_/____/____/\____/_/  /____/  
                    / /   (_____ _______________/ /  / ___/____  ____  _____/ /__                 
                   / /   / /_  // __ `/ ___/ __  /   \__ \/ __ \/ __ \/ ___/ //_/                 
                  / /___/ / / // /_/ / /  / /_/ /   ___/ / /_/ / /_/ / /__/ ,<                    
                 /_____/_/ /___\__,_/_/   \__,_/   /____/ .___/\____/\___/_/|_|                   
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
        elif computer =="spock":
            return 'lose'
        elif computer == "lizard":
            return 'win'
    elif user == "scissors":
        if computer == "rock":
            return 'lose'
        elif computer == "paper":
            return 'win'
        elif computer =="spock":
            return 'lose'
        elif computer == "lizard":
            return 'win'
    elif user == "paper":
        if computer == "rock":
            return 'win'
        elif computer == "scissors":
            return 'lose'
        elif computer =="spock":
            return 'win'
        elif computer == "lizard":
            return 'lose'
    elif user == "spock":
        if computer == "rock":
            return 'win'
        elif computer == "scissors":
            return 'win'
        elif computer == "paper":
            return 'lose'
        elif computer == "lizard":
            return 'lose'
    elif user == 'lizard':
        if computer == "rock":
            return 'lose'
        elif computer == "scissors":
            return 'lose'
        elif computer == "paper":
            return 'win'
        elif computer == "spock":
            return 'win'

comp_score = 0
user_score = 0



while True:
    comp = random.choice(rpc) 

    u_rpc = input('Make your choice: ')
    if u_rpc not in rpc: 
        print('Please enter a valid choice!')
        continue
    print(f"""
    You chose {u_rpc}
    The computer chose {comp}
    """)
    result = rock_paper_scissors(u_rpc, comp) 
    if result == "win":
        user_score += 1
        print('Congratulations! You won!')
    elif result == "lose":
        comp_score += 1
        print('Unfortunatly, you lost. Better luck next time!')
    else:
        print("It's a tie!")
    
    print(f"""
    Current score:
    User  {user_score}
    Computer {comp_score}
    """)

    answer = input('Would you like to play again?[yes/no] ')
    if answer != 'yes':
        print('Thank you, goodbye!')
        break
        
    
