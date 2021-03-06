# importing multiple libraries
import requests
import re
from datetime import datetime
import math
import matplotlib.pyplot as plt
from os import *
from colorama import Fore, Back, Style



# using the regex to find the specific data needed
regex = r'(\d{2}-\w{3}-\d{4})(\s+)(\d+)'
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
response = response.text
results = re.finditer(regex, response)

# turn a string into a datetime object
# date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')

# this function extracts the dates and rain totals from the response
def get_data(data):
    rain_data = []
    index = 0
    for match in data:
        index += 1
        date = datetime.strptime(match.group(1), '%d-%b-%Y')
        rain_data.append({'Date': date, 'Total': int(match.group(3))})
    return rain_data


# This function gets the average rainfall from the data
def get_average(data):
    totals = []
    for i in range(len(data)):
        totals.append(data[i]['Total'])
        mean = (sum(totals)/len(totals))
    return mean

# Using the average, this function calculates the variance
def get_variance(data, mean):
    var = 0
    for i in range(len(data)):
        var += (data[i]['Total'] - mean)**2
    return var / len(data)


# this function will obtain the max rainfall and its date
def get_max_rainfall(data):
    highest_rain = 0
    date_hr = ''
    for i in range(len(data)):
        if data[i]['Total'] > highest_rain:
            highest_rain = (data[i]['Total'])
            date_hr = data[i]['Date']
    return f'The date of highest rainfall for the selected region was on {date_hr} with {highest_rain} tips.'

# This function takes the data and plots it in a simple graphic
def plot_data(data):
    x_values = []
    y_values = []
    for i in range(len(data)):
        x_values.append(data[i]['Date'])
        y_values.append(data[i]['Total'])
    plt.bar(x_values,y_values)
    plt.show()

# obtaining the data from the functions
rain_data = get_data(results)
mean = get_average(rain_data)
var = get_variance(rain_data, mean)
std = math.sqrt(var)
max_rain = get_max_rainfall(rain_data)

system('cls') # clearing the screen of previous data

# displaying the information to the user
print(Fore.LIGHTGREEN_EX+Back.LIGHTRED_EX+f'''
----------------------------------------------------------------------------------------------
The average rainfall for the region is {round(mean,1)} tips.                                
The variance is {round(var,1)} tips.                                                      
The standard deviation is {round(std,1)} tips.                                            
----------------------------------------------------------------------------------------------
{max_rain}
''')
print(Style.RESET_ALL)
plot_data(rain_data)







