from turtle import *




# starting with the head
i = 0 
while i<4:
    forward(100)
    left(90)
    i += 1

penup()

# the body
setposition(50,0)
pendown()
right(90)
forward(150)

# now heading back up for the arms
right(180)
forward(75)
left(90)
forward(75)
left(180)
penup()
forward(75)
pendown()
forward(75)

# now heading back down for the legs
penup()
right(180)
forward(75)
left(90)
forward(75)
pendown()
left(30)
forward(75)
penup()
left(180)
forward(80)
left(180)
right(60)
pendown()
forward(80)


done()