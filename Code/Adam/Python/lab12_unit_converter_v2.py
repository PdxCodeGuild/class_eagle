'''
Lab 12: Unit Converter
Write a program that allows the user to convert a number between units.

Version 2 
Allow the user to also enter the units. Then depending on the units, convert 
the distance into meters. The units we'll allow are feet, miles, meters, and 
kilometers.
'''

# write a function that takes a given unit and distance and converts it to meters
def convert_to_meters(unit, distance):
    #   dictionary of units and their conversion factor for meters
    units = {'feet': .3048, 'miles': 1609.34, 'meters': 1, 'kilometers': 1000 }
    output = distance*units[unit] # convert distance to metes and assign to output
    return round(output, 4)

# have user enter starting unit and distance
user_unit = input('What is the starting unit; feet, miles, meters, kilometers? ').lower()
user_distance = float(input('What is the distance? '))
conversion = convert_to_meters(user_unit, user_distance)

print(f'{user_distance} {user_unit} is {conversion} meters')



# test
# print(convert_to_meters('foot', 1)) # 0.3048
# print(convert_to_meters('mile', 1)) # 1609.34
# print(convert_to_meters('meter', 1))    # 1
# print(convert_to_meters('kilometer', 1))    # 1000
