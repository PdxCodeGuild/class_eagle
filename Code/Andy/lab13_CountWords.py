# Improvements - let user pick website, use expressions


import requests
import string
import re

response = requests.get('http://www.gutenberg.org/files/1342/1342-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8


def lower_strip(text):
    text = str(text)
    text_1 = text.lower()
    text_2 = ''
    punctuations = '''!()-[]{\};:'"\,<>./?@#$%^&*_~'''
    for char in text_1:
        if char not in punctuations:
            text_2 += char
    text_2 = text_2.split()
    return text_2


def count_words(stripped_text):

    word_library = {}

    for word in stripped_text:
        word_library[word] = word_library.get (word, 0) + 1
    return word_library

def sort_words(dictionary):
    sorted_dict = {}
    sorted_keys = sorted(dictionary, key = dictionary.get)
    for w in sorted_keys:
        sorted_dict[w] = dictionary[w]
    return sorted_dict

def top_10(dict):
    words = list(dict.items()) 
    words.sort(key=lambda tup: tup[1], reverse=True)  
    for i in range(min(10, len(words))):  
         print (words[i])
    return words[i]





top_10(count_words(lower_strip(response.text)))


#print(lower_strip(response.text))





