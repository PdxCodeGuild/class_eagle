# import libraries
import requests as req
import re

def find_ari(text):
    regex_char = r'\w|d' # finds number of letters and digits
    regex_word = r'\s+' # finds number of whitespaces (" " = 1, "    " = 1, " a " = 2)
    regex_sentence = r'[A-Z0-9]*\.|!|\?' # finds segments of the string that start with a capital letter or a number, and end with a . or ! or ?
    output = []

    char_count = len(re.findall(regex_char, text)) # Counts all segments that satisify the condition specified in regex_char
    word_count = len(re.findall(regex_word, text)) # Counts all segments that satisify the condition specified in regex_word
    sentence_count = len(re.findall(regex_sentence, text)) # Counts all segments that satisify the condition specified in regex_sentence

    ari_formula = (4.71*(char_count/word_count))+(0.5*(word_count/sentence_count))-21.43 # Applies ARI formula to the text input
    output = round(ari_formula) # Round to the nearest integer for output
    return output

# Dictionary of dictionaries for the ARI scale
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


# request a book off of Gutenberg.org
response = req.get('https://www.gutenberg.org/files/98/98-0.txt') # Gets 'Tale of Two Cities' by Charles Dickens
response.encoding = 'utf-8' # set encoding to utf-8
# Put it into a string variable
text_in = response.text

ari = find_ari(text_in)
grade = ari_scale[ari]['grade_level']
age = ari_scale[ari]['ages']
print('For the input text of A Tale of Two Cities by Charles Dickens') # Had to hardcode input text, no easy way to get title and author from plain string using Gutenberg.org
print(f'The ARI is ~{ari}, that\'s the equivelant of {grade} or ages {age}')