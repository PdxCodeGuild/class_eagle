import random as rand

upper_count = int(input('How many uppercase letters would you like? '))
lower_count = int(input('How many lowercase letters would you like? '))
num_count = int(input('How many numbers would you like? '))
special_count = int(input('How many special characters would you like? '))


output = ''

while upper_count > 0 or lower_count > 0 or num_count > 0 or special_count > 0: #Keep going until the 'quota' for each type of character is filled
    rand_chr_val = rand.randint(33, 126) #generate a random integer [33, 126]
    
    if rand_chr_val <= 90 and rand_chr_val >= 65:  #if that number is 65 <= x <= 90 then it's uppercase
        if upper_count > 0: #double checked we haven't hit our max
            upper_count -= 1 #if we haven't hit our max, subtract one from the 'quota'
            output += chr(rand_chr_val) #And convert it from int to the corresponding unicode char, ALSO, add it onto the output of what we already have
    elif rand_chr_val <= 122 and rand_chr_val >= 97:  #if that number is 97 <= x <= 122 then it's lowercase
        if lower_count > 0:
            lower_count -= 1
            output += chr(rand_chr_val)
    elif rand_chr_val <= 57 and rand_chr_val >= 48:  #if that number is 48 <= x <= 57 then it's a number
        if num_count > 0:
            num_count -= 1
            output += chr(rand_chr_val)
    else:  #All other cases (for the given range [33, 126]), it's a special character
        if special_count > 0:
            special_count -= 1
            output += chr(rand_chr_val)

    # Debug statement!

    # print(f'''
    #     ============================
    #     Generated: {rand_chr_val} Corresponds to: {chr(rand_chr_val)}
    #     Uppercase left: {upper_count}
    #     Lowercase left: {lower_count}
    #     Numerical left: {num_count}
    #     Special C left: {special_count}
    #     ----------------------------
    #     Password so far: {output}
    #     ============================
    #         ''')


print(f'Your password is: {output}')