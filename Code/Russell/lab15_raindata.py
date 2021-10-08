import re
from datetime import datetime
import matplotlib.pyplot as plt

with open('cascade.rain.txt', 'r') as file:
    text = file.read()
# print(text[:700])


# dates_list 

regex_date = r'(\d+-[A-Z]{3}-\d{4}) +(\d+)'

date_result = re.findall(regex_date, text)


data_list =[]
for i in range(len(date_result)):
    data_list.append({ 'date' : date_result[i][0], 'total'  : date_result[i][1] })

for i in range(len(data_list)):
    data_list[i]['date'] = datetime.strptime(data_list[i]['date'], '%d-%b-%Y')

for i in range(len(data_list)):
    data_list[i]['total'] = int(data_list[i]['total'])

def average(nums):
    total = 0
    for i in range(len(data_list)):
        total += data_list[i]['total']
    return(total) / len(nums)



def variance(nums, mean):
    total = 0
    for num in nums:
        total += (nums[i]['total'] - mean)**2
    return total / len(nums)


mean = average(data_list)



seq = []
for x in data_list:
    seq.append(x['total'])

 
#Iterate over the data list to find the day with the highest rainfall 
highest = max(seq)
for i in range(len(data_list)):
    if data_list[i]['total'] == highest:
        print(f"The highest rainfall was on: {data_list[i]['date']}")



x_vs = []
for i in range(len(data_list)):
    x_vs.append(data_list[i]['date'])
    

y_vs = []
for i in range(len(data_list)):
    y_vs.append(data_list[i]['total'])


x_values = x_vs
y_values = y_vs
plt.plot(x_values, y_values)
plt.show()
