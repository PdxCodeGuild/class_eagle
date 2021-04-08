
import random
import string


n = int(input("How many lower case characters do you want?"))
o = int(input("How many upper case characters do you want?"))
p = int(input("How many special characters do you want?"))

char_low = 0
char_up = 0 
char_dig = 0

password = ''

while char_low < n:
    password += random.choice(string.ascii_lowercase)
    char_low += 1

while char_up < o:
    password += random.choice(string.ascii_uppercase)
    char_up += 1

while char_dig < p:
    password += random.choice(string.digits)
    char_dig += 1


password = list(password)
random.shuffle(password)
random.shuffle(password)

x = ''.join(password)

print(x)


