'''
Lab 12: Unit Converter

Write a program that allows the user to convert a number between units.

Version 3

Ask user for the unit and distance and convert them to meters. Allow for inches, 
feet, yards, miles, meters, and kilometers.

Version 4
Ask the user for the starting unit, the distance, and the unit to convert to.
'''

# write a function that takes a given unit and distance and converts it to meters
def convert_to_meters(stat_unit, end_unit, distance):
    #   dictionary of units and their conversion factor for meters
    units = {'inches': .0254, 'feet': .3048, 'yards': .9144,
             'meters': 1, 'miles': 1609.34, 'kilometers': 1000}
    unit_to_meters = distance*units[start_unit]
    meters_to_unit = unit_to_meters/units[end_unit]
    output = meters_to_unit
    return round(output, 4)


# write a funtion to check if input is valid
def interpret_input(unit):
    output = ''
    valid_units = {
        'inches': ['in', 'inch', 'inches'], 
        'feet': ['ft', 'foot', 'feet'], 
        'yards': ['yd', 'yard', 'yards'], 
        'meters': ['m', 'meter', 'meters'], 
        'miles': ['mi', 'mile', 'miles'], 
        'kilometers': ['km', 'kilometer', 'kilometers']}
    for key in valid_units:     # problem
        for value in valid_units[key]:
            if unit == value:
                output = key[0]
            else:
                output = 'invalid'
    return output

while True:
    output = 0
    start_unit = input('\nWhat is the starting unit of distance? ').lower()
    distance = float(input('\nWhat is the distance? '))
    end_unit = input('\nWhat unit of distance would you like to convert to? ').lower()
    # if interpret_input(start_unit) == 'invalid':
    #     print(f'\n{start_unit} is not a valid unit')
    #     continue
    # elif interpret_input(end_unit) == 'invalid':
    #     print(f'\n{end_unit} is not a vailid unit')
    #     continue

    # convert the starting unit and distance into meters, then the distance in meters to the end unit
    # converted_distance = convert_meters(end_unit, (convert_to_meters(start_unit, distance)))
    converted_distance = convert_to_meters(start_unit, end_unit, distance)
    output = f'\n{distance} {start_unit} is {converted_distance} {end_unit}'

    print(output)
