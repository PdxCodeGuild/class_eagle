import requests
import re
from datetime import datetime

regex = r'(\d{2}-\w{3}-\d{4})(\s+)(\d+)'
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
response = response.text
results = re.finditer(regex, response)

# turn a string into a datetime object
# date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')
def get_data(data):
    rain_data = []
    index = 0
    for match in data:
        index += 1
        date = datetime.strptime(match.group(1), '%d-%b-%Y')
        rain_data.append({'Date': date, 'Total': int(match.group(3))})
    return rain_data



print(get_data(results))
