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


# version 2 - List Quotes by Keyword

# Prompt the user for a keyword, list the quotes you get in response, and 
# prompt the user to either show the next page or enter a new keyword. You can 
# use string concatenation to build the URL.


#   this function prints quotes and returns the last page boolean
def print_quotes(page, keyword):
    url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
    header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(url, headers = header)
    data = response.json()
    quotes = data['quotes']
    last_page = data['last_page']
    if last_page != True:
        for quote in quotes:
                display_quote = quote['body'] + ' -' + quote['author']
                print('\n')
                print(textwrap.fill(display_quote, 79))
        else:
            print(f'\nNo more {keyword} quotes')
    return last_page


print('\nWelcome to FavQs\n')


page = 0
last_page = False
while last_page == False:
    keyword = input('\nEnter a keyword or type done: ')
    
    if keyword == 'done':
        break

    last_page = print_quotes(page, keyword)

    user_choice = input('\nWould you like to see the next page? y or n: ')

    if user_choice == 'y':
        page += 1
        print_quotes(page, keyword)

    else:
        last_page = True
