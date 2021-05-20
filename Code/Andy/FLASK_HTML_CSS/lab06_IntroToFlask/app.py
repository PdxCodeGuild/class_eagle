from flask import Flask, render_template, request
import random
import string


def rot(text, rot_num):
    new_word = []
    for letter in text:
        new_let = int(ord(letter))
        rot_num = int(rot_num)
        new_let += rot_num
        if new_let <= 122:  # 122 is the ascii value for z
            new_let = chr(new_let)
            new_word.append(new_let)
        else:
            # if the ascii value goes past z, we subtract 26 so that we stay within the alphabet.
            new_let -= 26
            new_let = chr(new_let)
            new_word.append(new_let)
    new_new = ''.join(new_word)
    return new_new


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        word = request.form['input_text']
        rotate = int(request.form['input_rot'])
        new = rot(word,rotate)
        return render_template('flask_mob.html', message=new)

    else:
        return render_template('flask_mob.html', message='')



app.run(debug=True)
