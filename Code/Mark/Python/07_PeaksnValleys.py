data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


# def peak(data):
#     output = []
#     for i in range(len(data)-1):
#       if data[(i-1)] < data[i] > data[(i+1)]:
#           output.append(i)
#     return output


# def valley(data):
#     output = []
#     for i in range(1,len(data)):
#       if data[(i-1)] > data[i] < data[(i+1)]:
#           print(data[i])
#           output.append(i)
#     return output


def peaks_and_valleys(data):
    output = []
    for i in range(1, len(data)-1):
        if data[i-1] > data[i] < data[i+1] or data[i-1] < data[i] > data[i+1]:
            output.append(i)
    for i in data:
        print('x '*i)
    return output


# print(peak(data))
# print(valley(data))
print(peaks_and_valleys(data))
