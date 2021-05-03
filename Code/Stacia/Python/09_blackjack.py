import string # imports string functions

card_values ={# a dictonary of values. A is currently 1 point but will be redfined if 
    'A' :  11,
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

points = 0
ace_count = 0


def draw(points,ace_count):# this function is designed to draw a card and evaluate its value. 
    
    card = input ("What is your card? ") #user requests card
    if card.upper()[0] == "A":
            ace_count += 1
            
    if not card.isdigit(): # if the card is  not a didgit
        card = card.upper()[0] # cards is convereted to uper case and stripped to first digit.
        card = card_values.get(card) # we will have a value even if user types queeeeeeen
        
            
    
    points += int(card)  
    return points, ace_count
    
        

def check(points,ace_count):
    print(points)
    if points > 21:
        if ace_count > 0:
            points -= 10
            print("aces wild")
        else:
            print ("bust")
         
    if points  == 21:
            print ("21!!!")
    
    
    if points > 17 and  points < 21:
        print ( "I recomend you hold there partner." )

    if points <= 16:
        print ("Saddle up partner hit!")
    return points



for i in range (3):
    points,ace_count = draw(points, ace_count)   
    check(points, ace_count)
    
    if points == 21 :
        break
        
    
    
    