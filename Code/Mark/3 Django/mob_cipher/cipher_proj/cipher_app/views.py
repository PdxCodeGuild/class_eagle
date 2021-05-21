from django.shortcuts import render
from django.http import HttpResponse
from string import *

def encryptv2(rotation,text):
    char_list = list(text)
    letters = ascii_letters
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


def index(request):
    if request.method == "POST":
        text = request.POST['text']
        rotation = int(request.POST['rotation'])
        secret_word = encryptv2(rotation, text)
        context = {
            'secret_word': secret_word
        }
        return render(request, 'cipher_app/index.html', context)
    else:
        context = {}
        return render(request, 'cipher_app/index.html', context)
