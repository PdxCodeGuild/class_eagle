

while True:

    

    noun1 = input('Noun: ')
    noun2 = input('Noun: ') 
    noun3 = input('Noun: ')
    noun4 = input('Noun: ')
    noun5 = input('Noun: ')
    occupation = input('Occupation: ')
    verb = input('Verb: ')
    location = input('Location: ')
    verbed = input('Verb ending in "ed": ')
    verbing = input('Verb ending in "ing": ')
    plural_noun = input('Pural noun: ')
    emotion = input('Emotion: ')

    print(f'''
    It was during the battle of {noun1} when I was running through a {noun2} when a {noun3} went off right next to my platoon.
    Our {occupation} yelled for us to {verb} to the nearest {location} we could find.
    When we got to the {location} we {verbed} to start a fire.
    As we were starting the fire the enemy saw the {noun4} from the fire and started {verbing} {plural_noun} at us.
    We all quickly ducked behind the {noun5} at the {location} and returned fire.
    We quickly eliminated the enemy and were {emotion} that we had won the battle.
    ''')

    answer = input('''
    Would you like to go again?
    [yes/no]
    ''')
    if answer == 'yes':
        continue
    else:
        break

print('Thank you!')