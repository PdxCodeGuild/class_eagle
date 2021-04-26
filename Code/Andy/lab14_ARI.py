
import requests
import math
import re

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


run_again = 'y'
while run_again == 'y':
    url = input('Enter gutenburg.com book in .txt url format to find out its ARI. ')
    response = requests.get(url)
    response.encoding = 'utf-8' # set encoding to utf-8
    text = response.text 
    text = str(text)

    reg = r'\w+'
    words = re.findall(reg,text)
    words = len(words)

    reg = r'\w|d'
    characters = re.findall(reg,text)
    characters = len(characters)

    reg = r'([A-Z][^\.!?]*[\.!?])'
    sentences = re.findall(reg, text)
    sentences = len(sentences)


    ari = 4.71*(characters/words) + .5*(words/sentences) - 21.43
    ari = math.ceil(ari)

    grade = ari_scale[ari]['grade_level']
    age = ari_scale[ari]['ages']

    print(f'The text in the URL entered has an ARI of {ari}, this corresponds to {grade} level of difficulty that is suitable for the ages of {age}')

    run_again = input('Find the ARI of another text? y/n ')

