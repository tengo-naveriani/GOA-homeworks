from turtle import *


# we want to paint a house

#step 1: draw a square

width(7)
color("yellow")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("brown")
begin_fill()

left(90)
forward(70)
right(90)
forward(35)
right(90)
forward(70)
end_fill()
#end of door

#drawing a roof
penup()
goto(200, 200)
right(125)
color("brown")
pendown()
begin_fill()
forward(120)
left(70)
forward(120)
end_fill()
#end of roof

#drawing a windows
penup()
goto(20,120)
right(125)
color("blue")
pendown()
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()
 
penup()    
goto(120,120)
pendown()
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()



exitonclick()
