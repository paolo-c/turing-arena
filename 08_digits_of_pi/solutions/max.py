#score expected 16
import math

def compute_pi():
	pi=math.pi
	n=0
	global PI
	PI=[]
	while pi!=0:
		PI+=[int(pi)]
		n+=1
		pi-=int(pi)
		pi*=10

	return len(PI)	
	
def get_digit(i):
	return PI[i]
