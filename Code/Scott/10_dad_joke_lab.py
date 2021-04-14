# Versions & Optimizations:
# - Add a search function that allows you to enter a search term and go through jokes one by one
# - Add support for multiple pages

# Import the HTTP requests library
import requests as req
import os

def random_joke():
    # Make a request to the API w/ custom headers and save it in a variable
    response = req.get('https://icanhazdadjoke.com', headers={'Accept': 'application/json'})

    # Convert the JSON object we've recieved into a python dict
    data = response.json()

    # Print out the 'value' definition
    joke = data['joke']
    return joke

def joke_search(a, b, c):
    # Make a request to the API to get all the jokes for the given search term on the given page
    response = req.get('https://icanhazdadjoke.com/search',
     headers={'Accept':'application/json'}, 
     params={'term': a, 'page': b, 'limit' : c})
    
    # Format it into a dictionary
    data = response.json()
    output = data

    # If no jokes exist, then tell user
    if data['total_jokes'] == 0:
        output = 'No jokes for that search term can be found!'
        print(output)
    else:
        print(f"Page {b} of {output['total_pages']}")


        # only take the results of the page (returns a list)
        output = output['results']
        print(f"Showing jokes {1 + (c*(b-1))}-{len(output) + (c*(b-1))}\n")
        
        for result in output:
            # for each result on the page, only return the joke
            joke = result['joke']
            print(f'{joke}\n')

def max_pages(a, b): # returns the max number of pages the given term returns
    response = req.get('https://icanhazdadjoke.com/search',
     headers={'Accept':'application/json'}, 
     params={'term': a, 'limit' : b})
    
    data = response.json()
    output = data
    
    return output['total_pages']

# print(random_joke())

search_term = input("Enter a search term to find a joke: ")
pg_num = 1
result_lim = 5
direction = 0

max_page = max_pages(search_term, result_lim)

while True: # start of a REPL loop

    # Check that user selected a velid page
    if pg_num <= max_page and pg_num >= 1:
        os.system('cls||clear') # clear terminal
        joke_search(search_term, pg_num, result_lim) # print page
    else: 
        print('ERROR: Page does not exist')
        direction = 0 

    direction = input('Enter -1 to go back a page, and 1 to go forward, enter "exit" to exit: ')
    if direction == 'exit':
        break

    direction = int(direction)
    if direction > 0:
        pg_num += 1
    elif direction < 0:
        pg_num -= 1
