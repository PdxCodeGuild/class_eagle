
# import requests
response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
text = response.text

# cd Code/Matthew
# python lab13_count_words.py
with open('arabian_nights.txt', 'r', encoding='utf-8') as file:
    text = file.read()
print(text)

# running it with the green arrow or "python .\Code\Matthew\lab13_count_words.py"
# the 'working directory' is class eagle
with open('./Code/Matthew/arabian_nights.txt', 'r', encoding='utf-8') as file:
    text = file.read()
print(text)


# initial string: Apples, bananas, apples. Pears!
# use regex or string operations to turn our string into a list of strings
# list of strings: ['Apples', 'bananas', 'apples', 'pears']
# count of the strings in this list using a dictionary
# dictionary of counts: {'apples': 2, 'bananas': 1, 'pears': 1}

# d = {'a': 1, 'b': 2}
# if 'a' in d:
#     print('a is in d')









