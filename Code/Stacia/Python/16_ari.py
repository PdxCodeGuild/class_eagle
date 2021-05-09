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
#print(contents)


def setence_maker(contents):
    contents = contents.replace('\n'," ")
    setences = (re.split('[.?!]', contents)) # clean up the data into setences
    return setences

def make_word (setences):
    regex = r'\w+'
    words = re.findall(regex, contents)
    
    return words
   
def word_length(setences):    
    regex = r'\w' 
    char_count = re.findall(regex, contents)
    char_count =(len(char_count))
    return char_count

def ari(char_count, words, setence_countsetences):
    x = char_count / len(words)
    y = len(words) / len(setences)
    a = 4.71 * x
    b = 0.5 * y - 21.43
    ari_float = a + b
    return ari_float


setences = setence_maker(contents)
words = make_word(setences)
char_count = word_length(words)

ari=  ari(char_count, words, setence_count)

# split = name.split("\\")
# split = split[len(split)-1].split(".")

# title = (split[0].replace("_"," "))
# print(ari_float)
# print(f'{title} has an ARI of {ari_float}')
print(f'Arabian Nights has an ARI of {ari}')
    
    

