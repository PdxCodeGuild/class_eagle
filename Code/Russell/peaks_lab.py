




#       0  1  2  3  4  5  6  7  8  9  10
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):
    peaks = []
    for i in range(1, len(data) -1):
        if data[i] > data[i -1] and data[i] > data[i + 1]:
            peaks.append([i])
    return peaks



def valleys(data):
    valleys = []
    for i in range(1, len(data) -1):
        if data[i] < data[i -1] and data[i] < data[i + 1]:
            valleys.append([i])
    return valleys



def peaks_valleys(data):
    pnv = []
    peaks_list = peaks(data)
    valleys_list = valleys(data)
    pnv.append(peaks_list)
    pnv.append(valleys_list)
    return pnv

both = peaks_valleys(data)

print(both)


