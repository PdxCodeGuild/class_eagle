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


def convert_to_meters(start_unit, end_unit, distance):
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


# write a funtion for input validation
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

# # test interpret_input()
# unit = 'feet'
# print(interpret_input(unit))

output = 0


while True:     # need a condition that breaks this loop
    # user enters a start unit; the string is converted to lowercase
    start_unit = input('\nEnter a starting unit of distance? ').lower() 
    if interpret_input(start_unit) == 'invalid':    # if interpret_input returns the string 'invalid'
        print(f'\n{start_unit} is not a valid unit')    # the user is notified
        continue    # the loops starts over

    # user enters a distance
    distance = float(input('\nWhat is the distance? '))
    # validate this input by:
    # check if distance is a digit
    # if the user is notified
    # the loop starts over

    # user enters an end unit; the string is converted to lowercase
    end_unit = input('\nWhat unit of distance would you like to convert to? ').lower()   
    if interpret_input(end_unit) == 'invalid':      # if interpret_input returns the string 'invalid'
        print(f'\n{end_unit} is not a vailid unit')     # the user is notified
        continue     # the loops starts over

    converted_distance = convert_to_meters(interpret_input(start_unit), interpret_input(end_unit), distance)
    output = f'\n{distance} {interpret_input(start_unit)} is {converted_distance} {interpret_input(end_unit)}'

    print(output)
