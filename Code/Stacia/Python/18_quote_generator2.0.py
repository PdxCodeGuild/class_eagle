import requests 
import json
import string 




# response = requests.get(url)
# data = response.json()

# quote = data['quote']
# text= quote['body']
# author = quote['author']
# print ()
# print (text)
# print (author)




# data = response.json()
# data_20 = response.json()
# quote = data['quotes']
# vibes = {}
# def vibe_check():
#     vibe= input("did you enjoy this qoute and would you like to save it?")
   
# def quotester():
    
#     for body in data["quotes"]:
#         print ()
#         print (body["body"])
#         print (body["author"])
#         print ()
#         vibe= input("did you enjoy this qoute and would you like to save it?")
#         if vibe.lower()[0] == "y":
#             vibes[body["author"]]=(body["body"])
        
#         go = input ("would you like another quote?")
        
#         if go.lower()[0] == "y" :
#             print ()
#         else:
#             break


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

go = "y"  
page = 1
keyword = input ("Pick a topic.")
while go == "y":

    while True:
        header = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        url =  f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
    
        response = requests.get(url, headers = header)

        data = response.json()
        quote = data['quotes']
        for i in range (20):
            for body in data["quotes"]:
                print ()
                print (body["body"])
                print (body["author"])
                print ()
        blahg = input ("enter next for next page last for last or  end to quit?")
        if blahg.lower == "next":
            page+=1
        else:
            break

    
    
  
                    
    # if mode == "2":
    #     quotester()
    #     redo = input ("would you like to pick a new topic?")
    #     if redo.lower()[0] == "y":
    #         quotester()
    #     vibe_dump = input ("would you like to see your vibes?")
    #     if vibe_dump.lower()[0] == "y":
    #         print (vibes)

