# Optional Additions:
# - try randomly generating an input (TODO)
# - drawing the range with ASCII (DONE)

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def DerivFind(x): # function is used to find the derivative of given list
    y =[]
    for i in range(len(x) - 1): # because when calculating derivative, there is no first value or last value, we have to end the array one slot sooner...
        if i == 0: # ...and create a specialcase for the first slot of the array, which would be a 'null' value, but to save from typeError, we just set it at 0
            y.append(0)
        else:
            y.append(x[i+1] - x[i]) # calculate derivative (change in data / change in index) and index only goes up by 1 so, x/1 = 1 so we don't need to divide!
    return y

def Peaks(x):
    data_calc = []
    output = []
    data_calc = DerivFind(DerivFind(x)) # finding the double derivative, we can easily say, anything < 0 is a peak because of how derivatives work

    for i in range(len(data_calc)):
        if data_calc[i] < 0:
            output.append(i + 2) #Add 1 because array starts at 0, and add another 1 because the derivative moves the values over to the left (Null val in index 0)

    return output # return index + 1 of where the peak occurs

def Valleys(x):
    data_calc = []
    output = []
    data_calc = DerivFind(DerivFind(x)) # finding the double derivative, we can easily say, anything > 0 is a valley because of how derivatives work

    for i in range(len(data_calc)):
        if data_calc[i] > 0:
            output.append(i + 2) #Add 1 because array starts at 0, and add another 1 because the derivative moves the values over to the left (Null val in index 0)

    return output # return index + 1 of where the valley occurs

def PeaksAndValleys(x):
    peaks = Peaks(x).copy() #move the functions into lists here (without pointer to prevent possible bugs)
    valleys = Valleys(x).copy()

    output = [] # define as list
    output.extend(peaks) # combine the lists 
    output.extend(valleys)
    
    return sorted(output) # sort the list and return it!

def DataDraw(x): 
    # this function operats similar to a old-school dot-matrix printer, or CRT television
    # we go layer by layer, resetting when we get to the next layer

    layer = max(x) # finds the tallest peak
    calc_list = x.copy() #copy over list into function (without pointers to prevent changing the original list)

    while layer >= 0: # use a while loop here instead of a for loop so we can iterate down with the layer variable
        output = '' # define / redefine output string as blank

        for val in calc_list: # iterate through every value in the list
            if val > layer - 1: # if the 'height' at that point (val) is > the current layer we're on (max_height - iterations of height)
                output += ' * ' # to represent ground
            else:
                output += ' | ' # to represent air

            val -= 1 # subtract 1 from the height of this value because we have iterated through this layer
        print(output) # print the layer
        layer -= 1 # move to the next layer down
        
DataDraw(data) #draw the data

data_str = '' 

for n in data: #iterates through each value and turns into a string, (this is just for formatting so the data vals line up with the ASCII drawing)
    data_str += f' {str(n)} '

# Print results!
print(data_str)
print(f'Peaks occur at: {Peaks(data)}')
print(f'Valleys occur at: {Valleys(data)}')
print(f'Peaks & Valleys occur at: {PeaksAndValleys(data)}')