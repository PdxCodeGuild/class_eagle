import requests
import json


# Prompting the user for their keyword
keyword = input('Enter a keyword to search for: ')
page = 1
last_page = 500


while page <= last_page:
    # using the requests to search for quotes with that keyword
    url = f'https://favqs.com/api/quotes'
    response = requests.get(url,headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params={'page': page, 'filter': keyword})
    response = response.json()



    # printing out the page number
    print('----------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(f"Page: {response['page']}")
    print('----------------------------------------------------------------------------------------------------------------------------------------------------------')
    # looping through the response to print out the quotes and their authors
    for i in range(len(response['quotes'])):
            if response['quotes'][i]['body'] == 'No quotes found':
                print('No quotes found')
            else:
                print(f"Quote: \"{response['quotes'][i]['body']}\"")
                print(f"Author: {response['quotes'][i]['author']}")
                print('\n')
    
    # prompting the user if they would like to go to the next page
    print('----------------------------------------------------------------------------------------------------------------------------------------------------------')
    prompt = input('Next page? ')
    if prompt != 'yes':
        print('Thank you!')
        break
    else:
        page += 1
    print('----------------------------------------------------------------------------------------------------------------------------------------------------------')