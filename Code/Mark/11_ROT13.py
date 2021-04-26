from string import *

# used this function to attempt the encryption with a dictionary
def encrypt(text):
    cypher = {
        'a':'n',
        'A':'N',
        'b':'o',
        'B':'O',
        'c':'p',
        'C':'P',
        'd':'q',
        'D':'Q',
        'e':'r',
        'E':'R',
        'f':'s',
        'F':'S',
        'g':'t',
        'G':'T',
        'h':'u',
        'H':'U',
        'i':'v',
        'I':'V',
        'j':'w',
        'J':'W',
        'k':'x',
        'K':'X',
        'l':'y',
        'L':'Y',
        'm':'z',
        'M':'Z',
        'n':'a',
        'N':'A',
        'o':'b',
        'O':'B',
        'p':'c',
        'P':'C',
        'q':'d',
        'Q':'D',
        'r':'e',
        'R':'E',
        's':'f',
        'S':'F',
        't':'g',
        'T':'G',
        'u':'h',
        'U':'H',
        'v':'i',
        'V':'I',
        'w':'j',
        'W':'J',
        'x':'k',
        'X':'K',
        'y':'l',
        'Y':'L',
        'z':'m',
        'Z':'M'
    }
    char_list = list(text)
    message = ''
    for i in range(len(char_list)):
        if char_list[i] == ' ':
            message += char_list[i]
        else:
            letter = cypher.get(char_list[i])
            message += letter
    return message


# using string methods to generate the alphabet 
def encryptv2(rotation,text):
    char_list = list(text)
    letters = ascii_lowercase
    message = ""
    # utilizing a for loop to iterate through each character
    for i in range(len(char_list)):
        # condition to check for spaces and add them to the message
        if char_list[i] == ' ':
            message += ' '
        else:
            # finding the index for the character and adding the rotation to it
            x = letters.index(char_list[i])
            x += rotation
            x %= len(letters)
            # adding the new character onto the message using the rotated index
            message += letters[x]
    return message



text = input('Enter your message: ')
text = text.lower()
rotation = int(input('Amount of rotation: '))


print(f'''
Your newly encrypted message is:
{encryptv2(rotation,text)}
{encrypt(text)}
''')



