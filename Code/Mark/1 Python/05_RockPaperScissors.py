import random

# Some amazing ascii art to add some flavor!
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

# a function with lots of if's and elif's to determine the winner


def rock_paper_scissors(user, computer):
    if user == computer:
        return 'tie'
    elif user == "rock":
        if computer == "paper":
            return 'lose'
        elif computer == "scissors":
            return 'win'
        elif computer == "spock":
            return 'lose'
        elif computer == "lizard":
            return 'win'
    elif user == "scissors":
        if computer == "rock":
            return 'lose'
        elif computer == "paper":
            return 'win'
        elif computer == "spock":
            return 'lose'
        elif computer == "lizard":
            return 'win'
    elif user == "paper":
        if computer == "rock":
            return 'win'
        elif computer == "scissors":
            return 'lose'
        elif computer == "spock":
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


# The list the will be randomly chosen from by the comp
rpc = ['rock', 'paper', 'scissors', 'lizard', 'spock']

# setting the variables to increment the score
comp_score = 0
user_score = 0

while True:

    # comp choses its fighter
    comp = random.choice(rpc)

    # user choses its fighter
    u_rpc = input('Make your choice: ')

    # ensuring that the user chose a valid option
    if u_rpc not in rpc:
        print('Please enter a valid choice!')
        continue

    # displaying what the user and the computer chose
    print(f"""
    You chose {u_rpc}
    The computer chose {comp}
    """)

    # determining the winner with the function
    result = rock_paper_scissors(u_rpc, comp)

    # ifs and elifs to display the results and incriment the score
    if result == "win":
        user_score += 1
        print('Congratulations! You won!')
    elif result == "lose":
        comp_score += 1
        print('Unfortunatly, you lost. Better luck next time!')
    else:
        print("It's a tie!")

    # displaying the current score
    print(f"""
    Current score:
    User  {user_score}
    Computer {comp_score}
    """)

    # asking the user if they would like to play again
    answer = input('Would you like to play again?[yes/no] ')
    if answer != 'yes':
        print('Thank you, goodbye!')
        break
