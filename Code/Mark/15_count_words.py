import requests
import re


response = requests.get('http://www.gutenberg.org/files/65075/65075-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
book = response.text

book = re.findall(r'\w+',book)


count = 0
word_count = {}
for word_count in book:
    word = word.lower()
    if word in word_count:
        continue
    count_word = book.count(word)
    word_count[word] = count_word




words = list(word_count.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])