import requests
import html


url = f'https://opentdb.com/api.php?amount=10&category=18&type=boolean'
# get a responce from api
response = requests.get(url)
# convert to a list of dictionarys
data = response.json()

results = data["results"]
print( results)
# seperate the results into infi

for lamma in data["question"]:
    print ( lamma.get["question"])
    
    

# for question in data[results]: 
#     print resul(question["question"])