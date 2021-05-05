def madLib():
    noun = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter a 3rd noun: ")
    occupation = input("Enter an occupation: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    verb2 = input("Enter a verb ending in 'ed': ")
    verb3 = input("Enter a verb ending in 'ing': ")
    noun4 = input("Enter a 4th noun: ")
    noun5 = input("Enter a plural noun: ")
    noun6 = input("Enter a 5th noun: ")
    emotion = input("Enter an emotion: ")

    output = f'It was during the battle of {noun} when I was running through a {noun2} when a {noun3} went off right next to my platoon. Our {occupation} yelled for us to {verb} to the nearest {place} we could find. When we got to the {place} we {verb2} to start a fire. As we were starting the fire, the enemy saw the {noun4} from the fireand started {verb3} {noun5}! We all quickly ducked behind the {noun6} at the {place} and returned fire. We quickly eliminated the enemy and were {emotion} that we had won the battle!'
    print(output)

def goAgain():
    repeatIn = input("Go Again? (y/n): ")
    if(repeatIn == 'y' or repeatIn == 'Y'):
        return True
    else:
        return False

madLib()

while goAgain() == True:
    madLib()