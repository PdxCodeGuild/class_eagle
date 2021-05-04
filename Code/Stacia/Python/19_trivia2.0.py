import requests
import html

categories = [
    
    {'General Knowledge': 9 },
    {'Entertainment: Books': 10 },
    {'Entertainment: Film' : 11},
    {'Entertainment: Music': 12 },
    {'Entertainment: Musicals &amp; Theatres': 13 },
    {'Entertainment: Television': 14 },
    {'Entertainment: Video Games': 15 },
    {'Entertainment: Board Games': 16 },
    {'Science &amp; Nature': 17 },
    {'Science: Computers': 18 },
    {'Science: Mathematics': 19 },
    {'Mythology': 20 },
    {'Sports': 21 },
    {'Geography': 22 },
    {'History' : 23 },
    {'Politics' : 24 },
    {'Art' : 25 },
    {'Celebrities' : 26 },
    {'Animals' : 27 },
    {'Vehicles' : 28 },
    {'Entertainment: Comics' : 29 },
    {'Science: Gadgets' : 30 },
    {'Anime and Manga' : 31 },
    {'Cartoon and Animation': 32 }
]
score = 0  #this will store our points. 
#variables for url.

amount = int(input ("how many questions?"))
for i in range( len (categories)):
    print (categories[i])
topic = input ("please select a catagory")


url = f'https://opentdb.com/api.php?amount={amount}&category={topic}&type=boolean'
# get a responce from api
response = requests.get(url)
# convert to a list of dictionarys
data = response.json()

results = data["results"]
#print( results)

#this will run 10 times to give up 
for i in range(amount):
    print (f'Question:{i+1}')
    print ()
    #display question
    print(html.unescape(data['results'][i]['question']))
    #user input guess
    guess = input ("True or False?")
    #evaluate user input against answer. 
    if guess.title() == data['results'][i]['correct_answer']:
        print ("Correct!")
        score +=1
#display correct answers
print (f'You scored {score} points!')
