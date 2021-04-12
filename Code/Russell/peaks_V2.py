


def is_peak(data, i):
    peaks = []
    for i in range(1,len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            peaks.append(i)
    return peaks
    



#       0  1  2  3  4  5  6  7  8  9  10
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


x = is_peak(data, i)

print(x)



