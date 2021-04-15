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


def convert_to_meters(unit, distance):
    #   dictionary of units and their conversion factor for meters
    units = {'inches': .0254, 'feet': .3048, 'yards': .9144,
             'meters': 1, 'miles': 1609.34, 'kilometers': 1000}
    # convert distance to metes and assign to output
    output = distance*units[unit]
    return round(output, 4)

# write a function that converts a distance in meters to other units of distance
def convert_meters(unit, distance):
    units = {'inches': .0254, 'feet': .3048, 'yards': .9144,
             'meters': 1, 'miles': 1609.34, 'kilometers': 1000}
    output = distance/units[unit]
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
    for key in valid_units:
        for value in valid_units[key]:
            if unit == value:
                output = key[0]
            else:
                output = 'invalid unit'
    return output


# print(convert_meters('feet', 1)) # 1
output = 0
start_unit = input('\nWhat is the starting unit of distance? ').lower()
distance = float(input('\nWhat is the distance? '))
end_unit = input(
    '\nWhat unit of distance would you like to convert to? ').lower()

# convert the starting unit and distance into meters, then the distance in meters to the end unit
converted_distance = convert_meters(
    end_unit, (convert_to_meters(start_unit, distance)))
output = f'\n{distance} {start_unit} is {converted_distance} {end_unit}'

print(output)
