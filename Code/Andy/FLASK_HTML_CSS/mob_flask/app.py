import random
import string


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password_length = int(request.form['input_text'])
        print(password_length)

        # Setting chars as upper and lowercase letters and punctuation characters
        chars = string.ascii_letters + string.digits + string.punctuation


        # Looping to add random characters to a list until input number is met
        i = 0
        password = []
        while i < password_length:
            password.append(random.choice(chars))
            i += 1
            # once number of characters is met, turn list into a string and print to console
            if i == password_length:
                password = ''.join(password)
            

        return render_template('flask_mob.html', message=password)

    else:       
        return render_template('flask_mob.html', message='hello')




app.run(debug=True)