

# Lab 6: Random Password Generator

import random
import string

# use these
# string.ascii_uppercase
# string.ascii_lowercase
# string.digits
# string.punctuation

# Part 1 - Use a while loop to generate a random password, the length of which 
# is chosen by the user.


password = ''
char_pool = list(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
# print(char_pool)

# Promt user to input passward length
pw_length = int(input('\nHow many characters would you like in your password? '))

# using a while loop to generate a password of the chosen length
i = 0
while i < pw_length:
    password += random.choice(char_pool)
    i += 1

print(f'\n{password}\n')




# Part 2 - Ask user for the number of each character type
# n_uppercase = int(input('How many upppercase letters would you like? '))
# n_lowercase = int(input('How many lowercase letters would you like? '))
# n_digits = int(input('How many digits would you like? '))
# n_punctuation = int(input('How much punctuation would you like? '))
# pw_length = n_uppercase + n_lowercase + n_digits + n_punctuation

# using a while loop to generate a password of the chosen length

# i = 0

# while i < pw_length:
#     ...


# for testing
# print(n_uppercase)
# print(n_lowercase)
# print(n_digits)
# print(n_punctuation)
# print(pw_length)
# print(type(n_uppercase))
# print(type(pw_length))



