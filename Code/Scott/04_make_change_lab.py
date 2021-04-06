coin_dict = { # Dictionary of all US bills and coins (in cents)
    '$100 bill': 10000,
    '$50 bill': 5000,
    '$20 bill': 2000,
    '$10 bill': 1000,
    '$5 bill': 500,
    '$1 bill': 100,
    'half-dollar': 50,
    'quarter': 25,
    'dime': 10,
    'nickel': 5,
    'penny': 1
}

user_in = input('enter a dollar amount: ') #prompt user input
user_in = float(user_in) * 100 # convert to cents and convert user_input into float from string
user_in = int(user_in) #convert the float to an int now that we're in cents (no need for the .0 at the end)

print('=================') 
for key in coin_dict: #iterate through every type of bill & coin
    sum_left = user_in // coin_dict[key] #take the value and floor divide to the largest bill
    
    if  sum_left != 0: #don't print anything if there's none of that coin / bill...
        print(str(sum_left) + ' | ' + key + '\n-----------------') #otherwise, print this bill onto the next line, the amount of these bills (sum_left), and the name of this bill (key)

    user_in -= sum_left * coin_dict[key] #subtract out the amount we just calculated (value of bill * # of bills)-> move to the next smallest bill on next iteration
