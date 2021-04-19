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
text = response.text    # assign response to text
list_text = text.lower().split()    # make text lowercase and split into list
# print(list_text)


# # running it with the green arrow or "python .\Code\Matthew\lab13_count_words.py"
# # the 'working directory' is class eagle
# with open('./Code/Adam/frankenstein.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
# print(text)


# Write a function that clears the text of documentation and punctuation. 
def clean_ebook(text):
    # https://regex101.com/r/mOQE0o/1
    regex_ebook_start = r'(\*{3})\s(\w{5})\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(...+)(\*{3})'
    # https://regex101.com/r/szSOo2/1
    regex_ebook_end = r'(\*{3})\s(\w{3})\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(...+)(\*{3})'
    start_of_ebook = re.search(regex_ebook_start, text)
    end_of_ebook = re.search(regex_ebook_end, text)
    text = text[start_of_ebook:end_of_ebook]
    ...
    return text

print(clean_ebook(text))

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
