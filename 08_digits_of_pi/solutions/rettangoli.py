#score expected 9
def C(x):
	return (1.-x*x)**0.5
	

def compute_pi():
	N=10**6
	step=2./N
	Area=0.

	for i in range(0,N):
		Area+=C(-1+i*step)*step
	
	pi=str(Area*2.)

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
