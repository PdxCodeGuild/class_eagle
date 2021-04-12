#asks user for amount to be converted into change.
change = input ("How much change do you have?")
#converts change to a float and multiplies by 100 so we can work in pennys, the most basic unit of curancy. 
cents = float(change)*100
# finds how many dollars can be found in our total change pool and assigns it to a variable 
dollars = (cents //100)
# takes change after dollars removed by using modulous of 100 and stores it as a unique variable.
dchange = int(cents % 100)
#same process as beore, continues untill  we have only pennies. 
quarters = (dchange // 25)
qchange = int(dchange % 25)

dimes = qchange //10
dchange = int(qchange % 10)

nickles = dchange //5
penies = int(dchange % 5)

#prints out an f string that tells how much of each coin they have. 
print (f"You recive {dollars}  dollars {quarters} quarters {dimes} dimes {nickles} nickles and {penies} pennys. Sorry but half dollars are collector peices.")

 