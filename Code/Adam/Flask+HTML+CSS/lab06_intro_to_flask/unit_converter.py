

from flask import Flask, render_template, request
app = Flask(__name__)

# # function that return distance with a single or plural unit of measurement
def compose_unit(unit, num):
    num = float(num)
    output = ''
    singular = 1
    valid_units = {
        'in': ['in', 'inch', 'inches'],
        'ft': ['ft', 'foot', 'feet'],
        'yd': ['yd', 'yard', 'yards'],
        'm': ['m', 'meter', 'meters'],
        'mi': ['mi', 'mile', 'miles'],
        'km': ['km', 'kilometer', 'kilometers']
    }
    if num == singular:
        output = f'{num} {valid_units[unit][1]}'
    else:
        output = f'{num} {valid_units[unit][2]}'

    return output

def convert_unit(start_unit, end_unit, distance):
    #   dictionary of units and their conversion factor for meters
    units = {
        'in': .0254,
        'ft': .3048,
        'yd': .9144,
        'm': 1,
        'mi': 1609.34,
        'km': 1000
    }
    unit_to_meters = distance*units[start_unit]
    meters_to_unit = unit_to_meters/units[end_unit]
    output = meters_to_unit
    return round(output, 4)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_unit = request.form['start_unit'].lower()
        distance = float(request.form['distance'])
        end_unit = request.form['end_unit'].lower()
        output = ''

        converted_distance = round(convert_unit(start_unit, end_unit, distance), 2)
        output = f'\n{distance} {start_unit} converts to {converted_distance} {end_unit}'
        # output = f'{compose_unit(start_unit, distance)} = {compose_unit(end_unit, converted_distance)}'

        return render_template('unit_converter.html', message=output)
    
    else:

        return render_template('unit_converter.html', message='')
    
app.run(debug=True)
