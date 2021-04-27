'''
Lab 18: Quotes API
For this lab we'll be using the Favqs Quotes API to first get a random quote, 
and then allow the user to find quotes by keyword. To accomplish this we'll be 
using the requests library.
'''


import requests
import json
import textwrap
import time

# version 1 - get the quote of the day and its author

url = 'https://favqs.com/api/qotd'
response = requests.get(url)
data = response.json()
# print(data)

# quote_of_the_day
qotd = data['quote']['body']
author = data['quote']['author']

print(f'\n{qotd} -{author}\n')


