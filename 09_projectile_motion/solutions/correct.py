# evaluation_assert data["goals"]["correct"]
import math

def sin(x):
	return math.sin(x/180*math.pi)

def cos(x):
	return math.cos(x/180*math.pi)

def set_initial_values(h,v,theta):
	global x,y,vy,vx,x,g,dt
	
	g=9.8
	
	y=h
	x=0.
	
	vy=v*sin(theta)
	vx=v*cos(theta)
	
	dt=v/100.
	
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



def theoric(h,v,theta):
	g=9.8
	vy=v*sin(theta)
	t=(vy+math.sqrt(vy**2 + 2*g*h))/g
	return v*cos(theta)*t
	
def simul(h,v,theta):
	set_initial_values(h,v,theta)
	while is_landed()==False:
		go_forward()
	return get_x()


