import requests
import re
from datetime import datetime
import string
import math

import matplotlib.pyplot as plt
from datetime import datetime


def plot(z):
    dic_maker(tups)
    y_line = []
    x_line = []   
    for i in range(len(z)):
        
        y_line.append(z[i]['keyring'])
        x_line.append(z[i]['puddle'])
    plt.plot(x_line, y_line)
    plt.show()


# turn a string into a datetime object
# date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')


def get_data():
    response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')

    realtext = response.text
    regex_date = r'(\d{2}-\w+-\d{4}) \s+(\d+)'
    date = datetime.strptime()

    tups = re.findall(regex_date, realtext)
    # we have a list of tuples, and each tuple has two strings
    # we could convert that into a list of tuples where each tuple has a datetime and a int

    return tups



def dic_maker(x):
    rainy = {}
    keyring = []
    puddle =[]
    for i in range (len(tups)):
        date, rain = tups[i]
        rainy[date]=int(rain)
        keyring.append(date)
        puddle.append(rain)
    return rainy , keyring , puddle


def average (z):
    total=0
    for i in range (len(z)):
        x , y = z[i]
        total += int(y)

        # total += int(z[i][1])

    total=(total / len(z))
    return total

def variance(z):
    mu = average(z)
    total_2 = 0
    for i in range (len(z)):
        x , y = z[i]
        total_2 += (int(y) - mu)**2
    total_2 = total_2 / len(z)
    return total_2

def standard_deviation(z):
    
    v= variance(z)
    return math.sqrt(v)

tups = get_data()
rainy=dic_maker(tups)
av = average(tups)
vartotal = variance(tups)
sd = standard_deviation(tups)
plot(rainy)
print (vartotal)
print (av)



