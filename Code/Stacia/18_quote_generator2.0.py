import requests 
import json
import string 

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
vibes = {}
def vibe_check():
    vibe= input("did you enjoy this qoute and would you like to save it?")
    if vibe.lower()[0] == "y":
        wisdom.append()
def quotester():
       
        for body in data["quotes"]:
            print ()
            print (body["body"])
            print (body["author"])
            print ()
            vibe= input("did you enjoy this qoute and would you like to save it?")
            if vibe.lower()[0] == "y":
                vibes[body["author"]]=(body["body"])
            
            go = input ("would you like another quote?")
            
            if go.lower()[0] == "y" :
                print ()
            else:
                break


quotester()
vibe_dump = input ("would you like to see your vibes?")
if vibe_dump.lower()[0] == "y":
    print (vibes)


#print (data)