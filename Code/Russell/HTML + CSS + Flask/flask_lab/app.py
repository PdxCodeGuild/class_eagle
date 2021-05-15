from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    print(request.form['uncoded_text'])
    return render_template('index.html')

app.run(debug=True)



