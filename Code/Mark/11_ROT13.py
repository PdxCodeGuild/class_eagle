from string import *


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



def encryptv2(num,text):
    char_list = list(text)
    letters = ascii_letters
    message = ""
    for i in range(0,len(char_list)):
        if char_list[i] == ' ':
            message += ' '
            continue
        x = letters.index(char_list[i])
        if x > 26:
            x -= num
            message += letters[x]
        elif x <= 25:
            x += num
            message += letters[x]
    return message



text = input('Enter your message: ')
num = int(input('Amount of rotation: '))


print(f'''
Your newly encrypted message is:
{encryptv2(num,text)}
{encrypt(text)}
''')



