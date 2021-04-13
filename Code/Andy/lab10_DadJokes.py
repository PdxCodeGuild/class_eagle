import requests

url = 'https://icanhazdadjoke.com/'

response = requests.get(url, headers={'Accept' :'applications/json'})
data = response.json()
joke = data['joke']
print(joke)

