
# Rock, Papeer, Scissors

print("Let's play Rock, Paper, Scissors!")

import random

run_again = 'yes'
while run_again == 'yes' :

    # Displaying to user the possible choices
    choices = ["Rock", "Paper", "Scissors"]
    for choices in choices :
        print(f"{choices}")

    # Asking user to choose 
    user_choice = input("You choose " )
    choices = ["Rock", "Paper", "Scissors"]
    cpu_choice = random.choice(choices)

    # Displaying user and computer choices
    print(f"You chose {user_choice}, I chose {cpu_choice}")

    # Win conditions depending on input from user and random cpu choice
    if user_choice == cpu_choice:
        print("It's a Tie!")
    elif user_choice == "Rock":
        if cpu_choice == "Scissors":
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == "Paper":
        if cpu_choice == "Rock":
            print("You win!")
        else:
                print("You lose!")
    elif user_choice == "Scissors":
        if cpu_choice == "Paper":
            print("You win!")
        else:
            print("You lose!")

    # REPL
    run_again = input('Would you like to play again? yes/no ')
    if run_again != 'yes':
        print('Goodbye!')
        