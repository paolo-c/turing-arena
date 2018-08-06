#score expected 15

def compute_pi():

	N=10
	a=1./5.
	b=1./239.
	a2=a*a
	b2=b*b
	sign=1.

	tot=4.*a-b
	for i in range(1,N):
		sign*=-1
		a*=a2
		b*=b2	
		tot+=sign/(2.*i+1.)*(4.*a-b)
	
	pi=str(4.*tot)
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
