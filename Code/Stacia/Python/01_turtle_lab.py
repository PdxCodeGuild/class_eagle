from turtle import * #the turle pack is imported allowing all the turtle functions.
#0,0 is the defult cordinate. 
circle (20) #this draws a circle with a radius of 20. 
setposition (0,-100)#the tutle moves to this position dragging a pen behind it.
setposition (-30,-200) # the turtle moves from the hips to the left leg. 
penup ()#the pen is lifted from the paper.
setposition (0,-100)# because the pen is up it will not draw a line as it retuns to the hip. In this case it would just retrace a line.
pendown ()#the pin is placed back down.
setposition (30,-200) #because the pen is down a line is drawn to the right foot.
penup ()
setposition (-60,-20)
pendown ()
setposition (60,-20)


done()#its nice to put the turtle away when your done with it. 
