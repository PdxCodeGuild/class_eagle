import requests 
import json

url = f'https://favqs.com/api/qotd'

response = requests.get(url)
data = response.json()

# quote = data['quote']
# text= quote['body']
# author = quote['author']
# print ()
# print (text)
# print (author)


keyword = input ("Pick a topic.")
url = f'https://favqs.com/api/quotes?&filter={keyword}'
header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers = header)
#print (response.text)

data = response.json()

quote = data['quotes']

def quotester():
       
        for body in data["quotes"]:
            print ()
            print (body["body"])
           
            go = input ("would you like another quote?")
            if go == "yes":
                print ()
            else:
                break

quotester()
        
#print (data)