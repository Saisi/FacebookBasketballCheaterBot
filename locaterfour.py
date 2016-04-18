#!/usr/bin/env python
#not always current
#failed ball info
#reduce size of transactions
#update 9000 values
#1440x900
from PIL.ImageGrab import grab
from PIL import Image
from pytesseract import image_to_string
from time import sleep
from os import system
from random import randint
from sys import exit
import threading

#image.resize((300, 160), Image.ANTIALIAS).show()

def get_hoop():
	previous = 1
	start = 0
	end = 0
	hoop_y = 0
	hoop_x = 0
	image = grab(bbox=(0,249,450,1))
	for j in xrange(0,1):
		if end > 0: break
		for i in xrange(0,448):
			t = image.getpixel((i,j))
			if t[2] == 15 and t[1] == 38:
				if previous == 1: 
					start = i
					previous = 0
					hoop_y = (j)+249
			else:
				if previous == 0: 
					previous = 1
					end = i

	hoop_x = (start+end)/2
	return (hoop_x,hoop_y)

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
direction = 0
previous_b=(9000,9000)
previous_h=(-9000,-9000)
previous_direction = 0
transactions = []

r1 = []
l1 = []
l2 = []
r2 = []
r3= []
l3= []

mode = 'r1'
lines=open('facts')
for line in lines:
	line = line.strip()
	if line == "": continue
	if line=='r1': 
		mode = 'r1'
		continue
	elif line=='l1':
		mode = 'l1'
		continue
	elif line=='r2':
		mode='r2'
		continue
	elif line=='l2':
		mode='l2'
		continue
	elif line=='l3':
		mode='l3'
		continue
	elif line=='r3':
		mode='r3'
		continue

	if mode == 'r1':
		r1.append(int(line))
	elif mode == 'r2':
		r2.append(int(line))
	elif mode == 'l1':
		l1.append(int(line))
	elif mode == 'l2':
		l2.append(int(line))
	elif mode == 'l3':
		l3.append(int(line))
	elif mode == 'r3':
		r3.append(int(line))

lines=open('bogey')
for line in lines:
	line = line.strip()
	if line=="":continue
	transactions.append(int(line))

r1= list(set(r1))
r2= list(set(r2))
r3= list(set(r3))
l1= list(set(l1))
l2= list(set(l2))
l3= list(set(l3))

r1.sort()
l1.sort()
r2.sort()
l2.sort()
l3.sort()
r3.sort()


transactions= list(set(transactions))

print "LET'S FUCKING GO"
print "\n"*3

previous_level = 0


substitute = 0


def get_ball():
	#image = grab(bbox=(0,577,500,1))

	#get ball location
	count = 0
	b = 0
	t = 0
	start = -1
	end = -1
	ball_j = 0

	while start < 0:
		image = grab(bbox=(0,577,500,1))
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
	return ((start),(ball_j)+577)




def determine_level():
	return determine_direction_two()

def determine_direction_two(x=0):
	x_1,y_1 = get_hoop()
	sleep(.1+x/10.0)
	x_2,y_2 = get_hoop()

	if x_1*x_2*y_1*y_2 == 0: return 4

	image=grab(bbox=(165,440,10,2))
	for j in xrange(0,2):
		for i in range(0,9):
			if image.getpixel((i,j))[0] == 126: return 4

	if x_1 == x_2: 
		if y_1 == y_2: 
			if x == 1: return 1
			else: return determine_direction_two(1)
		return 4

	i=grab(bbox=(170,463,4,1))
	if  i.getpixel((0,0))[0] == 126: return 3
	return 2
	





def level_one():
	print "1, i am captain now"
	h = get_hoop()
	b = get_ball()

	return (b,h)




def level_two():
	print "2, i am captain now"
	global previous_direction, direction

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


	d_x = 159.542;

	previous_direction = d
	if d == -1:
		x -= d_x
	else:
		x += d_x

	# if x > 355.5: 
	# 	previous_direction *=-1
	# 	x = 355.5-(x-355.5)-10
	# elif x < 100.5: 
	# 	previous_direction *=-1
	# 	x = 100.5+(100.5-x)+10

	if x > 358:
		x = 358-(x-358)
	if x < 92: 
		x = 92+(92-x)


	dist=abs(x-b[0])
	if d == -1:
		if dist in l2: return None
	else:
		if dist in r2: return None



	# if x > 355.5 or x < 100.5:return (1,1)
	x = int(x)
	h = (x,y-50)
	print x,"predicted hoop_x"
	print b[0],"actual ball_x"
	return (b,h)


def level_three():
	print "3, i am captain now"
	global previous_direction, direction

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

	# if x > 300:
	# 	print "we ran away"
	# 	return None

	print x,"actual hoop_x"

	previous_direction = d
	d_x = 298
	if d == -1:
		x -= d_x
	else:
		x += d_x

	# if x > 355.5: 
	# 	previous_direction *=-1
	# 	x = 355.5-(x-355.5)-10
	# elif x < 100.5: 
	# 	previous_direction *=-1
	# 	x = 100.5+(100.5-x)+10

	while x > 358 or x < 92:
		if x > 358:
			x = 358-(x-358)
		if x < 92: 
			x = 92+(92-x)


	dist=abs(x-b[0])
	if d == -1:
		if dist in l3: return None
	else:
		if dist in r3: return None


	# previous is 40
	x = int(x)
	h = (x,y-40)
	print x,"predicted hoop_x"
	print b[0],"actual ball_x"
	return (b,h)


def compute_x(d,x):
	#v = 140.66
	#d_x=1.2755*v


	d_x = 310;
	previous_direction = d
	if d == -1:
		x -= d_x
	else:
		x += d_x	

	while x > 358 or x < 92:
		print x
		if x > 358:
			x = 358-(x-358)
		if x < 92: 
			x = 92+(92-x)

	return int(x)

def compute_y(d,y):
	v = 36.520

	previous_direction = d
	d_y = v*2.312
	if d == -1:
		y -= d_y
	else:
		y+= d_y

	while y > 301 or y < 248:
		print y
		if y > 301:
			y = 301-(y-301)
		if x < 248: 
			y = 248+(248-y)

	return int(y-40)	

def get_moving_hoop():
	image = grab(bbox=(0,100,650,250))
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
					hoop_y = (j)+100
			else:
				if previous == 0: 
					previous = 1
					end = i

	if start<=0: return None
	if end<=0: return None
	hoop_x=(start+end)/2
	return (hoop_x, hoop_y)

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
	global direction
	b = get_ball()
	ball_x = b[0]

	
	t= get_moving_direction()
	if t is None: return None
	dir_x, dir_y,x,y = t
	print x,y,"actual hoop"
	dist = abs(x-b[0])
	print dist, "distance"
	if (x > 305 or y < 100): 
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


def update_blacklist():

	global l1, l2, l3, r1, r2, r3
	global transactions, substitute

	b = previous_b
	h = previous_h
	if b[0] < 0:
		dist = -abs(abs(b[0])-h[0])
		b = (abs(b[0]), b[1])
	else:	
		dist = abs(b[0]-h[0])


	if substitute > 0: transactions.append(substitute)
	substitute = -100

	print "failed ball", b
	print "failed hoop", h
	print "knowledge is", dist

	if b[0] < h[0]:
		if previous_level == 1:
			l1.append(dist)
		elif previous_level == 2:
			l2.append(dist)
		elif previous_level == 3:
			l3.append(dist)
	elif h[0] < b[0]:
		if previous_level == 1:
			r1.append(dist)
		elif previous_level == 2:
			r2.append(dist)
		elif previous_level == 3:
			r3.append(dist)


def save_to_disk():
	with open('facts', 'w') as f:
	    f.write('r1\n')
	    for n in r1:f.write(str(n)+'\n')
	    f.write('l1\n')
	    for n in l1:f.write(str(n)+'\n')	    
	    f.write('r2\n')
	    for n in r2:f.write(str(n)+'\n')
	    f.write('l2\n')
	    for n in l2:f.write(str(n)+'\n')
	    f.write('r3\n')
	    for n in r3:f.write(str(n)+'\n')
	    f.write('l3\n')
	    for n in l3: f.write(str(n)+'\n')
	with open('bogey', 'w') as f:
	    for n in transactions:f.write(str(n)+'\n')


def level_three_new(x,y,d):
	
	print "new 3 captain now"
	

	print x,"actual hoop_x"
	v = 263
	d_x=.25*v

	if d == -1: d_x *=-1	
	x+=d_x

	if x > 355.5: x = 355.5-(x-355.5)
	elif x < 92: x = 92+(92-x)

	h=(int(x),y-20)
	print x,"predicted hoop_x"

	return h

hoop_x = None
hoop_y = None
level = 1



check = 0




for x in xrange(1,1000000):
	#substitute=-100
	if x%10==0:
		print "x: ",x
	skip = False

	if x%100 == 0:
		print("wrote to disk")
		r1= list(set(r1))
		r2= list(set(r2))
		r3= list(set(r3))
		l1= list(set(l1))
		l2= list(set(l2))
		l3= list(set(l3))
		transactions= list(set(transactions))
		save_to_disk()

	i=grab(bbox=(242,353,5,1))
	if i.getpixel((0,0))[0] == 126 and previous_level > 1:
		dist = abs(previous_b[0]-previous_h[0])
		print dist, "marked dangerous"

		# if level == 2:
		# 	if previous_direction == -1:
		# 		l2.append(dist)
		# 	else:
		# 		r2.append(dist)
		# elif level == 3:
		# 	if previous_direction == -1:
		# 		l3.append(dist)
		# 	else:
		# 		r3.append(dist)


		level = 1
	else:
		level = determine_level()

	if x==40:
		print x, "iteration"
		save_to_disk()


	
	if level == 1:
		b,h = level_one()
	
	elif level == 2:


		t = level_two()
		if t is None: continue

		b,h  = t
		dist = abs(b[0]-h[0])

		if (h[0] > 305 or h[0] < 100): 
			print "Too far"
			continue

		if dist > 100:
			continue

	elif level == 3:



		t= level_three()
		if t is None: continue
		b,h =t
		b=(int(b[0]),int(b[1]))
	

		if (h[0] > 305 or h[0] < 100): 
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

		if (h[0] > 305 or h[0] < 100): 
			print "Too far"
			continue

		

	b=(int(b[0]),int(b[1]))
	h=(int(h[0]),int(h[1]))
	system("/Users/saisi/Desktop/mac.py " + str(b[0]) + " " +  str(b[1]) + " "+ str(h[0]) + " " + str(h[1]) + " " + str(level))
	previous_b=b
	previous_h=h	
	previous_level = level

