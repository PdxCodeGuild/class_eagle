
# random is imported allowing for random int. 
import random

 
def picksix ():#define a picksix function.
    ticket=[]# a ticket will store a list to be created in the for loop.
    for i in range(6): # this is a counter that will run 6 times. 
        number=random.randint(1,6)# a random number is generated.
        ticket.append(number)# the number is stored in the loop. 
        i+=1# this is likely unessisary. I then to run if loops that say if counter < 6 and add one each time...
    
    return ticket #this return allows the function to produce a ticket that exists outside the fuction. 

#2. Start your balance at 0

def poor_life_choices():
    match = 0
    winnings = 0 #here we start integers for cost match and winnings. each of these will have values reassined later and will be returned. 
    cost = 0
    total = 0
    #2. Loop 100,000 times, for each loop:
    lucky = picksix() #here we pick the lucky ticket by calling the pick six function.
    
    for i in range (100,000): #this loop will allow us to expereince loss 100,000 times as it runs over and over.  

         #3. Generate a list of 6 random numbers representing the ticket
        ticket=picksix() #heres a ticket each ticket will run the picksix indipendent of others. 

        #4. Subtract 2 from your balance (you bought a ticket)
        cost += -2 # here the user is charged two dollars to a running cost value. 
        
        #5. Find how many numbers match

        for g in range (6): #here we run over the numbers. 
            
            if ticket[g] == lucky[g]: # check if the indices match on lucky and ticket. 
                match +=1 # if its a match you get one point for this ticket. 
        #6. Add to your balance the winnings from your matches
        

        # We start with six matches and use elif statements of only one condition will trigger at the highest victory level. THis way three matches adds $100 and not 113
        if match == 6:
            winnings += 25,000,000
            sixers +1
        elif match == 5:
            winnings += 1,000,000
            fivers +=1
        elif match == 4:
            winnings += 50,000
        elif match == 3:
        winnings += 100
        elif match == 2:
            winnings += 7
        elif match == 1:
            winnings += 4      
        # matches are outside of the evaluation loop so that all the matches can be evaluated per each ticket. 
    
    return cost, winnings, total #these values are returned. 
#7. After the loop, print the final balance


print ("New Jersey pick six has an odd of one in 13,983,816.")
play= input("Are you fealing lucky?")
print ("It dosen't matter at two bucks a ticket your paying for the fantasy")
print ("but with 100,000 tickets how could you lose?")
print ("Sure you could by that 7 bedroom almost 4000 square foot house in Pilesgrove, but with 25,000,000 million calling your name you could build a realestate empire.
print ("What could go wrong?")
cost, winnings, total = poor_life_choices()

print (f"Well what could you expect? {winnings} only cost you {cost}")
print (f" Thats a net of {total}")