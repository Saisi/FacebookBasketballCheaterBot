#!/usr/bin/env python
#not always current
#failed ball info
#reduce size of transactions
#update 9000 values
#1440x900
from pyscreenshot import grab
from PIL import Image
from time import sleep
from os import system
from random import randint
from sys import exit
import threading
import os
#image.resize((300, 160), Image.ANTIALIAS).show()


dragger=os.path.dirname(os.path.realpath(__file__))+"/dragger.py "

window_x = -350
window_y = 0

x_offset=350
y_offset=0

anchor_x = window_x+x_offset
anchor_y = window_y+y_offset

max_x = 358+anchor_x
min_x = 92+anchor_x
max_y = 301+anchor_y
min_y = 248+anchor_y

def get_hoop():
	previous = 1
	start = 0
	end = 0
	hoop_y = 0
	hoop_x = 0

	s_x = 0+anchor_x
	s_y = 249+anchor_y
	image = grab(bbox=(s_x,s_y,450,1))

	for j in xrange(0,1):
		if end > 0: break
		for i in xrange(0,448):
			t = image.getpixel((i,j))
			if t[2] == 15 and t[1] == 38:
				if previous == 1: 
					start = i
					previous = 0
					hoop_y = j
			else:
				if previous == 0: 
					previous = 1
					end = i

	hoop_x = (start+end)/2
	return (hoop_x+s_x,hoop_y+s_y)

def determine_direction(x=0):
	x_1,y_1 = get_hoop()
	x_2,y_2 = get_hoop()

	if x_1 < x_2:
		return (1,x_2,y_2)
	elif x_1 > x_2:
		return (-1,x_2,y_2)	
	else:
		if x > 4: return None
		return determine_direction(x+1)



b = h = 0
previous_direction = 0


print "LET'S FUCKING GO"
print "\n"*3

previous_level = 0


substitute = 0


def get_ball():
	count = 0
	b = 0
	t = 0
	start = -1
	end = -1
	ball_j = 0
	s_x = 0+anchor_x
	s_y = 577+anchor_y
	while start < 0:
		image = grab(bbox=(s_x,s_y,500,1))
		for j in xrange(0,1):
			for i in xrange(0,498):
				t = image.getpixel((i,j))
				if t[2] == 47 and t[1] == 150 :
						if start < 0:
							ball_j = j
							start = i
						else:
							end = i
	

	assert end > 0

	start = (start+end)/2
	return (start+s_x,(ball_j)+s_y)




def determine_level():
	return determine_direction_two()

def determine_direction_two(x=0):
	x_1,y_1 = get_hoop()
	sleep(.1+x/10.0)
	x_2,y_2 = get_hoop()

	if x_1*x_2*y_1*y_2 == 0: return 4

	s_x = 165+anchor_x
	s_y = 440+anchor_y

	image=grab(bbox=(s_x,s_y,10,2))
	for j in xrange(0,2):
		for i in range(0,9):
			if image.getpixel((i,j))[0] == 126: return 4

	if x_1 == x_2: 
		if y_1 == y_2: 
			if x == 1: return 1
			else: return determine_direction_two(1)
		return 4

	s_x = 170+anchor_x
	s_y = 463+anchor_y

	i=grab(bbox=(s_x,s_y,4,1))
	if  i.getpixel((0,0))[0] == 126: return 3
	return 2
	

def level_one():
	print "1, i am captain now"
	h = get_hoop()
	b = get_ball()

	return (b,h)


def level_two():
	print "2, i am captain now"

	b = get_ball()
	ball_x = b[0]

	v = (309-52)/3.5
	#v = 75


	
	t = determine_direction(0)
	if t is None:
		print "de nada"
		return None

	d,x,y = t
	dist = abs(x-b[0])
	print dist, "distance"
	print x,"actual hoop_x"


	d_x = 158.542;


	if d == -1:
		x -= d_x
	else:
		x += d_x

	if x > max_x: x = max_x-(x-max_x)
	if x < min_x:  x = min_x+(min_x-x)


	dist=abs(x-b[0])


	x = int(x)
	h = (x,y-50)
	print x,"predicted hoop_x"
	print b[0],"actual ball_x"
	return (b,h)


def level_three():
	print "3, i am captain now"

	b = get_ball()
	ball_x = b[0]

	#v = (309-52)/3.5
	v=140.666666

	t = determine_direction(0)
	if t is None:
		print "de nada"
		return None

	d,x,y = t


 	dist = abs(x-b[0])
	print dist, "distance"

	print x,"actual hoop_x"

	d_x = 280
	if d == -1:
		x -= d_x
	else:
		x += d_x

	while x > max_x or x < min_x:
		if x > max_x:
			x = max_x-(x - max_x)
		if x < min_x: 
			x = min_x+( min_x -x)


	dist=abs(x-b[0])

	# previous is 40
	x = int(x)
	h = (x,y-40)
	print x,"predicted hoop_x"
	print b[0],"actual ball_x"
	return (b,h)


def compute_x(d,x):
	#v = 140.66
	#d_x=1.2755*v

	#170
	d_x = 300;

	if d == -1:
		x -= d_x
	else:
		x += d_x	

	i=0
	while x > max_x or x < min_x:
		if x > max_x:
			x = max_x-(x - max_x)
		if x < min_x: 
			x = min_x+( min_x -x)
		i+=1
		if i>9: return None
	return int(x)



def compute_y(d,y):
	v = 36.520

	d_y = v*2.312
	if d == -1:
		y -= d_y
	else:
		y+= d_y

	i=0
	while y > max_y or y < min_y:
		if y > max_y:
			y = max_y-(y-max_y)
		if x < min_y: 
			y = min_y +( min_y -y)
		i+=1
		if i>9: return None

	return int(y-40)	

def get_moving_hoop():
	s_x = 0+anchor_x
	s_y = 100+anchor_y
	image = grab(bbox=(s_x,s_y,650,250))
	previous = 1
	start = -1
	end = -1
	hoop_y = 0
	for j in range(0,248):
		if end > 0: break
		for i in range(0,648):
			t = image.getpixel((i,j))
			if end > 0: break
			if t[2] == 15 and t[1] == 38:
				if previous == 1: 
					start = i
					previous = 0
					hoop_y = j
			else:
				if previous == 0: 
					previous = 1
					end = i

	if start<=0: return None
	if end<=0: return None
	hoop_x=(start+end)/2
	return (hoop_x+s_x, hoop_y+s_y)

def get_moving_direction():
	t=get_moving_hoop()
	if t is None: return None
	x_1,y_1 =t
	t=get_moving_hoop()
	if t is None: return None
	x_2,y_2=t
	dir_x=dir_y=-1
	if x_2 > x_1: dir_x = 1
	if y_2 > y_1: dir_y=1
	return (dir_x,dir_y,x_2,y_2)

def level_four():
	print "4, i am captain now"

	b = get_ball()
	ball_x = b[0]

	
	t= get_moving_direction()
	if t is None: return None
	dir_x, dir_y,x,y = t
	print x,y,"actual hoop"
	dist = abs(x-b[0])
	print dist, "distance"
	if (x > (305+anchor_x) or y < (100+anchor_x)): 
		print "Too far"
		return None

	print b, "balll"


	y = compute_y(dir_y,y)
	if y is None: return None
	x = compute_x(dir_x,x)
	if x is None: return None



	print x,y,"predicted hoop"
	
	h = (x,y-30)
	return (b,h)


level = 1


for x in xrange(1,1000000):

	if x%10==0:
		print "x: ",x

	s_x = 242+anchor_x
	s_y = 353+anchor_y

	i=grab(bbox=(s_x,s_y,5,1))
	if i.getpixel((0,0))[0] == 126 and previous_level > 1:
		dist = abs(previous_b[0]-previous_h[0])
		print dist, "marked dangerous"
		level = 1
	else:
		level = determine_level()

	
	if level == 1:
		b,h = level_one()
	elif level == 2:
		t = level_two()
		if t is None: continue
		b,h  = t
		dist = abs(b[0]-h[0])

		if (h[0] > (anchor_x+305) or h[0] < (anchor_x+100)): 
			print "Too far"
			continue

		if dist > 100:
			continue

	elif level == 3:

		t= level_three()
		if t is None: continue
		b,h =t
		b=(int(b[0]),int(b[1]))
	

		if (h[0] > (anchor_x+305) or h[0] < (anchor_x+100)): 
			print "Too far"
			continue
		dist = abs(b[0]-h[0])
		if dist > 100:
			continue
			
	elif level == 4:
		#exit()

		t = level_four()
 		if t is None:continue
 		b,h = t	

		if (h[0] > (anchor_x+305) or h[0] < (anchor_x+100)): 
			print "Too far"
			continue

		dist = abs(b[0]-h[0])
		if dist > 70:
			continue

		

	b=(int(b[0]),int(b[1]))
	h=(int(h[0]),int(h[1]))
	system(dragger + str(b[0]) + " " +  str(b[1]) + " "+ str(h[0]) + " " + str(h[1]) + " " + str(level))
	previous_b=b
	previous_h=h	
	previous_level = level

