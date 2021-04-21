


import requests
import json

url = 'https://icanhazdadjoke.com/'
response = requests.get(url, headers={'Accept': 'application/json'})
data = response.json()
joke = data['joke']
print(joke)


# response = requests.get('https://icanhazdadjoke.com/search?term=hipster')
response = requests.get('https://icanhazdadjoke.com/search', params={'term': 'hipster'}, headers={'Accept': 'application/json'})
data = json.loads(response.text)
print(json.dumps(data, indent=4))





