

import turtle


turtle.speed('fastest')

i = 0
n_sides = 1000
while i < n_sides:
    turtle.forward(1)
    turtle.left(360/n_sides)

turtle.done()

