from turtle import *

#left leg
left(60)
forward(50)

#right leg
right(90)

forward(50)

#goto where legs meet
penup()
right(180)
forward(50)
pendown()

#lower torso
right(30)
forward(100)

#right arm
right(90)
forward(40)
penup()
right(180)
forward(40)
pendown()

#left arm
forward(40)
penup()
right(180)
forward(40)
left(90)
pendown()

#upper torso
forward(50)
right(90)

#head
begin_fill()
for i in range(0,180):
    left(2)
    forward(1)
end_fill()
done()    