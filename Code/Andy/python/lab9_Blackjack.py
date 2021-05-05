
# Function that gets 'score' based on user inputs for cards
def get_total():
    cards = { 'A' : 1, '2' : 2, '3' : 3,  '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9,  '10' : 10,  'J' : 10, 'Q' : 10, 'K' : 10 }

    card_1 = input('What is your first card? ')
    card_2 = input('What is your second card? ')
    card_3 = input('What is your third card? ')

    total = cards[card_1] + cards[card_2] + cards[card_3]
    return total


# based on the users 'score' advice is given
def get_advice(tot):
    total = tot
    if total < 17:
        print(f'{total} Hit')
    elif total >= 17 and total < 21:
        print(f'{total} Stay')
    elif total == 21:
        print(f'{total} Blackjack!')
    elif total > 21:
        print(f'{total} Already Busted')



get_advice(get_total())
