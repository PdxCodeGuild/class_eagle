import string
import re
import math


with open('The_White_Company.txt', 'r', encoding='utf-8') as file:
    text = file.read()



def get_words(text):
    regex = r'\w+'
    words_result = re.findall(regex, text)
    return len(words_result)


def get_characters(text):
    regex = r'\w' 
    char_result = re.findall(regex, text)
    return len(char_result)
    

def get_sentences(text):
    regex = r'\s+[^.!?]*[.!?]'
    sentence_result = re.findall(regex, text)
    return len(sentence_result)


words = get_words(text)
characters = get_characters(text)
sentences = get_sentences(text)


print(words)
print(characters)
print(sentences)

x = characters / words
y = words / sentences

a = 4.71 * x
b = 0.5 * y - 21.43


ari_float = a + b

ari_int = math.ceil(ari_float)

print(ari_int)

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

print(ari_scale[ari_int])

print(f"The ARI for that text is {ari_int}, which is a {ari_scale[8]['grade_level']} reading level. \n That\'s suitable for the average {ari_scale[8]['ages']} year old.")

