


def peaks(data):
    peaks_list = []
    for i in range(1,len(data)-1):
        if data[i+1] == data[i-1] and data[i] > data[i+1]:
            peaks_list.append(i)
    return print(peaks_list)


def valleys(data):
    valleys_list = []
    for i in range(1,len(data)-1):
        if data[i+1] == data[i-1] and data[i] < data[i+1]:
            valleys_list.append(i)
    return print(valleys_list)


def peaks_and_valleys(data):
    pv_list = []
    for i in range (1,len(data)-1):
        if data[i+1] == data[i-1] and data[i] != data[i+1]:
            pv_list.append(i)
    return print(pv_list)

