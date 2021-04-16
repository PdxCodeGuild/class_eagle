

# import requests
# response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
# response.encoding = 'utf-8' # set encoding to utf-8
# text = response.text

# cd Code/Matthew
# python lab13_count_words.py
# with open('arabian_nights.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
# print(text)

# running it with the green arrow or "python .\Code\Matthew\lab13_count_words.py"
# the 'working directory' is class eagle
# with open('./Code/Matthew/arabian_nights.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
# print(text)


# initial string: Apples, bananas, apples. Pears!
# use regex or string operations to turn our string into a list of strings
# list of strings: ['apples', 'bananas', 'apples', 'pears']
# count of the strings in this list using a dictionary
# dictionary of counts: {'apples': 2, 'bananas': 1, 'pears': 1}


# 1) start with an empty dictionary
# 2) iterate over your list of strings
# 3) if a word is in the dictionary, increment its value
# 4) if a word is not in the dictionary, add it with a value of 1

# d = {'a': 1, 'b': 2}
# if 'a' in d:
#     print('a is in d')




def add(a, b):
    return a + b

add = lambda a, b: a + b




# word_dict is a dictionary where the key is the word and the value is the count
word_dict = {'apples': 2, 'bananas': 1, 'pears': 1, 'kiwi': 7}
print(word_dict)
words = list(word_dict.items()) # .items() returns a list of tuples
print(words)
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
print(words)
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])










