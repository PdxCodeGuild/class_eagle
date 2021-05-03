import requests as req
from datetime import datetime
import re
import math

#Get the plain-text table of rain water accumulation at the Wilson HS station
response =  req.get('https://or.water.usgs.gov/non-usgs/bes/wilson.rain')
response_text = response.text

def get_dates(text_in): # A function that takes in the plain-text table and finds the dates and converts them to datetime
    regex = r'\d+-\w+-\d+'
    date_format = r'%d-%b-%Y'
    output = []

    results = re.findall(regex, text_in)

    for result in results:
        output.append(datetime.strptime(result, date_format))

    return output

def get_totals(text_in): #function that takes in the plain-text table and returns the daily accumalution
    regex = r'(\d+-\w+-\d+\s+)(\d+)'
    output = []

    results = re.findall(regex, text_in)
    for result in results:
        output.append(int(result[1]))

    return output

def mean(a): # finds the mean of a given list of numbers
    total = 0
    
    for i in range(len(a)):
        total += a[i]

    return total / len(a)

def variance(a): # finds the variance of a given list of numbers
    avg = mean(a)
    total = 0

    for i in range(len(a)):
        total += (a[i] - avg)**2
    
    return total / len(a)

def standard_dev(a): # finds the standard deviation of a given list of numbers
    v = variance(a)
    return math.sqrt(v)

def find_day(a): #Finds the day where that much rain occured a nd returns the date
    total_ind = totals_list.index(a)
    return dates_list[total_ind-1]

dates_list = get_dates(response_text)
totals_list = get_totals(response_text)

# print(dates_list)
# print(totals_list)
print(f'''
The rain accumulation data from {dates_list[-1]} to {dates_list[0]} for the Wilson HS weather station:
    Daily Average: {mean(totals_list)}
    Daily Variance: {variance(totals_list)}
    Daily Standard Deviation: {standard_dev(totals_list)}
    Rainiest Day: {max(totals_list) / 100 }" of rain, which occured on {find_day(max(totals_list))}
''')