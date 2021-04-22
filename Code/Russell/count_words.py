import re
import string


with open('Arabian_Nights.txt', 'r', encoding='utf-8') as file:
    text = file.read()


text = text.lower() 
punc = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""" # fix this  
for char in text:
    if char in punc:
        text = text.replace(char, '')

regex =  r'\w+'

result = re.findall(regex, text)


arabian_words = {}
for i in range(len(result)):
    if result[i] not in arabian_words:
        arabian_words[result[i]]=1
    elif result[i] in arabian_words:
        arabian_words[result[i]]+=1


# print(arabian_words)

words = list(arabian_words.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])




