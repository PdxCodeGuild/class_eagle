# 0 zero
# 1 one
# 2 two
# 3 three
# 4 four
# 5 five
# 6 six
# 7 seven
# 8 eight
# 9 nine
# 10 ten
# 11 eleven
# 12 twelve
# 13 thirteen
# 14 fourteen
# 15 fifteen
# 16 sixteen
# 17 seventeen
# 18 eighteen
# 19 nineteen
# 20 twenty
# 21 twenty-one
# 22 twenty-two

less_19_dic = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen"
    
}
over_19_dic  = {
    2 : "twenty",
    3 : "thirty",
    4 : "fourty",
    5 : "fifty",
    6 : "sixty",
    7 : "seventy",
    8 : "eighty",
    9 : "ninety"
}
def turn_string(num):

    if num < 20:
        output= less_19_dic[num]
        return output
    
    else: 
        ones_digit = num % 10
        tens_digit = num // 10 
        if ones_digit == 0:
            output = over_19_dic[tens_digit]
        else:
            output = over_19_dic[tens_digit] + "-" + less_19_dic[ones_digit]
        return output  


for i in range(100):
    print(i, turn_string(i))