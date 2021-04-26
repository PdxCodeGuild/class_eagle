import random
import string



print("\n***** Password Generator *****\n")

run_again = 'y'
while run_again == 'y':

    # Setting chars as upper and lowercase letters and punctuation characters
    chars = string.ascii_letters + string.digits + string.punctuation

    # request input for number of random characters
    a = int(input("How many characters do you want for your password? "))

    # Looping to add random characters to a list until input number is met
    i = 0
    password = []
    while i < a:
        password.append(random.choice(chars))
        i += 1
        # once number of characters is met, turn list into a string and print to console
        if i == a:
            print(''.join(password))
            break

    # REPL       
    run_again = input('Run again? y/n ')
else:
    print("Goodbye!")
