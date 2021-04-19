#benchdel marking of casic litturature.


import requests
import string

# Why?= What is a bedchdel test?


#Created by Alison Bechdel in 1985, The Bechdel Test is a measure of female representation in film and television that uses three criteria for evaluating the presence and visibility of strong female characterizations.

# three criteria.
# At least two named female characters?
# do they speak to eachother?
# do they speak to each other about something other than a male love intrest?
# the goal of this is to create a system of indexing by gender and non gender markers in works of liturature to help facilitate liturary analasis.
# 
#
title = '''
____  _____  ____ __  __ _____ _____ __       ___  __  ___  _____ __ __ __ __  __  ____  
||=)  ||==  ((    ||==|| ||  ) ||==  ||       || \/ | ||=|| ||_// ||<<  || ||\\|| (( ___ 
||_)) ||___  \\__ ||  || ||_// ||___ ||__|    ||    | || || || \\ || \\ || || \||  \\_|| '''


#author "Stacia Aguilar"


#desired feature list
# user decided input method
    #take in any book from project guttenburg.
    # take in work from plain text

# start up
 #introduction to Bechdel testing.
        # options what is bechdel
        # input an option
        # quit
        # previoud results
    #user input-------------
    # 



# what to do when
print(title)
punc = [",", "." ,"*", "!", "?"]
word_dict = {}
gender_markers = ["she", "he", "they", "it" ,"her's", "her", "hers", "his","its", "theirs" ]
top_10= []
found_markers ={}


f = open(r'C:\Users\16616\Desktop\pdx_code\code\class_eagle\Code\Stacia\arabian_nights.txt')  # open the file
contents = f.read()  # read the contents
#print(contents)


contents = contents.lower()
contents = contents.split()


#print(contents)



for i in range(len(contents)):
    if contents[i] in word_dict:
        word_dict[contents[i]] += 1
    if contents[i] not in word_dict:
       word_dict[contents[i]] = 1
    

for indicator in gender_markers: #take the markers from our list of gender markers.
    
    found_markers[indicator]=word_dict.get(indicator)

print(found_markers)
    #list , key value tupple,
#word_dict_keys=list(word_dict.keys())


#words = list(word_dict.items()) # .items() returns a list of tuples
#words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
#for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    #print(words[i])
