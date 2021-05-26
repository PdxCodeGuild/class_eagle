import random
choices = ['rock', 'paper', 'scissors']

def rps_game(score, c_score):
    if score == c_score:
        result = "It's a TIE!"

    elif score == 'rock' and c_score == 'paper':
        result = "Paper covers rock. You lose!"
    elif score == 'rock' and c_score == 'scissors':
        result = "Rock crushes scissors. You win!"
    elif score == 'paper' and c_score == 'rock':
        result = "Paper covers rock. You win!"
    elif score == 'paper' and c_score == 'scissors':
        result = "Scissors cut paper. You lose!"  
    elif score == 'scissors' and c_score == 'rock':
        result = "Rock crushes scissors. You lose!"
    elif score == 'scissors' and c_score == 'paper':
        result = "Scissors cut paper. You win!"
    return result


while True:
    person_choice = input("Choose rock, paper, or scissors: ")

    comp_choice = random.choice(choices)

    x = rps_game(person_choice, comp_choice)
    print(x)

    again = input("Would you like to play again? y or n " )

if again == 'y':
elif again == 'n':
    print("seeya!")
    break




