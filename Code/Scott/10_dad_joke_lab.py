# Versions & Optimizations:
# - Add a search function that allows you to enter a search term and go through jokes one by one
# - Add support for multiple pages

# Import the HTTP requests library
import requests as req

# Make a request to the API w/ custom headers and save it in a variable
response = req.get('https://icanhazdadjoke.com', headers={'Accept': 'application/json'})

# Convert the JSON object we've recieved into a python dict
data = response.json()

# Print out the 'value' definition
joke = data['joke']
print('Here\'s your dad joke:')
print(joke)