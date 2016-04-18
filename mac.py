#!/usr/bin/env python
from Quartz.CoreGraphics import *
from time import sleep
from sys import argv, exit
from math import pow

def get_x_point(y,m,C):
    return (y-C)/(m*1.0)

def mouseEvent(type, posx, posy):
        theEvent = CGEventCreateMouseEvent(
                    None, 
                    type, 
                    (posx,posy), 
                    kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
        mouseEvent(kCGEventMouseMoved, posx,posy);

def mouseclick(posx,posy):
        # uncomment this line if you want to force the mouse 
        # to MOVE to the click location first (I found it was not necessary).
        mouseEvent(kCGEventMouseMoved, posx,posy);
        mouseEvent(kCGEventLeftMouseDown, posx,posy);
        mouseEvent(kCGEventLeftMouseUp, posx,posy);
        
def mousedrag(posx,posy):
    mouseEvent(kCGEventLeftMouseDragged, posx,posy)
    
def mouseclickup(posx,posy):
    mouseEvent(kCGEventLeftMouseUp, posx,posy)
		
def mouseclickdn(posx,posy):
    mouseEvent(kCGEventLeftMouseDown, posx,posy)



b=(int(float(argv[1])),int(float(argv[2])))
h=(int(float(argv[3])),int(float(argv[4])))


debug = False
# if int(argv[5]) == 4: debug = True

s = .02
# if len(argv) == 6:
#     if int(argv[5]) == 2:
#         h = (h[0],h[1]-20)

# if debug:
#     b=(125,577)
#     h=(225,209)

# print h,"height"
# print b, "current b values"

# ball_start = b[0]-20
# ball_end = b[0]+20

# start_h = h[0]-40
# end_h = h[0]+40


# print "\n"
# if ball_end < h[0]:
#     h=(start_h,h[1])
#     b=(ball_start,b[1])
#     print "left"
# elif ball_start > h[0]:
#     h=(end_h,h[1])
#     b=(ball_end,b[1])
#     print "right"


dist = (b[0]-h[0])
print "dragger start"
# print dist, "distance"
print b, "ball"
print h
print "end dragger"

# if 5 < dist < 80:
#     print "fingers crossed"
#     h=(h[0]+4,h[1])
# elif -5 < dist < -80:
#     h=(h[0]-4,h[1])


# for i in range(1,len(argv)):
#     argv[i]=int(argv[i])
#     if i % 2: argv[i]-=300

dist = abs(dist)



change_y = b[1] - h[1]
change_x = b[0] - h[0]

if(change_x == 0):
    change_x +=.25
    print("haya makanjo")


m = (change_y*1.0)/change_x
C = b[1] - (b[0]*m) 
d = change_y**2 + change_x**2

#print m,"slope"
print dist,"fake distance\n"
# print m,"current m"
# print d, "distance squared"
# print abs(b[0]-h[0])

for i in range(2):
    mouseclick(b[0], b[1])
    sleep(.15)


x = b[0]
y = b[1]




if not debug:
    mouseclickdn(x, y)


# vert = start_h < b[0]-20 < b[0] < b[0] + 20 < end_h
# level_two  = len(argv) == 6

# if level_two:
#     for i in range(3):
#         mousedrag(x, y)
#         y-=5
#         sleep(.04)
# else:



r=5

for i in range(r):
    if not debug:
        mousedrag(x, y)
    else:
        mousemove(x,y)
    #y-=10
    y -= 30
    x = int(get_x_point(y,m,C))
    sleep(s) #this needs tending



mousedrag(x, y)
mouseclickup(x, y)
sleep(.1)