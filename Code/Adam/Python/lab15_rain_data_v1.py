'''
Lab 15: Rain Data

The 'City of Portland Bureau of Environmental Services' operates and maintains 
a network of rain gauges around Portland, and publishes their data publicly at 
http://or.water.usgs.gov/non-usgs/bes/. 

Version 1 - Download or use requests to get one of these files. The two columns 
that are most important are the date and the daily total. The simplest 
representation of this data is a list of tuples, but you may also use a list of 
dictionaries, or a list of instances of a custom class.
'''

import requests
from datetime import datetime
import re
import statistics


response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
text = response.text

# write a function that returns a list of dictionaries
def get_dates_and_totals(text):
    dates_totals_dic = []
    # https://regex101.com/r/ELDlmL/1
    pertinent_data = r'(\d{2}[-]\w{3}[-]\d{4})\s+(\d+)'
    # capture group 1: date, capture group 2: rain_total
    result = re.findall(pertinent_data, text) # returns a list of dates and totals
    for i in range(len(result)):
        date = str(datetime.strptime(result[i][0], '%d-%b-%Y').date())
        if result[i][1] != '-':
            rain_total = int(result[i][1])
            dates_totals_dic.append({"date": date, "total": rain_total}) 
            # dates_totals_dic.append({date: rain_total}) # the date is the key and the rain total is its value
        else:
            continue
    return dates_totals_dic


'''
Version 2 - Calculate the mean, the variance, and find the day which had the most rain.
'''

# write a function that calculates and returns the mean
def calculate_mean(data):
    total = 0
    mean = 0
    for i in range(len(data)):
        total += data[i]['total']
    mean = total/len(data)  # The mean is the sum of all the daily totals divided by the number of daily totals.
    return mean


# write a function that calculates and returns the variance. Find the squared difference from the mean for each data value.
def calculate_variance(mean, data):
    sum_square_deviation = 0
    variance = 0
    for i in range(len(data)):
        # Subtract the mean from each data value and square the result.
        sum_square_deviation += (data[i]['total']-mean)**2      # Find the sum of all the squared differences.
    variance = sum_square_deviation/len(data)       # divide this result by the number of data values
    return variance


# write a function that returns the date with the most total rain
def most_daily_rain(data):
    date = ''   # set date to an empty string
    sorted_data = sorted(data, key=lambda k: k['total'])    # sorted data by it's 'total's
    date = sorted_data[-1]['date']      # set date to the last date in sorted_data
    return date

# assign function calls to variables
rain_data = get_dates_and_totals(text)
mean = calculate_mean(rain_data)
variance = calculate_variance(mean, rain_data)
rainiest_day = most_daily_rain(rain_data)

# print(rain_data)
# print(mean)
# print(variance)
# print(rainiest_day)

print(f'\nThe mean of rain data is: {round(mean, 4)}')
print(f'\nThe variance of rain data is: {round(variance, 4)}')
print(f'\nThe rainiest day was: {rainiest_day}\n')