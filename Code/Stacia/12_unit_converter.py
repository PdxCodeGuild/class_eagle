conversions={

    "feet": 0.3048,
    "miles": 1609.34,
    "meters": 1,
    "killometers": 1000,
    "yards": 0.9224,
    "inches": 0.0254
    } 
#def Input block
base = input ("what unit would you like to start with?")
while base not in conversions:
    base = input ("unit not suppoerted. Please enter feet, miles, meters killometers, yards, or inches.")
      
conversion = input (f" what would you like to convert your {base} to?" )
while conversion not in conversions:
    conversion = input ("unit not suppoerted. Please enter feet, miles, meters killometers, yards, or inches.")

units = int(input(f"how many {base} would you like to convert to {conversion}? "))

#this could be a function. If i wanted to itterate.  

#def converter
if conversion =="meters" :
    answer = conversions[base] * units

else:
    stepone = conversions["meters"] / units
    answer  =  conversion 

print (answer)
