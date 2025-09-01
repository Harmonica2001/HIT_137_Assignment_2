#HIT137: Software Now: Assesment 2: Question 3

#We are using turtle to draw a fractal polygon

import turtle

# -------Drawing one edge--------

# Our job is to take one side and decide is to take one side of the polygon and decide, if depth is 0 → just draw it straight, if that is more than 0 → instead of one straight line, need to cut it into three parts and make a triangle dent in the middle and the process repeats again and again until depth reaches 0.


def draw_edge(leanth,depth):
    if depth == 0:
        turtle.forward(leanth)
    else:
        leanth=leanth/3 #will divide the side in 3 equal parts

        #First portion would be straight
        draw_edge(leanth, depth - 1)

        # In the 2nd portion dent needs to be there by going up and will go down
        turtle.left(60)
        draw_edge(leanth, depth -1)

        turtle.right(120)
        draw_edge(leanth, depth -1)
    

        # For the 3rd portion, needs to get back to original direction
        turtle.left(60)
        draw_edge(leanth, depth -1)



# ------ Drawing full polygon--------

#We are using edge function recursively for all the sides, after each side is drawe we need to turn the turtle by 360/sides to complete the polygon shape

def draw_polygon(sides, leanth, depth):
    for _ in range(sides):
        draw_edge(leanth,depth)
        turtle.right(360/sides)


# ------ Asking for input --------

# This part takes user inputs, sets up the turtle to draw the polygon, and keeps the window open until it’s closed.

sides = int(input("Enter the number of sides:"))
length = int(input("Enter the side leanth:"))
depth = int(input("Enter the recursion depth:"))

turtle.speed(0)
turtle.hideturtle()


draw_polygon(sides, length, depth)  

turtle.done()         