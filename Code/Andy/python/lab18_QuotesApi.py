import requests
import json
'''

                     Version 1

response = requests.get('https://favqs.com/api/qotd')
data = response.json()


quotes = {}
author = data['quote']['author']
body = data['quote']['body']
quotes[author] = body
print(quotes)

'''

################ Version 2 ##################
# This code outputs 25 quotes at a time given a subject

def run():
    page = 1
    keyword = input('What would you like a quote on? \n')
    url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
    response = requests.get(url ,headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'} )
    data = response.json()
    print('\n')
    for num in range(0,25):
        print(data['quotes'][num]['body']) # print quote 
        print('-' + data['quotes'][num]['author']) # print author
        print('\n')
    while data['last_page'] == False:
        ask = input('"next page" or "done"? ')
        if ask != 'next page' and ask != 'done': # 'error' message in case a typo or invalid option is entered
            ask = input('please enter "next page" or "done" ')
        while ask == 'next page':
            page += 1
            url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
            response = requests.get(url ,headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'} )
            data = response.json()
            print('\n')
            for num in range(0,25):
                print(data['quotes'][num]['body'])
                print('-' + data['quotes'][num]['author'])
                print('\n')
            break
        if ask == 'done':
            break
    if data['last_page'] == True:
        print('This is the last page of quotes!')
# lines 25-32 and 39-46 are the same and can be made into a function to call, these lines request, and print the pertinent data.

# REPL
run_again ='y'
while run_again == 'y':
    run()
    run_again = input('new search? y/n ')
    if run_again != 'y':
        print('Goodbye!')
