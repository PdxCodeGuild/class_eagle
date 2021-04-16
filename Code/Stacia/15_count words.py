import requests
import string

punc = [",", "." ,"*", "!", "?"]
word_dict = {}

top_10= []
f = open(r'C:\Users\16616\Desktop\pdx_code\code\class_eagle\Code\Stacia\arabian_nights.txt')  # open the file
contents = f.read()  # read the contents
#print(contents)


contents = contents.lower()
contents = contents.split()


print(contents)



for i in range(len(contents)):
    if contents[i] in word_dict:
        word_dict[contents[i]] += 1
    if contents[i] not in word_dict:
       word_dict[contents[i]] = 1
    


#word_dict_keys=list(word_dict.keys())


words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
