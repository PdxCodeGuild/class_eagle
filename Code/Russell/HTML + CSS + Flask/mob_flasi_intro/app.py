from flask import Flask, render_template, request 
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        password_length = request.form['password_length']
        password_length = int(password_length)
        print(password_length)
        password = ''
        for i in range(password_length):
            characters = string.ascii_letters + string.digits + string.punctuation
            password += random.choice(characters)
        return render_template('index.html', password = password)
    else:
        return render_template('index.html')



app.run(debug=True)

