
import random
import string
lowercase =5
uppercase = 3

passw =[]
password = ""
for i in range(lowercase):
    # b =random.choice(string.ascii_lowercase)
    passw.append(random.choice(string.ascii_lowercase))
for i in range (uppercase):
    # b = random.choice(string.ascii_uppercase)
    passw.append(random.choice(string.ascii_uppercase))
random.shuffle(passw)

for i in range (len(passw)):
    password += passw [i]
print (password)