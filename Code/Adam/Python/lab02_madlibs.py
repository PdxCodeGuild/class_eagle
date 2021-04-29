# lab 2 - Create a mad lib game


print('Let\'s play a Mad Libs')

adj1 = input('Please enter an adjective: ')

pl_noun = input('Enter a plural noun: ')

adj2 = input('Enter another adjective: ')

adj3 = input('Enter another adjective: ')

adj4 = input('Enter one more adjective: ')

mad_lib = f'Roses are {adj1} {pl_noun} are {adj2}. I\'m really {adj3} to have a {adj4} friend like you!'

print(mad_lib)


# Challenge:

# Write a funtion searches a string for most common verbs and adjectives
# and replaces them with {verb0 or adj0}, converts it to an f string for
# future concatenation. Return the string and a list of generated variables.

# Write a function that takes the list of generated variables and prompts 
# the user add their own verbs and adjectives.

# Then print the f string with the new verbs and adjectives.