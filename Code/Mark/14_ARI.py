import requests
import re
import math

url = input("Enter a url: ")


response = requests.get(url)
response.encoding = 'utf-8' # set encoding to utf-8
book = response.text

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




# finds all the words in the requested url
book_words = re.findall(r"[\w']+", book, re.I)
words = 0
for word in book_words:
    words += 1
# finds all the characters in the requested url
book_chars = re.findall(r'[\w]', book, re.I)
chars = 0
for char in book_chars:
    chars += 1
# finds all the sentances in the requested url
book_sentance = book.split('.')
sentances = 0
for sent in book_sentance:
    sentances +=1

# ari math
ari_score = math.ceil(4.71*(chars/words)+0.5*(words/sentances)-21.43)

print(f"""

--------------------------------------------------------
The requested text contains {words} words')
The requested text contains {chars} characters')
The requested text contains {sentances} sentances')
--------------------------------------------------------
The ARI for {url} is {ari_score}
This corresponds to a {ari_scale[ari_score]['grade_level']} level of difficulty
that is suitable for an average person {ari_scale[ari_score]['ages']} years old.
--------------------------------------------------------

""")


