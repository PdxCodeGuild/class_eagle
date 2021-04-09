

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




# # Part 2 - Ask user for the number of each character type




# password = []

# def random_uppercase_chars(n_uppercase):
#     uppercase_chars = ''
#     i = 0
#     while i < n_uppercase:
#         uppercase_chars += random.choice(string.ascii_uppercase)
#         i += 1
#     return uppercase_chars

# def random_lowercase_chars(n_lowercase):
#     lowercase_chars = ''
#     i = 0
#     while i < n_lowercase:
#         lowercase_chars += random.choice(string.ascii_lowercase)
#         i += 1
#     return lowercase_chars

# def random_digits(n_digits):
#     digits = ''
#     i = 0
#     while i < n_digits:
#         digits += random.choice(string.digits)
#         i += 1
#     return digits

# def random_punctuation(n_punctuation):
#     punctuation = ''
#     i = 0
#     while i < n_punctuation:
#         punctuation += random.choice(string.punctuation)
#         i += 1
#     return punctuation

# n_uppercase = int(input('How many upppercase letters would you like? '))
# n_lowercase = int(input('How many lowercase letters would you like? '))
# n_digits = int(input('How many digits would you like? '))
# n_punctuation = int(input('How much punctuation would you like? '))
# # pw_length = n_uppercase + n_lowercase + n_digits + n_punctuation

# uppercase_chars = random_uppercase_chars(n_uppercase)
# lowercase_chars = random_lowercase_chars(n_lowercase)
# digits = random_digits(n_digits)
# punctuation = random_punctuation(n_punctuation)


# password.append(uppercase_chars)
# password.append(lowercase_chars)
# password.append(digits)
# password.append(punctuation)

# print(password)


# for testing
# print(uppercase_chars)
# print(lowercase_chars)
# print(digits)
# print(punctuation)


