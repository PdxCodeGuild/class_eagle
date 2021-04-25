import random
import string



print("\n***** Password Generator *****\n")

run_again = 'y'
while run_again == 'y':
    chars = string.ascii_letters + string.digits + string.punctuation
    a = int(input("How many characters do you want for your password? "))

    i = 0
    password = []
    while i < a:
        password.append(random.choice(chars))
        i += 1
        while i == a:
            print(''.join(password))
            break

    run_again = input('Run again? y/n ')
else:
    print("Goodbye!")
