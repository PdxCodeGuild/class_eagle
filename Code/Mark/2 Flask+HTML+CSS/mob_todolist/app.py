from flask import Flask, render_template, request
from jsondb import JsonDB

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print(request.form)
    # if request.method == 'GET':
    db = JsonDB()
    db.load()
    print(request.form)
    if request.method == 'POST':
        db['todos'].append({
            'text': request.form['text'],
            'priority': request.form['priority']
        })
        db.save()

    return render_template("index.html", todo=db['todos'])

app.run(debug=True)