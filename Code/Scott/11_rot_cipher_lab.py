def rot_word(n, text):
    # Break the input word into individual characters
    # Turn into ASCII vals
    ascii_list = []
    for char in text:
        ascii_list.append(ord(char))


    # Add n number of rotations to each character
    rot_list = ascii_list
    for i in range(len(rot_list)):
        # check to see if in alphabet
        if rot_list[i] <= ord('z') and rot_list[i] >= ord('a'):
            # If n number of rotations creates a character too large, 
            if rot_list[i] + n > ord('z'):
                # then go to start and keep adding
                rot_list[i] += n
                rot_list[i] -= ord('z')
                rot_list[i] += ord('a') - 1

            else:
                rot_list[i] += n

        rot_list[i] = chr(rot_list[i])

    # Recombine string
    output_str = ''.join(rot_list)
    # Return recombined string
    return output_str

user_in = input('Enter text to be encrypted: ').lower()
user_rot_val = int(input('How far rotated should it be?: '))
print(user_in)
print(rot_word(user_rot_val, user_in))
