#Prompt the user for an amount of money.
money = float(input("How much you got?"))


def convert_to_coins(a):
    cents = a * 100
    quarters = (cents // 25)
    remain = cents % 25
    dimes = (remain // 10)
    remain_2 = remain % 10
    nickles = (remain_2 // 5)
    remain_3 = remain_2 / 1
    pennies = (remain_3 / 1)
    return quarters, dimes, nickles, pennies

quarters, dimes, nickles, pennies = convert_to_coins(money)
    
print(f"Ya got {quarters} quarters, {dimes} dimes, {nickles} nickles, {pennies} pennies")

  
