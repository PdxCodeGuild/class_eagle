
import json
import requests

response = requests.get('https://api.adviceslip.com/advice')
data = response.json()
# print(type(data))
# print(data)




query = input("What kind of advice do you need?")

url = f"https://api.adviceslip.com/advice/search/{query}"

response = requests.get(url)
data = response.json()

for slip in data['slips']:
    advice = slip['advice']
    # print(advice)
    print()
    print(advice)


