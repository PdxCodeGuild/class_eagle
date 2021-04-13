


'''
Lab 10: Dad Joke API

Use the Dad Joke API to get a dad joke and display it to the user. You may want 
to also use time.sleep to add suspense.

Part 1

This will return a dad joke in JSON format. You can then use the .json() method 
on the response to get a dictionary. Get the joke out of the dictionary and 
how it to the user.
'''

import requests
import json

# Part 1 - Use the requests library to send an HTTP request to https://icanhazdadjoke.com/
# with the accept header as application/json.
response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
# print(response.text)
data = response.json()
print(data['joke'])


# Part 2 - Add the ability to "search" for jokes using another endpoint. Create 
# a REPL that allows one to enter a search term and go through jokes one at a 
# time. You can also add support for multiple pages.

# term = input('Enter a term to search for: ')
# response = requests.get('https://icanhazdadjoke.com/search', headers={'Accept': 'application/json'})
# data = response.json()
# results = data['results']
# # print(results)
# for result in results:
#     print(result)
