

def get_int(message):
    while True:
        x = input(message + ' ')
        if x.isdigit():
            x = int(x)
            return x
        else:
            print('please enter a valid integer')

