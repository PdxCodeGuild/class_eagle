# import libraries
import requests as req
import re
# request a book off of Gutenberg.org
response = req.get('https://www.gutenberg.org/files/98/98-0.txt') # Gets 'Tale of Two Cities' by Charles Dickens
response.encoding = 'utf-8' # set encoding to utf-8
# Put it into a string variable
text_in = response.text

# Format the string
regex = r'\S+\b'
# Remove all punctuation and split the long string into a list of words
result = re.findall(regex, text_in)

for i in range(len(result)):
    # Convert it all into lowercase
    result[i] = result[i].lower()

# Create an empty dictionary
word_dict = {}

for i in range(len(result)):
    # IF the word is already in the dictionary
    if result[i] in word_dict:
    #   THEN increment that words value up one
        word_dict[result[i]] += 1
    # ELSE IF the word is not already in the dictionary 
    else:
    #   THEN add that word to the dictionary with a value of one
        word_dict[result[i]] = 1


# Print out the most frequent top 10 words
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])