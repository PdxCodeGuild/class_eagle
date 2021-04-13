from os import * # imported for the "cls"
import requests 
import time




# importing the dad joke from the internet
response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})

# assigning it to the dict 'dad_joke'
dad_joke = response.json()

# clearing the screen to make it look better
system('cls')

# using a timer to make it seem like its loading for suspense
print('Loading dadjoke.exe...')
time.sleep(6)

# clearing the screen of the loading text and presenting the dad joke
system('cls')
print(dad_joke['joke'])
time.sleep(6)