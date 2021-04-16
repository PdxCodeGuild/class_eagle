'''
Lab 13: Count Words

Write a python module to analyze a given text file containing a book for its 
vocabulary frequency and display the most frequent words to the user in the 
terminal.
'''
import re
import requests


response = requests.get('http://www.gutenberg.org/files/84/84-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
text = response.text
# print(text)
list_text = text.lower().split()
# print(list_text)

# Write a function that returns just the book section of text
def ebook_crusts_cutoff():
    # # https://regex101.com/r/mOQE0o/1
    regex_start = r'(\*{3})\s(\w{5})\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(...+)(\*{3})'
    # # https://regex101.com/r/szSOo2/1
    regex_end = r'(\*{3})\s(\w{3})\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(...+)(\*{3})'

    # start_of_ebook = re.search(regex_start, text)
    # end_of_ebook = re.search(regex_end, text)

    # text = text[start_of_ebook:end_of_ebook]
    # print(text)
    ...
    return text


word_count_dic = {}
for i in range(len(list_text)):
    if list_text[i] not in word_count_dic:
        word_count_dic[list_text[i]] = 1
    else:
        word_count_dic[list_text[i]] += 1

# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_count_dic.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

        
# print(word_count_dic)

# starter code
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
# list of strings: ['Apples', 'bananas', 'apples', 'pears']
# count of the strings in this list using a dictionary
# dictionary of counts: {'apples': 2, 'bananas': 1, 'pears': 1}

# d = {'a': 1, 'b': 2}
# if 'a' in d:
#     print('a is in d')
