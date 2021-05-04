import requests
import re
from datetime import datetime
import string

rainy = {}
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')

realtext = response.text


from datetime import datetime

# turn a string into a datetime object
date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')


def date_split(realtext):
    regex_date = r'(\d{2}-\w+-\d{4}) \s+(\d+)'

    blue = re.findall(regex_date,realtext)
    return blue
def days(blue):
    regex_date = r'(\d{2}-\w+-\d{4})'
    yellow = re.findall(regex_date,realtext)

blue=date_split(realtext)
#rain=rain_split(realtext)
#print(rain)
yellow=days(blue)
print(yellow)


print (date)