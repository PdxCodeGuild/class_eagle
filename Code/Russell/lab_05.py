import random

choices = [ 'rock', 'paper', 'scissors']

while True:
    challenge = input("Would you like to play Rock Paper Scissors? y or n " )
    if challenge == 'y':
        answer = input('Choose rock, paper or scissors')
        break
    elif challenge == 'n':
        print('You suck.')
        break
    else:
        print("Type y or n!")

comp_answer = random.choice(choices)
        
if answer == comp_answer:
    print("It's a TIE!")

elif answer == 'rock' and comp_answer == 'paper':
    print( "Paper covers rock. You lose!")

elif answer == 'rock' and comp_answer == 'scissors':
    print( "Rock crushes scissors. You win!")

elif answer == 'paper' and comp_answer == 'rock':
    print("Paper covers rock. You win!")

elif answer == 'paper' and comp_answer == 'scissors':
    print( "Scissors cut paper. You lose!")  

elif answer == 'scissors' and comp_answer == 'rock':
    print("Rock crushes scissors. You lose!")

elif answer == 'scissors' and comp_answer == 'paper':
    print("Scissors cut paper. You win!")




