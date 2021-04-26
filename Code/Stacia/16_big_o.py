import random


def linear(dataset, target):
    
    for index in range(len(dataset)):
        
        if dataset[index] == target:
            
            position=index
            return position
    else: 
        return position


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
    
   

#dataset
# length of list

#plant = binary(dataset_2, 8)

#dog = linear(dataset, 6)
           
        
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
dataset = [2,11,3,6,5,13,90,23,9,10]
dataset_2 = [1, 2, 3, 4, 5, 6, 7, 8,9]
#print(dataset) 
#bubble_sort2(dataset)
#print(dataset)
# k = nums[i]
        # nums[i] = nums[j]
        # nums[j] = k


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
    
#insert_method (dataset)



dog = linear(dataset, 6)
go = insert_method(dataset_2)
print (dataset_2)

print (dataset)
print (dog)
print (go)
print (dataset)
print (go)