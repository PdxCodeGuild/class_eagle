
def peaks(value):
    peaks=[]
    for i in range(1,len(value)-1):
        data_last=value[i-1]
        data_current=value[i]
        data_next=value[i+1]
        if data_current >data_last and data_current > data_next:
            peaks.append(i)
    return peaks
def valleys(value):
    valleys=[]
    for i in range(1,len(value)-1):
        data_last=value[i-1]
        data_current=value[i]
        data_next=value[i+1]
        if data_current < data_last and data_current < data_next:
            valleys.append(i)
    return valleys
        

data = [1,2,3,4,5,6,7,6,5,4,5,6,8,9,8,6,7,8,9]
print ("peaks:")
print(peaks(data))
print("valleys")
print (valleys(data))

#def highest_value(value)
def draw (data):
    row= biggest number
    stacks- len (data)
    for i in range(row, 0,-1:
        for j in range (stack)
        print x, end
        #line of list of string
#  A loop that takes highest_value
    #for i in range():
# a loopruns backwards from highest number
# if positions value == or < current number
    #add to string a x or  space
     #print with every run
     def draw)peaks_valleys (data):
