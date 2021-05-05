import requests as rec

url = 'https://icanhazdadjoke.com' # make adress easy to imput

response = rec.get(url, headers={'Accept':'application/json'})

data = response.json()
joke = data['joke']
print (joke)