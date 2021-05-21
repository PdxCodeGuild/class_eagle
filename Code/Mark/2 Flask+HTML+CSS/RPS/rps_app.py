from flask import Flask, render_template, request
from random import *
app = Flask(__name__)

def rock_paper_scissors(user, computer):
        if user == computer:
            return 'tie'
        elif user == "rock":
            if computer == "paper":
                return 'lose'
            elif computer == "scissors":
                return 'win'
            elif computer == "spock":
                return 'lose'
            elif computer == "lizard":
                return 'win'
        elif user == "scissors":
            if computer == "rock":
                return 'lose'
            elif computer == "paper":
                return 'win'
            elif computer == "spock":
                return 'lose'
            elif computer == "lizard":
                return 'win'
        elif user == "paper":
            if computer == "rock":
                return 'win'
            elif computer == "scissors":
                return 'lose'
            elif computer == "spock":
                return 'win'
            elif computer == "lizard":
                return 'lose'
        elif user == "spock":
            if computer == "rock":
                return 'win'
            elif computer == "scissors":
                return 'win'
            elif computer == "paper":
                return 'lose'
            elif computer == "lizard":
                return 'lose'
        elif user == 'lizard':
            if computer == "rock":
                return 'lose'
            elif computer == "scissors":
                return 'lose'
            elif computer == "paper":
                return 'win'
            elif computer == "spock":
                return 'win'



@app.route('/', methods=['GET', 'POST'])
def index():
   

    if request.method == 'POST':
        rps = ['rock', 'paper', 'scissors', 'spock', 'lizard']
        computer_choice = choice(rps)
        user_choice = request.form['user_choice']
        result = rock_paper_scissors(user_choice, computer_choice)
        return render_template('rps.html', user_choice=user_choice, computer_choice=computer_choice, result=result)

    else:   
        return render_template('rps.html')

app.run(debug=True)