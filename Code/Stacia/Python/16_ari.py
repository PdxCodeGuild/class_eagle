# the purpose of this program is to count the number of words in a setence to calculate its readability. 

#imports
import requests
import string
import re
list_alpha=string.ascii_lowercase

# deffinitions

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
list_alpha=string.ascii_lowercase
punc = ["." ,"*", "!", "?"]
word_dict = {}
okay_punc =['\'' ,'\"', '-','_']


f = open(r'C:\Users\16616\Desktop\pdx_code\code\class_eagle\Code\Stacia\arabian_nights.txt')  # open the file
contents = f.read().lower()  # read the contents
#print(contents)
contents = contents.replace('\n'," ")
setences = (re.split('[.?!]', contents)) # clean up the data
char_count = 0
setence_count= len(setences)


def county(setences):
    
    for i in setences: #itterate over each setence
        regex = r'\w+'
        words = re.findall(regex, contents) # now we have every word in every setence.
        print (words)
        
        
    return (char_count)

def make_word (contents):
    regex = r'\w+'
    words = re.findall(regex, contents)
    return words
   
def word_length(contents):    
    regex = r'\w' 
    char_count = re.findall(regex, contents)
    char_count =(len(char_count))

def ari(words, setence_count):
    x = char_count / words
    y = words / sentence_count
    a = 4.71 * x
    b = 0.5 * y - 21.43
    ari_float = a + b
    return ari_float

char_count = county(setences)
# contents = make_word (contents)

# char_count = county(setences)
# print (char_count)
# make_word (contents)
# word_length(contents)
# ari(words, setence_count)

# print(ari_float)

    
    
    

