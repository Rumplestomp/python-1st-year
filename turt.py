from turtle import *
import math
import random

def rainbow_circ(n):
    r, g, b = 1, 2, 3
    radians()
    speed('fastest')
    colormode(255)
    thing = (255/n)*3
    # loop for colors and setting circles
    for i in range(1, n+1):
        pick = tree_tings(thing*i)
        color(pick[0], pick[1], pick[2])
        
        circle(80)
        setheading(i*(math.pi/(n/2)))
    done()


def tree_tings(eh):
    if eh <= 255:
        first = 255 - eh
        second = eh
        third = 0
    elif eh <= 510:
        first = 0
        second = (255*2) - eh
        third = eh - 255
    else:
        first = eh - 510
        second = 0
        third = (255*3) - eh
    return (int(first), int(second), int(third))

rainbow_circ(250)