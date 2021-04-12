


import requests
response = requests.get('https://api.chucknorris.io/jokes/random')
# print(response)
# print(type(response))

# read the raw response
# print(response.text)

# take the JSON in the response and turn it into a python dictionary
data = response.json()
joke = data['value']

print(joke)


