import random

def compute_pi():
	tot=10**6
	inside=0
	
	for i in range(tot):
#		x=random.random()
#		y=random.random()
		x=0.5
		y=0.1
		
		if x**2+y**2<=1:
			inside+=1
	
	pi=str(inside/tot*4.)

	n=0
	global PI
	PI=[]
	for c in pi:
		if c!=".":
			PI+=[int(c)]
			n+=1
	return n

def get_digit(i):
	return PI[i]
