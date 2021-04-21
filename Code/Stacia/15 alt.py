import requests
import re
from datetime import datetime
import string
import math
step2=0
rainy = {}
keyring = []
sums_of_mean_minus = []
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')

realtext = response.text
sum_sq_dif = 0

from datetime import datetime

# turn a string into a datetime object
date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')


def tups_split(realtext):
    regex_date = r'(\d{2}-\w+-\d{4}) \s+(\d+)'

    tups = re.findall(regex_date,realtext)
    return tups
def days(tups):
    date = datetime.strptime(tups,'%d-%b-%Y')



tups=tups_split(realtext)


total=0
for i in range (len(tups)):
    
    date , rain = tups[i]
    
    rainy[date]=int(rain)
    keyring.append(date)

for i in range (len(keyring)):
    
   total += rainy.get(keyring[i])
   mean= total/((len(keyring)))
# The sum of squares is all the squared differences added together and put in a list
for i in range (len(keyring)):
    step_1 =float(rainy.get(keyring[i]) - mean)
    step_2 = step_1**2
    sum_sq_dif += step_2



variance = sum_sq_dif/(len(keyring))

print(total)
print(mean)
print(variance)



#rain=rain_split(realtext)
#print(rain)
