

from flask import Flask, render_template, request
app = Flask(__name__)

# # function that return distance with a single or plural unit of measurement
# def compose_unit(unit, num):
#     num = float(num)
#     output=''
#     singular = 1
#     valid_units = {
#         'in': ['in', 'inch', 'inches'],
#         'ft': ['ft', 'foot', 'feet'],
#         'yd': ['yd', 'yard', 'yards'],
#         'm': ['m', 'meter', 'meters'],
#         'mi': ['mi', 'mile', 'miles'],
#         'km': ['km', 'kilometer', 'kilometers']
#     }
#     for key in valid_units:
#         if num == singular:
#             output = f'{num} {key[1]}'
#         else:
#             output = f'{num} {key[2]}'

#     return output


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


def interpret_input(unit):
    output = ''
    valid_units = {
        'in': ['in', 'inch', 'inches'],
        'ft': ['ft', 'foot', 'feet'],
        'yd': ['yd', 'yard', 'yards'],
        'm': ['m', 'meter', 'meters'],
        'mi': ['mi', 'mile', 'miles'],
        'km': ['km', 'kilometer', 'kilometers']
    }
    # if unit is one of the listed values return its key, else return the string 'invalid'
    for key in valid_units:
        if unit in valid_units[key]:
            output = key
            return output
        else:
            output = 'invalid'
    return output


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_unit = request.form['start_unit'].lower()
        distance = float(request.form['distance'])
        end_unit = request.form['end_unit'].lower()

        output = ''

        converted_distance = round(convert_unit(interpret_input(
            start_unit), interpret_input(end_unit), distance), 2)
        output = f'\n{distance} {interpret_input(start_unit)} converts to {converted_distance} {interpret_input(end_unit)}'
        # # function dissabled
        # output = f'{compose_unit(interpret_input(start_unit)), distance} = {compose_unit(interpret_input(end_unit)), converted_distance}'

        return render_template('unit_converter.html', message=output)
    else:
        return render_template('unit_converter.html', message='')


app.run(debug=True)
