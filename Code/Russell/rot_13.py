
import string


#Start with a string containing the letters
alph_1 = string.ascii_lowercase

#Get a word from the user and an interger for the offset
word = input('What is your word?')
offset = int(input("How much do you want to offset by?"))

#Creat a new list for the offset index and add the new index numbers 
enc_word = []
for char in word:
    enc_word.append(alph_1.find(char) + offset)

#Fix the numbers that are out of range of the alphabet string 
for i in range(len(enc_word)):
    if enc_word[i] >= len(alph_1):
        enc_word[i] = enc_word[i] - len(alph_1)


#Use the index numbers to add the corrisponding characters to a new string
code_word = ''
for i in enc_word:
    code_word += alph_1[i]


print(code_word)



