'''
Lab 18: Quotes API
For this lab we'll be using the Favqs Quotes API to first get a random quote, 
and then allow the user to find quotes by keyword. To accomplish this we'll be 
using the requests library.
'''


import requests
import json
import textwrap  

# version 1 - get the quote of the day and its author

# url = 'https://favqs.com/api/qotd'
# response = requests.get(url)
# data = response.json()
# # print(data)

# # quote_of_the_day
# qotd = data['quote']['body']
# author = data['quote']['author']

# print(f'\n{qotd} -{author}\n')


# version 2 - List Quotes by Keyword




keyword = input('Enter a keyword: ')
page = 0
url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers = header)
data = response.json()

page = data['page']
last_page = data['last_page']
quotes = data['quotes']

for quote in quotes:
    display_quote = quote['body'] + ' -' + quote['author']
    print(textwrap.fill(display_quote, 79))
    print('\n')