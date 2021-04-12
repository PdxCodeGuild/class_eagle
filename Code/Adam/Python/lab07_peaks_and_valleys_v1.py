

# Lab 7: Peaks and Valleys


# Define the following functions:

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# 1. peaks(data)
# Define peaks(data)
def peaks(data):
    peaks = []
    # Compare previous_num, num, and next_num; if num is the largest of the three it is a peak.
    for i in range(1, len(data)-1):
        num = data[i]
        previous_num = data[i-1]
        next_num = data[i+1]
        if previous_num < num > next_num:
            peaks.append(i)
    # Return the indices of the peaks.
    return(peaks)

print(peaks(data))

# 2. valleys(data)
# Define valleys(data)
def valleys(data):
    valleys = []
# Compare previous_num, num, and next_num;if num is the lowest its a valley.
    for i in range(1, len(data)-1):
        num = data[i]
        previous_num = data[i-1]
        next_num = data[i+1]
        if previous_num > num < next_num:
            valleys.append(i)
    # Return the indices of the valleys.
    return valleys

print(valleys(data))

# 3. peaks_and_valleys(data)
# Define peaks_and_valleys(data)
def peaks_and_valleys(data):
    peaks_and_valleys = []
    # Compare previous_num, num, and next_num to check for a peak or a valley
    for i in range(1, len(data)-1):
        num = data[i]
        previous_num = data[i-1]
        next_num = data[i+1]
        if previous_num < num > next_num:
            peaks_and_valleys.append(i)
        elif previous_num > num < next_num:
            peaks_and_valleys.append(i)
    # Return a list of peaks and valleys
    return peaks_and_valleys

print(peaks_and_valleys(data))