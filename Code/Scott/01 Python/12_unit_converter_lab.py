# This is the ratio of 1 ft -> x unit, allowing us to use ft as a universal measuring unit
ft_mult_dict = { # * = convert out of ft, / = converts into ft
    'mi' : 0.0001893939,
    'm' : 0.3048,
    'km' : 0.0003048,
    'yd' : 0.3333333333,
    'in' : 12,
    'ft' : 1
}

def convert(length, unit_in, unit_out):
    # Convert the input into ft
    in_ft = length / ft_mult_dict[unit_in]
    # Convert it out of ft for the output
    output = in_ft *  ft_mult_dict[unit_out]
    # Round the output to 10 decimal places to prevent floating integer error
    output = round(output, 10)
    return output


unit_in = input('Enter a unit of length (m, km, in, ft, yd, mi): ')
unit_out = input('Enter a unit to convert into: ')
user_in = input(f'Enter a length in {unit_in}: ')
print(f'{convert(float(user_in), unit_in, unit_out)} {unit_out}')