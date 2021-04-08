import random
import string



print("***** Password Generator *****")

run_again = 'y'
while run_again == 'y':
    chars = string.ascii_letters + string.digits + string.punctuation

    a = int(input("How many characters do you want for your password? "))

    i = 1

    while i <= a:
        password = random.choice(chars)
        print(password)
        i += 1
    run_again = input('Run again? y/n ')
else:
    print("Goodbye!")

