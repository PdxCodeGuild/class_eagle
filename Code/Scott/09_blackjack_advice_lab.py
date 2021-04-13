# Versions & Improvments
# - Rather than assume aces as 1s, judge if they should be treated as 11s or 1s
# - use functions
# - implement a REPL for valid inputs

# Create a dictionary of the card type inputted -> and the corresponding blackjack points
cardDict = {'A': 1, 
'2' : 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
'J': 10, 'Q': 10, 'K': 10}

# Get input from user
user_input = ['', '', '']

print('Welcome to BlackJack Advisoer 3000, tell me your hand!')
print('Valid inputs: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K')
for i in range(3):
    user_input[i] = input(f'What is card {i+1}\'s value? ').upper()

# Create users score from their input
hand_val = 0

for card in user_input:
    hand_val += cardDict[card]

# Using an if-else block, offer them advice
if hand_val < 17:
    print(f'{hand_val} Hit')
elif hand_val >= 17 and hand_val < 21:
    print(f'{hand_val} Stay')
elif hand_val == 21:
    print(f'{hand_val} Blackjack!')
else:
    print(f'{hand_val} Already Busted :(')
