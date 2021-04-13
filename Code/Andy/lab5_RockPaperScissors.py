
# Rock, Papeer, Scissors

print("Let's play Rock, Paper, Scissors!")

import random

run_again = 'yes'
while run_again == 'yes' :

    choices = ["Rock", "Paper", "Scissors"]
    for choices in choices :
        print(f"{choices}")

    user_choice = input("You choose " )
    choices = ["Rock", "Paper", "Scissors"]
    CPU_choice = random.choice(choices)

    print(f"You chose {user_choice}, I chose {CPU_choice}")

    if user_choice == CPU_choice:
        print("It's a Tie!")
    elif user_choice == "Rock":
        if CPU_choice == "Scissors":
            print("You win!")
        else:
                print("You lose!")
    elif user_choice == "Paper":
        if CPU_choice == "Rock":
            print("You win!")
        else:
                print("You lose!")
    elif user_choice == "Scissors":
        if CPU_choice == "Paper":
            print("You win!")
        else:
                print("You lose!")

    run_again = input('Would you like to play again? ')
    if run_again != 'yes':
        print('Goodbye!')
        break
