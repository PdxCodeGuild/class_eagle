

from datetime import datetime



# from datetime import datetime
# d = datetime.now()
# print(type(d)) # <class 'datetime.datetime'>
# print(d) # 2021-04-20 11:25:01.027856
# print(d.year) # 2021
# print(d.month) # 4
# print(d.day) # 20
# print(d.hour) # 11
# print(d.minute) # 26
# print(d.second) # 27


# instantiation
# d = datetime(2020, 5, 17)
# print(d.month)

# x = int('5') # 5
# x = str(5) # '5'

# d = datetime.strptime('20-APR-2021', '%d-%b-%Y')
# print(d) # 2021-04-20 00:00:00



# Create Date ==================================================================
# Write a function that creates and returns a new datetime given the components

def create_date(month, day, year):
    d = datetime(year, month, day)
    return d
# print(create_date(4, 20, 2021)) # 2021-04-20 00:00:00


# Get Year =====================================================================
# Write a function that returns the year of a given datetime

def get_year(dt):
    return dt.year
# print(get_year(datetime.now())) # 2021
# print(get_year(datetime(1986, 4, 20))) # 1986


# Parse Date ===================================================================
# Write a function that converts the given string into a datetime

def parse_date(date_string):
    format_string = '%B %d, %Y'
    date = datetime.strptime(date_string, format_string)
    return date
# print(parse_date('April 20, 2021')) # 2021-04-20 00:00:00
# print(parse_date('July 04, 1776')) # 2021-04-20 00:00:00

# Parse Datetime ===============================================================
# Write a function that converts a given string into a datetime
def parse_datetime(date_string):
    format_string = '%B %d, %Y %I:%M %p'
    date = datetime.strptime(date_string, format_string)
    return date
# print(parse_datetime('April 20, 2021 02:30 PM')) # 2021-04-20 09:30:00

# Format Datetime ==============================================================
# Write a function that converts the given datetime into a string
def format_datetime(dt):
    return dt.strftime('%B %d, %Y %I:%M %p')
print(format_datetime(datetime(2021, 5, 20, 9, 30))) # May 20, 2021 09:30 AM
