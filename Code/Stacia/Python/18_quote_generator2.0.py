import requests 
import json
import string 

mode = input ("enter 1 for page mode or 2 for vibe check")

url = f'https://favqs.com/api/qotd'

# response = requests.get(url)
# data = response.json()

# quote = data['quote']
# text= quote['body']
# author = quote['author']
# print ()
# print (text)
# print (author)

page = 1
keyword = input ("Pick a topic.")
url = f'https://favqs.com/api/quotes?&filter={keyword}'
header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
url_20 =  f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
response = requests.get(url, headers = header)
response_page = requests.get(url_20, headers = header)

def mode_url(page, keyword):
    keyword = input ("Pick a topic.")
    url_20 =  f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
    header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
    response_page = requests.get(url_20, headers = header)
    data_20 = response.json()
#print (response.text)

data = response.json()
data_20 = response.json()
quote = data['quotes']
vibes = {}
def vibe_check():
    vibe= input("did you enjoy this qoute and would you like to save it?")
   
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


#display pages of 25

def page_mode ():
    for body in data["quotes"]:
        print ()
        print (body["body"])
        print (body["author"])
        print ()

def page_turn (page):
    turn = input ("would you like next or last page?").lower
    if turn == "last":
        page -= 1
    if turn == "next":
        page += 1
    
    
    return (page)
    
# quotester()

# redo = input ("would you like to pick a new topic?")
# if redo.lower()[0] == "y":
#     quotester()
# vibe_dump = input ("would you like to see your vibes?")
# if vibe_dump.lower()[0] == "y":
#     print (vibes)



if mode == "1":
    page_mode()
    go = "y"
    while go == "y":
        page_mode
        go = input ("would you like to continue y/n")
        while go == "y" :
            page_turn(page)
            page_mode()
            go = input ("would you like to continue y/n")
            if go == "y":
                mode_url(page, keyword)
                
if mode == "2":
    quotester()
    redo = input ("would you like to pick a new topic?")
    if redo.lower()[0] == "y":
        quotester()
    vibe_dump = input ("would you like to see your vibes?")
    if vibe_dump.lower()[0] == "y":
        print (vibes)

