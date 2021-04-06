


from turtle import *
# import turtle

# Draw a stick person (Vitruvian man)


# Preferences
pensize(5)
fillcolor('blue')


# choose a to start point
penup()
left(90)
forward(100)
right(90)
pendown()

# draw the head
begin_fill()

circle(40)

end_fill()

# draw the neck
right(90)
forward(20)

# draw the left arm
right(130)
forward(120)

# return to shoulder
penup()
right(180)
forward(120)
pendown()

# draw right arm
left(90)
forward(120)

# return to shoulder
penup()
right(180)
forward(120)
pendown()

# draw torso
left(50)
forward(100)

# draw the right leg
left(45)
forward(160)

# return to hip
penup()
right(180)
forward(160)
pendown()

# draw left leg
left(90)
forward(160)

done()
