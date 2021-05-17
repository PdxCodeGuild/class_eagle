from flask import Flask,render_template,request
import string

alph_1 = string.ascii_lowercase

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        word = request.form['uncoded_text']
        enc_word = []
        offset = 3
        for char in word:
            enc_word.append(alph_1.find(char) + offset)

        for i in range(len(enc_word)):
            if enc_word[i] >= len(alph_1):
                enc_word[i] = enc_word[i] - len(alph_1)

        code_word = ''
        for i in enc_word:
            code_word += alph_1[i]

        print(code_word)

        return render_template('index.html', code_word = code_word)
    else:
        return render_template('index.html')



app.run(debug=True)



