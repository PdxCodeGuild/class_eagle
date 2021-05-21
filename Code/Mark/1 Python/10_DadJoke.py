from os import * # imported for the "cls"
import requests 
import time

while True:
    url = 'https://icanhazdadjoke.com/search?term='

    term = input('Keyword to search for: ')

    # importing the dad joke from the internet
    response = requests.get(url+term, headers={'Accept': 'application/json'})

    # assigning it to the dict 'dad_joke'
    dad_joke = response.json()

    # clearing the screen to make it look better
    system('cls')

    # using a timer to make it seem like its loading for suspense
    print('Loading dadjokes.exe...')
    time.sleep(6)

    # clearing the screen of the loading text and presenting the dad joke
    system('cls')

    # setting results as a dictionary for the results from the search
    results = dad_joke['results']
    
    # iterating through the list of dictionaries to print the results of the search
    for i in results:
        print(i['joke'])

    answer = input('Would you like to search another term? ')

    if answer != 'yes':
        break
