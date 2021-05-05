import requests
import re


response = requests.get('http://www.gutenberg.org/files/65075/65075-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
book = response.text


# asks the user for the keyword to search by
user_word = input('Select a keyword to search for: ')


# raw string to find all uses of the user word and the word that follows it
book = re.findall(fr"({user_word} [\w']+)",book, re.I)



# a for loop to iterate through each string and take count of each time it appears
count = 0
word_count = {}
for words_2 in book:
    words_2 = words_2.lower()
    if words_2 in word_count:
        continue
    count_word = book.count(words_2)
    # adds the selected string and its count as key:values pairs in a dictionary
    word_count[words_2] = count_word 



words = list(word_count.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])