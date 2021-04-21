import re
from datetime import datetime


with open('cascade.rain.txt', 'r') as file:
    text = file.read()
# print(text[:700])


# dates_list 

regex_date = r'(\d+-[A-Z]{3}-\d{4}) +(\d+)'

date_result = re.findall(regex_date, text)


data_list =[]
for i in range(len(date_result)):
    data_list.append({ 'date' : date_result[i][0], 'total'  : date_result[i][1] })
#Keep in mind the correct syntax here
for i in range(len(data_list)):
    data_list[i]['date'] = datetime.strptime(data_list[i]['date'], '%d-%b-%Y')
#Keep in mind the correct syntax here
for i in range(len(data_list)):
    data_list[i]['total'] = int(data_list[i]['total'])

def average(nums):
    total = 0
    for i in range(len(data_list)):
        total += data_list[i]['total']
    return(total) / len(nums)

n = len(data_list)

def variance(nums, mean):
    





print(n)




