
'''************************LAB 15 RAIN DATA***********************'''
# This code reads data from a given document, and returns calculated data.
# Possible improvements: better graph range, maybe let user pick date range?
# redo without using built in stats functions


import requests
import re
from datetime import datetime
from statistics import mean
from statistics import variance
from statistics import stdev
import matplotlib.pyplot as plt


# From data get dates
def get_first(data):
    return [item[0] for item in data]


# From data get rain totals
def get_second(data):
    return [item[1] for item in data]


# Function to get data, analyze, and output results
def analzye_data():


    # Getting Data table
    url = input('Enter PDX rain data url: ')
    response = requests.get(url)
    response.encoding = 'utf-8'
    text = response.text 
    text = str(text)


    # Using Regex to find dates, and total rain for the day
    reg = r'(\d{2}[-]\w{3}[-]\d{4})\s+(\d+)'
    rain_data = re.findall(reg, text)


    # Separating data into 2 lists
    dates = get_first(rain_data)
    rain_total = get_second(rain_data)


    # Convert to integers in order to do math
    rain_int = [int(x) for x in rain_total]


    # Creating a dictioanary from the two lists
    data_dict = dict(zip(dates, rain_int))


    # Finding mean rain, variance, standard deviation, and day with most rain
    mean_rain = mean(data_dict[num] for num in data_dict)
    variance_rain = variance(data_dict[num] for num in data_dict)
    deviation_rain = stdev(data_dict[num] for num in data_dict)
    highest_rain = max(data_dict, key=data_dict.get)
    highest_value = data_dict[highest_rain] # highest value for ease of use in output.


    # Output
    print('\nRain data is measured in tips, one tip is one hundredth of an inch. \n')
    print(f'From the given data, the mean rainfall is {mean_rain} tips,')
    print(f'the variance is {variance_rain} tips^2, \nthe standard deviation is {deviation_rain} tips')
    print(f'and the day with the most rain is {highest_rain} with {highest_value} tips of rain falling.')



# REPL
run_again = 'y'
while run_again == 'y':
    analzye_data()
    run_again = input('Run again? y/n ')
    if run_again != 'y':
        print('Goodbye! ')

