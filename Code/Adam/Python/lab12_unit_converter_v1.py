'''
Lab 12: Unit Converter

Write a program that allows the user to convert a number between units.

Version 1 - Ask the user for the number of feet, and print out the equivalent 
distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters 
by multiplying the input distance by 0.3048. Below is some sample input/output.
'''

def ft_to_m(ft):
    m = .3048
    output = ft*m
    return round(output, 4)


# ask the user for distance in feet
distance_in_ft = float(input('What is the distance in feet? '))
print(f'{distance_in_ft} ft is {ft_to_m(distance_in_ft)} m')
