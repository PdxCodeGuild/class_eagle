import requests
import json

query = input('What advice do you want?: ')

url = f'https://api.adviceslip.com/advice/search/{query}'
response = requests.get(url)
data = response.json()
# for i in range(len(data['slips'])):
    
#     print('\n' + data['slips'][i]['advice'])

for slip in data['slips']:
    print('\n' + slip['advice'])