import random
import string


from flask import Flask, render_template, request
app = Flask(__name__)

def random_uppercase_chars(n_uppercase):
    uppercase_chars = ''
    i = 0
    while i < n_uppercase:
        uppercase_chars += random.choice(string.ascii_uppercase)
        i += 1
    return uppercase_chars

def random_lowercase_chars(n_lowercase):
    lowercase_chars = ''
    i = 0
    while i < n_lowercase:
        lowercase_chars += random.choice(string.ascii_lowercase)
        i += 1
    return lowercase_chars

def random_digits(n_digits):
    digits = ''
    i = 0
    while i < n_digits:
        digits += random.choice(string.digits)
        i += 1
    return digits

def random_punctuation(n_punctuation):
    punctuation = ''
    i = 0
    while i < n_punctuation:
        punctuation += random.choice(string.punctuation)
        i += 1
    return punctuation

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # password_length = int(request.form['input_text'])
        num_upper = int(request.form['upper_letters'])
        num_lower = int(request.form['lower_letters'])
        special_chars = int(request.form['special_chars'])
        numbers = int(request.form['numbers'])

        # Setting chars as upper and lowercase letters and punctuation characters
        chars = string.ascii_letters + string.digits + string.punctuation

        # Looping to add random characters to a list until input number is met
        i = 0
        password = []
        uppercase_chars = random_uppercase_chars(num_upper)
        lowercase_chars = random_lowercase_chars(num_lower)
        digits = random_digits(numbers)
        punctuation = random_punctuation(special_chars)


        password.append(uppercase_chars)
        password.append(lowercase_chars)
        password.append(digits)
        password.append(punctuation)
        password = ''.join(password)
        password = password.split()
        random.shuffle(password)
        password = ''.join(password)

        

        # while i < password_length:
        #     password.append(random.choice(chars))
        #     i += 1
        #     # once number of characters is met, turn list into a string and print to console
        #     if i == password_length:
        #         password = ''.join(password)
            

        return render_template('flask_mob.html', message=password)

    else:       
        return render_template('flask_mob.html', message='hello')




app.run(debug=True)