import string

list_alpha=string.ascii_lowercase

def rot13(text,int):
    ...

    # method 1
    # have one strings - the original 
    alpha_list=string.ascii_lowercase
    
    # start output as a blank string
    output = ''
    # iterate over the characters in the input string
    
    for i in user_string:
        j = alpha_list.find(i)
         
        if j+cipher_twist >=  len(alpha_list):
            j = j + cipher_twist - len(alpha_list)
            output += alpha_list[j]
            
        # use subtraction or modulus to keep the index in a valid range
        else:
            j += cipher_twist
            output += alpha_list[j]
            
                    
    return output
    # method 2

user_string = input ("pick a word to cipher ")
cipher_twist = int(input ("how many clicks, shall we twist? "))
print(rot13(user_string,cipher_twist))