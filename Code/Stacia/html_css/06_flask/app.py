import random
import string

from flask import Flask, render_template, request
app = Flask(__name__)





@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        lowercase = request.form['lowercase']
        lowercase = int(lowercase)
        uppercase = request.form["uppercase"]
        uppercase = int(uppercase)
        number = request.form["number"]
        number= int(number)
        symbol = request.form["symbol"]
        symbol = int(symbol)
        
        passw =[]
        password = ""
        symbol_list = ["!", "@", "#" "_"]
        for i in range(lowercase):
            passw.append(random.choice(string.ascii_lowercase))
        for i in range (uppercase):
            passw.append(random.choice(string.ascii_uppercase))
        for i in range (number):
            passw.append(random.randint(1,9))
        for i in range (symbol):
            passw.append(random.choice(symbol_list))
        random.shuffle(passw)
        for i in passw:
            password += str(i)
        print (password)
        return render_template('index.html', password = password)
    else:
        return render_template('index.html', password = " ( ͡° ͜ʖ ͡°) ?")


app.run(debug=True)
