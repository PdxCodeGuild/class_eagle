
cards = { 'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,  'K': 10}


card_1 = cards[input("What is your first card?")]

card_2 = cards[input("what is your second card?")]

card_3 = cards[input("what is your third card?")]

total = card_1 + card_2 + card_3

print(f"Your at {total}")

if total < 17:
    print('Hit')
elif total >= 17 and total < 21:
    print('Stay')
elif total == 21:
    print('Blackjack!')
else:
    print('Your busted, partner!')

