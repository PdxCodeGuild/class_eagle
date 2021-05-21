
# Dictionary used for card values
cards = {
    'a': 1,
    'k': 10,
    'q': 10,
    'j': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

# dictionary used for advice responses
advice = {
    'stay':'Trust me! I would stay!',
    'hit':'You should definitly hit!',
    'blackjack':'Blackjack! Talk about luck!',
    'bust':'Bust! This game is totally rigged!'
}


# using the input as the key for the card dictionary
first_card = cards[(input('What is your first card? '))]
second_card = cards[(input('What is your second card? '))]
third_card = cards[(input('What is your third card? '))]



total = first_card+second_card+third_card


# printing the total for the user
print(total)

# if and elif to decide which advice to give
if total < 17:
    print(advice['hit'])
elif 17 <= total < 21:
    print(advice['stay'])
elif total == 21:
    print(advice['blackjack'])
elif total > 21:
    print(advice['bust'])




