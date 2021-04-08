# Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost. If the user guesses the number, the user is told they've won and the game exits. You can get a random number using random.randint:
import random

# V1
# generate random number between a,b
# secret_num = random.randint(1,5)

# guess_count = 0

# # game loop
# while guess_count < 10:
#   print(guess_count)

#   # prompt user for number guess
#   guess = int(input('Guess a Number: '))

#   # win condition
#   if(secret_num == guess):
#     print('WIN')
#     print(f'You guess it in {guess_count + 1} tries!! CONGRATZ')
#     break
#   else:
#     # increment guess count every iteration
#     guess_count += 1
#     print(f'Wrong number! {10 - guess_count} guesses remaining')


# if(guess_count == 10):
#   print('FAIL')
# Do you want to play again


# Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost. If the user guesses the number, the user is told they've won and the game exits. You can get a random number using random.randint:

# Tell the user whether their current guess is closer than their last. This can be done by maintaining a variable containing the last guess outside the loop, then comparing the last guess to the current guess, and check if it's closer. Hint: you're interested in comparing the two absolute differences: abs(current_guess-target) and abs(last_guess-target).

# PART 3-4
# import random

# # generate random number between a,b
# secret_num = random.randint(1,100)

# guess_count = 0
# game_loop = True
# last_guess = ''
# guess = ''

# # game loop
# while game_loop:

#   # prompt user for number guess
#   guess = input('Guess a Number or type "done" to quit: ')

#   if(guess == "done"):
#     print(f"Goodbye. You guessed {guess_count} many times")
#     game_loop = False
#     break

#   # increment guess count every iteration
#   guess_count += 1
#   guess = int(guess)

#   # win condition
#   if(secret_num == guess):
#     print('WIN')
#     print(f'You guessed it in {guess_count} tries!! CONGRATZ')
#     break
#   else:
#     if(guess > 2):
#       if(abs(last_guess-secret_num) > abs(guess-secret_num)):
#         print(f"You're getting Warmer!")
#       elif(abs(last_guess-secret_num) == abs(guess-secret_num)):
#         print("You are no Closer and Further than last time.")
#       else:
#         print("You're getting Colder!")
#     print(f"Wrong number! You've guessed {guess_count} many times!")

#     if(guess < secret_num):
#       print('Your guess is to Low!')
#     else:
#       print('Your guess is to High')

#   last_guess = guess


# PART 5
import random

# generate random number between a,b

guess_count = 0
game_loop = True
last_guess = 0
guess = ''
# prompt user for number guess
secret_num = int(input('Pick a Secret Number (1-5): '))

# game loop
while game_loop:
    print()
    guess = random.randint(1, 5)
    print(f'Computer Guessed: {guess}')
    # increment guess count every iteration
    guess_count += 1

    # win condition
    if(secret_num == guess):
        print('WIN')
        print(f'You guessed it in {guess_count} tries!! CONGRATZ')
        break
    else:
        if(last_guess):
            if(abs(last_guess-secret_num) > abs(guess-secret_num)):
                print(f"You're getting Warmer!")
            elif(abs(last_guess-secret_num) == abs(guess-secret_num)):
                print("You are no Closer and Further than last time.")
            else:
                print("You're getting Colder!")
        print(f"Wrong number! You've guessed {guess_count} many times!")

        if(guess < secret_num):
            print('Your guess is to Low!')
        else:
            print('Your guess is to High')

    last_guess = guess
