import string # imports string functions

card_values ={# a dictonary of values. A is currently 1 point but will be redfined if 
    'A' :  1,
    '2'  : 2,
    '3'  : 3,
    '4'  : 4,
    '5'  : 5,
    '6'  : 6,
    '7'  : 7,
    '8'  : 8,
    '9'  : 9,
    'J' : 10,
    'Q' : 10,
    'K' : 10

}


def draw():# this function is designed to draw a card and evaluate its value. 

    card = input ("What is your card? ") #user requests card
    if not card.isdigit(): # if the card is  not a didgit
        card = card.upper()[0] # cards is convereted to uper case and stripped to first digit.
        card = card_values.get(card) # we will have a value even if user types queeeeeeen
        
    if int(card) <= 10 and int(card) >= 1: #evaluates if user input is a 
        card = int(card)
    if (card) == "A":
        
    return (card, ac)

def check():
    if points  == 21:
        print ("21!!!")
    elif points > 21:
        print ("bust")
    elif points > 17:
        print ( "I recomend you hold there partner." )
    elif points < 17:
        print ("Saddle up partner hit!")
    if  ac =>1  and points <= 10:
        points +1 
        

points = 0
ac = 0

for i in range(3):
     ac = draw()
    if card = 1
        Ac+=1
    points = points + card
    print (points)

check ()

