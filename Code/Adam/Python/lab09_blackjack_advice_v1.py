


'''
Lab 9: Blackjack Advice


Write a program that gives basic blackjack playing advice during a game by 
asking the player for cards. 

Use the following rules to determine the advice:
- Less than 17, advise to "Hit"
- Greater than or equal to 17, but less than 21, advise to "Stay"
- Exactly 21, advise "Blackjack!"
- Over 21, advise "Already Busted"

Print out the current total point value and the advice.
'''


def card_value(card):
    face_cards = {'A':1, '1':1, '2':2, '3':3, '4':4, '5': 5, '6':6, '7':7, '8':8, '9':9, 'J':10, 'Q':10, 'K':10}
    return face_cards[card]

# face_cards = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}

face_cards = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}
hand_total = 0

# 1) Ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K).
# 2) figure out the point value of each card individually. Number cards are 
# worth their number, all face cards are worth 10. At this point, assume aces 
# are worth 1.

card_one = card_value(input("\nWhat's your first card? ").upper())
card_two = card_value(input("\nWhat's your second card? ").upper())
card_three = card_value(input("\nWhat's your third card? ").upper())
# print(card_one)   #test
# print(type(card_one))

hand_total = card_one + card_two + card_three
if hand_total < 17:
    print(f'\nYour holding {hand_total}, you should hit.')
elif 17 <= hand_total < 21:
    print(f'\nYour holding {hand_total}, you should stay')
elif hand_total == 21:
    print(f'\nYou have {hand_total}. Blackjack!')
else:
    print(f'\nAlready Busted with {hand_total}')
