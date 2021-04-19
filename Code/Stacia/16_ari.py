
import requests
import string
import re

#Created by Alison Bechdel in 1985, The Bechdel Test is a measure of female representation in film and television that uses three criteria for evaluating the presence and visibility of strong female characterizations.

# three criteria.
# At least two named female characters?
# do they speak to eachother?
# do they speak to each other about something other than a male love intrest?
# the goal of this is to create a system of indexing by gender and non gender markers in works of liturature to help facilitate liturary analasis.
# 
#
remove

#author "Stacia Aguilar"


#steps 1 take in put 2 format text


# break at new line
#

punc = [",", "." ,"*", "!", "?"]
word_dict = {}
okay_punc =['\'' ,'\"', '-','_']


[i]



f = open(r'C:\Users\16616\Desktop\pdx_code\code\class_eagle\Code\Stacia\arabian_nights.txt')  # open the file
contents = f.read()  # read the contents
#print(contents)
setences = (re.split('[.?!]', contents))


print(setences)

#for i in range(len(contents)):
 #   if contents[i] in word_dict:
  #      word_dict[contents[i]] += 1
   # if contents[i] not in word_dict:
    #   word_dict[contents[i]] = 1
    

#for indicator in gender_markers: #take the markers from our list of gender markers.
    
 #   found_markers[indicator]=word_dict.get(indicator)

#print(found_markers)
    #list , key value tupple,
#word_dict_keys=list(word_dict.keys())


#words = list(word_dict.items()) # .items() returns a list of tuples
#words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
#for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    #print(words[i])
