'''
Lab 14: Automated Readability Index

Compute the automated readability index (ARI) for a given book. The general 
formula to compute the ARI is as follows:

4.71(charcaters/words) + 0.5 (words/sentences) - 21.43

If the result is a decimal, always round up, and if the result is higher than 
14, it should be set to 14.
'''

import re
import requests
import math

response = requests.get('http://www.gutenberg.org/files/84/84-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
text = response.text    # assign response to text
# list_text = text.lower().split()    # make text lowercase and split into list


# write a function that returns num_characters. Total letters and numbers.
def count_characters(text):
    count = 0
    return count

# write a function that returns num_of_words. Number of spaces.
def count_words(text):
    count = 0
    return count

# write a function that returns num_senctences. Number of '.', '!', '?'.
def count_sentences(text):
    count = 0
    return count

# Once you’ve computed the ARI score, you can use the following dictionary to 
# look up the age range and grade level:
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# store the number of characters, words, and sentences
num_of_characters = count_characters(text)   # number of letters and numbers
num_of_words = count_words(text)   # number of spaces
num_of_sentences = count_sentences(text)    # number of '.', '!', and '?'

ari = math.ceil(4.71*(num_of_characters/num_of_words) + .5*(num_of_words/num_of_sentences)-21.43)

if ari > 14: 
    ari = 14

print(ari_scale[ari])


