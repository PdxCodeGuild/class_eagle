import random as rand

upper_count = int(input('How many uppercase letters would you like? '))
lower_count = int(input('How many lowercase letters would you like? '))
num_count = int(input('How many numbers would you like? '))
special_count = int(input('How many special characters would you like? '))


output = ''
pass_word = ''

while upper_count > 0 or lower_count > 0 or num_count > 0 or special_count > 0: #Keep going until the 'quota' for each type of character is filled
    rand_chr_val = rand.randint(ord('!'), ord('~')) # generate a random integer in range of [33, 126] on ASCII table
    
    if rand_chr_val <= ord('Z') and rand_chr_val >= ord('A'):  # if that int is in the range of the ASCII values of ['A','Z'], then it's uppercase type
        if upper_count > 0: # double checked we haven't hit our max
            upper_count -= 1 # if we haven't hit our max, subtract one from the 'quota'
            output += chr(rand_chr_val) # And convert it from int to the corresponding unicode char, ALSO, add it onto the output of what we already have
    elif rand_chr_val <= ord('z') and rand_chr_val >= ord('a'): # if that int is in the range of the ASCII values of ['a,'z'], then it's lowercase type
        if lower_count > 0:
            lower_count -= 1
            output += chr(rand_chr_val)
    elif rand_chr_val <= ord('9') and rand_chr_val >= ord('0'):  # if that int is in the range of the ASCII values of ['0','9'], then it's numerical type
        if num_count > 0:
            num_count -= 1
            output += chr(rand_chr_val)
    else:  # All other cases (for the given range [33, 126]), it's a special character
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

pass_word = list(output) # Turn output into a list
rand.shuffle(pass_word) # take list and shuffle it 
pass_word = ''.join(pass_word) # rejoin into one string

print(f'Your password is: {pass_word}')