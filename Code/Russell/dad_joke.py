
import requests 
import json

response = requests.get('https://icanhazdadjoke.com/', headers={'accept': "application/json"})

x = response.json()

print(x['joke'])


