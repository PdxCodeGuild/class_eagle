from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        unit_values = {
            "ft": 0.3048,
            "m": 1,
            "mi": 1609.34,
            "NM": 1852,
            "km": 1000,
            "yd": 0.9144,
            "in": 0.0254,
            "cm": 0.01,
            "mm": 0.001
        }
        starting_unit = request.form['from']
        ending_unit = request.form['to']
        distance = int(request.form['distance'])

        # converting original unit to meters
        meters = distance * unit_values[starting_unit]
        # using the previous result to convert to our new unit
        output = meters / unit_values[ending_unit]
        return render_template('index.html', output=output, ending_unit=ending_unit)
    else:
        return render_template("index.html")

app.run(debug=True)
