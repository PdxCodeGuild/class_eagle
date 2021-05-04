import random

dataset = [2,11,3,6,5,13,90,23,9,10]
dataset_2 = [1, 2, 3, 4, 5, 6, 7, 8,9]

def linear(dataset, target):
    
    for index in range(len(dataset)):
        
        if dataset[index] == target:
            
            position=index
            return position
    else: 
        return position

linear_sort = (dataset, 4)
print (f'linear sort target is in position {linear_sort}')
print()

def binary(dataset,target):

    low = 0
    high = len(dataset) -1

    while low < high:
        mid = ((low+high)) // 2
        if dataset[mid] < target:
            low = mid +1
        elif dataset[mid] > target:
            high = mid-1
        else:
            return mid
    

binary_sort = binary(dataset_2, 8)
print (f'binary sort 8 is in index position {binary_sort}')
print()          

print("bubble sort")        
def bubble_sort2 (dataset):
    n =len(dataset)
    
    swap = True
    while swap == True:
        swap = False
        for i in range(1,len (dataset)):
            x= dataset[i]
            y= dataset[i-1]
            if y > x : 
                temp = dataset[i]
                dataset[i] =dataset[i-1]
                dataset[i-1] = temp
                swap= True
                print(dataset)
        return dataset

bubble = bubble_sort2(dataset)

print()


def insert_method (dataset):
    n =len(dataset)
    print(dataset)
    swap = False
    while swap == False:
        swap=False
        for i in range (1,len (dataset)):
        
            x= dataset[i]
            y= dataset[i-1]
            if y > x : 
                dataset.insert(x, y)  
                dataset.remove (y)
                
    swap=True 
    return dataset
    
insert = insert_method(dataset)
print (f'{dataset} becomes {insert} after insert.')
print ("fuck")