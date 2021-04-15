'''
Lab 11: Rot Cipher
Write a program that prompts the user for a string, and encodes it with ROT13. 
For each character, find the corresponding character, add it to an output 
string. Notice that there are 26 letters in the English language, so encryption 
is the same as decryption.
'''


import string


# method 2
def rot13(text, rot):
    rotation = rot  # amount of rotation to be used in encryption
    alphabet = string.ascii_lowercase   # have one string - the alphabet
    output = ''     # start output as a blank string

    for char in text:   # iterate over the characters in the input string
        if char == ' ':     # for handling spaces
            output += ' '
            continue
        abc_char_index = alphabet.find(char)    # find the index of the character in the alphabet
        rot_char_index = abc_char_index + rotation      # add 13 to the index
        if rot_char_index >= len(alphabet):     # use subtraction or modulus to keep the index in a valid range
            rot_char_index = rot_char_index - len(alphabet)
            rot_char = alphabet[rot_char_index]     # get the letter in the alphabet at that new index
            output += rot_char  # add the rotated character to your output 
        else:
            rot_char = alphabet[rot_char_index]
            output += rot_char

    return output   # return your output


user_text = input('Enter the message you\'d like encoded: ').lower()
user_rot = int(input('Enter amount the amount of rotation for encryption: '))
# test
# user_text = 'abcdefghijklmnopqrstuvwxyz'
# user_rot = 1

print(rot13(user_text, user_rot))

'''
alternative methods to try: 

# method 1
# have two strings - the original and rotated alphabet
# start output as a blank string
# iterate over the characters in the input string
    # find the index of the character in the alphabet
    # https://github.com/PdxCodeGuild/class_eagle/blob/main/1%20Python/docs/08%20Strings.md#find-afindb
    # use that index to find the corresponding character in the rotated alphabet
    # add the rotated character to your output
# return your output

# method 3
# make a dictionary where the keys are the original letters
# and the values are the rotated letters

# method 4
# use ord to find the ascii code of a letter
# add 13 to the ascii code
# do some arithmetic to put the ascii code in a valid range
# use chr to turn the ascii code into a character
# https://github.com/PdxCodeGuild/class_eagle/blob/main/1%20Python/docs/08%20Strings.md#ascii-codes-ord-and-chr


'''