import requests
import json


# response = requests.get('https://favqs.com/api/qotd')
# data = response.json()

# print(data)

# print(f"Quote: {data['quote']['body']} \nAuthor: {data['quote']['author']}")

#--------PART TWO --------------------------
# response = requests.get('https://favqs.com/api/quotes?page=<page>&filter=<keyword>')
# data = response.json()


query = input('What kind of quotes are you looking for?')

page = 1

url = f'https://favqs.com/api/quotes?page={page}&filter={query}'

header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers= header)
data = response.json()

data_list = data['quotes']

for thing in data_list:
    print(thing['body'],thing['author'])
    
#Ask the user for their next move and adjust the search accordingly 
while True:   
    next_move = input('Type next to see the next page, or type a new word')
    if next_move == 'next':
        page += 1
    elif next_move != 'next':
        query = next_move

    url = f'https://favqs.com/api/quotes?page={page}&filter={query}'

    header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response = requests.get(url, headers= header)
    data = response.json()

    data_list = data['quotes']

    for thing in data_list:
        print(thing['body'],thing['author'])



