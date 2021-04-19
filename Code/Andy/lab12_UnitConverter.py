

'''****************************************** Unit Converter ********************************************''' 

# improvements - put inside REPL


def unit_converter():
    conversions = {

    "ft" : 3.048,
    "mi" : 16093.4,
    "m" : 10,
    "km" : 10000,
    "yard" : 9.144,
    "inch" : 0.254,

    }

    # Asking for user inputs
    input_unit = input('What unit are you converting from? (ft, mi, m, km, yard, or inch) ')
    distance = float(input('What is the distance? '))
    output_unit = input('What unit do you want to convert to? (ft, mi, m, km, yard, or inch) ')


    #output_name is for better readibility on output
    output_name = output_unit 
    input_name = input_unit

    # math : converts user inputs to meters, then converts meters to final output
    input_unit = conversions.get(input_unit)
    meters = distance * input_unit
    output_unit = conversions.get(output_unit)
    final = meters / output_unit

    print(f' {distance} {input_name} = {final} {output_name}')


unit_converter()







