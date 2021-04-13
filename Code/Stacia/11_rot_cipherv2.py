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
    
    for i in range(len(user_string)):
        j = alpha_list.find(user_string[i])
         
        if j+cipher_twist >= len(list_alpha):
            j %= len(alpha_list)
            print (j)
            output += alpha_list[j]
            i += 1
        # use subtraction or modulus to keep the index in a valid range
        else:
            j += cipher_twist
            output += alpha_list[j]
            i += 1
                    
    return output,0
    # method 2

    
        # use subtraction or modulus to keep the index in a valid range
        # get the letter in the alphabet at that new index
    # add the rotated character to your output
  

user_string = input ("pick a word to cipher")
cipher_twist = int(input ("how many clicks, shall we twist?"))
print(rot13(user_string,cipher_twist)) # uryyb