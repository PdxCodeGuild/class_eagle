import html
import requests as req

amount = input('How many questions would you like? ')
amount = str(amount)
amount_int = int(amount)

response = req.get('https://opentdb.com/api.php', params={  # Makes request to the API
    'amount': amount,
    'category': '18', # The code for the 'Science: Computers' category
    'type': 'boolean' # True / False questions only
})
data = response.json() # Get JSON object back
score = 0
round_count = 0

for result in data['results']:
    round_count += 1
    question = html.unescape(result['question']) # Format from HTML encoding
 
    print('\n'+f'Round {round_count} of {amount}:\n'+question) # Tell user round they're in

    # REPL for input
    while True:
        ans = input('True or False (T/F)? ')
        ans = str(ans)

        if ans == 't' or ans == 'T': # idk why ans.lower() didn't work, so rather than fix it, it was easier to just add an OR condition
            if result['correct_answer'] == 'True': # Check our answer matches the correct one
                score += 1
                print('Correct, +1 point!')
                break
            else:
                print('Incorrect, no change to your score')
                break
        elif ans == 'f' or ans == 'F': # idk why ans.lower() didn't work, so rather than fix it, it was easier to just add an OR condition
            if result['correct_answer'] == 'False': # Check our answer matches the correct one
                score += 1
                print('Correct, +1 point!')
                break
            else:
                print('Incorrect, no change to your score')
                break
        else: # catch all for any other input
            print('invalid input')
            continue

print(f'\nThank you for playing! Your score was: {score}')
print(f'You were correct for {round((score/amount_int)*100, 1)}% of the questions asked\n') # Calculates success percentage to one decimal place