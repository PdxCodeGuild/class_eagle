import math



def make_change(coin_amount):
    
    coin_amount = math.ceil(user_m/.01)

    quart = coin_amount//25 # The amount of quarters
    coin_amount = coin_amount - (quart*25)

    dime = coin_amount//10 # The amount of dimes
    coin_amount = coin_amount - (dime*10)

    nick = coin_amount//5 # The amount of nickels
    coin_amount = coin_amount - (nick*5)
    
    pen = coin_amount//1 # The amount of pennies

    return print(f'''
    Your change is:
    {quart} quarters, {dime} dimes, {nick} nickels and {pen} pennies.
    ''')    

while True:
    user_m = float(input('Enter a dollar amount:'))

    make_change(user_m)

    answer = input('Would you like to enter another amount?[yes/no]')
    if answer == 'yes':
        continue
    else:
        break

print('Thank you')      
