import random
import  string

lowercase_string=string.ascii_lowercase
uppercase_string=string.ascii_uppercase
i= 0
listomania=[]
lower_list=[]
lenlower=len(lowercase_string)
uppercase_list =[]
y= 0
z=0
    
for char in (string.ascii_lowercase):
  x=char
  lower_list.append(x)
  
for char in (string.ascii_uppercase):
  x=char
  uppercase_list.append(x)
  
special = []
password_length
total_characters= int(input("how many characters would you like?"))
capital= int(input ("How many capital letters would you like"))
total_numbers=int(input("how many numbers would you like in your password"))
lower= int(total_characters -(total_numbers + capital))
#special= input (put any any special characters you would like to use)


if lower < 0:
  print ("that seems a bit off, but lets just make it longer until v2.0 comes out")
if lower == 0:
  print ("You got it")
if lower > 0:
  print ("Great! and we will finish up the last (lower) with some lower case letters. ")


while i < total_numbers:
    i+=1
    listomania.append(random.randint(1, 100))


while (y) < lower:
  y +=1
  listomania.append(random.choice(lower_list))

while z < capital:
  z +=1
  listomania.append(random.choice(uppercase_list))

password=random.sample(listomania,len(listomania))
print (password)
