import string
from django.shortcuts import render
from django.http import HttpResponse


def rot13(text, rot):
    rotation = rot  # amount of rotation to be used in encryption
    alphabet = string.ascii_lowercase   # have one string - the alphabet
    output = ''     # start output as a blank string

    for char in text:   # iterate over the characters in the input string
        if char == ' ':     # for handling spaces
            output += ' '
            continue
        elif char in string.punctuation:     # for handling punctuation
            output += char
            continue

        # find the index of the character in the alphabet
        abc_char_index = alphabet.find(char)
        rot_char_index = abc_char_index + rotation      # add 13 to the index

        # use subtraction or modulus to keep the index in a valid range
        if rot_char_index >= len(alphabet):
            rot_char_index = rot_char_index - len(alphabet)
            # get the letter in the alphabet at that new index
            rot_char = alphabet[rot_char_index]
            output += rot_char  # add the rotated character to your output
        else:
            rot_char = alphabet[rot_char_index]
            output += rot_char

    return output   # return your output


def index(request):
    print(request.method)
    print(request.POST)
    if request.method == 'POST':
        rot_num = int(request.POST['rot_num'])
        input_text = request.POST['input_text'].lower()
        rot_text = rot13(input_text, rot_num)
        context = {
            'title': 'ROT Cipher',
            'input_text': input_text,
            'rot_text': rot_text,
        }
        return render(request, 'rotcipherapp/index.html', context)

    else:
        context = {
            'title': 'ROT Cipher'
        }
        return render(request, 'rotcipherapp/index.html', context)
