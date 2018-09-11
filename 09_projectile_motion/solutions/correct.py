# evaluation_assert data["goals"]["correct"]
import math

def sin(x):
	if x==0:
		return 0
	return math.sin(x/180*math.pi)

def cos(x):
	if abs(x)==90:
		return 0
	return math.cos(x/180*math.pi)

def set_initial_values(h,v,theta):
	global x,y,vy,vx,x,g,dt
	
	g=9.8
	
	y=h
	x=0.
	
	vy=v*sin(theta)
	vx=v*cos(theta)
	
	if vx*vy==0:
		dt=v/1000.
	else:
		dt=min(abs(vx),abs(vy))/1000.

	return
	

def go_forward():
	global x,y,vy
	x+=vx*dt
	y+=vy*dt
	vy+=-g*dt
	return 

def is_landed():
	if y<=0.1 and vy<=0:
		return 1
	return 0  

	
def get_x():
	return int(x+0.5)
