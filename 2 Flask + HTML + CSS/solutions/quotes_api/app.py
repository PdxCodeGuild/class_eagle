
import requests
import json

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/qotd/')
def qotd():
    response = requests.get('https://favqs.com/api/qotd')
    data = response.json()
    print(data)
    author = data['quote']['author']
    quote = data['quote']['body']
    return render_template('index.html', author=author, quote=quote)


@app.route('/search/', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        search_term = request.form['search_term']
        search_page = request.form['search_page']
        print(request.method)
        print(request.form)
        params = {
            'filter': search_term,
            'page': search_page
        }
        headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
        response = requests.get('https://favqs.com/api/quotes', params=params, headers=headers)
        data = response.json()
        print(json.dumps(data, indent=4))
        return render_template('search.html', data=data)


app.run(debug=True)

