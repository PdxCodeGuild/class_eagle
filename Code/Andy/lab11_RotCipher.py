# make the rotation random?


# Given text and requested rotation number, this function uses ord and chr to encode the message.
# ord and chr functions are used to find the ascii value of each letter and add the desired rotation

def rot(text, rot_num):
    new_word = []
    for letter in text:
        new_let = int(ord(letter))
        rot_num = int(rot_num)
        new_let += rot_num
        if new_let <= 122: # 122 is the ascii value for z  
            new_let = chr(new_let)
            new_word.append(new_let)
        else:
            new_let -= 26 # if the ascii value goes past z, we subtract 26 so that we stay within the alphabet.
            new_let = chr(new_let)
            new_word.append(new_let)
    new_new = ''.join(new_word)
    return new_new


# REPL with inputs requested to use 'rot' function
def run():
    run_again = 'y'
    while run_again == 'y':
        run_again = input('would you like to encode a word? y/n ')
        if run_again == 'y':
            word = input('Enter your word ')
            rotate = input('How much rotation? ')
            print(rot(word,rotate))
        else:
            print('Goodbye!')


run()


