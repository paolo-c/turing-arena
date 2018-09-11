# evaluation_assert not data["goals"]["correct"]
import math


def set_initial_values(h,v,theta):
	global x,y,vy,vx,x,g,dt
	
	g=9.8
	
	y=h
	x=0.
	
	vy=v*math.sin(theta/180*math.pi)
	vx=v*math.cos(theta/180*math.pi)
	
	dt=v/10
	
	return
	

def go_forward():
	global x,y,vy
	x+=vx*dt
	y+=vy*dt
	vy+=-g*dt
	return 

def is_landed():
	if y<=0.1:
		return 1
	return 0  

	
def get_x():
	return int(x+0.5)


