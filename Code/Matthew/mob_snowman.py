



import requests

def get_random_word():
    url = 'https://random-word-api.herokuapp.com/word/?swear=0' # url of the web API
    response = requests.get(url) # send a GET request to the url
    data = response.json() # take the JSON in response and turn it into a list
    word = data[0] # get the first element of the list
    return word # return it


print(get_random_word())
print(get_random_word())


