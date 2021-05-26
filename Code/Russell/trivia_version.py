import html
import json
import requests


response = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
text = response.json()

text_list = text['results']



right = 0 
wrong = 0 


for i in range(len(text_list)):
    answer = input(f"Question: {html.unescape(text_list[i]['question'])} true or false? " )
    answer = answer.title()
    if answer == text_list[i]['correct_answer']:
        print("SURRRVEY SAYS...CORRECT!")
        right += 1
    elif answer != text_list[i]['correct_answer']:
        print("I'm sorry, thats INCORRECT!")
        wrong += 1

print(f"Right:{right}")
print(f"wrong:{wrong}")






