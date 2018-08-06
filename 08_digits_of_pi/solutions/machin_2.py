#score expected 16

def compute_pi():

	digits_target=20
	n=0
	global PI
	PI=[]

	a=1./5.
	b=1./239.
	a2=a*a
	b2=b*b
	sign=1.

	i=0
	coef=4.
	new=coef*(4.*a-b)
	old=1
	
	while n<digits_target:
		i+=1
		old=new
		
		sign*=-1
		a*=a2
		b*=b2
#		coef+=8./(1.-4.*i*i)
		coef=4./(2.*i+1.)
		new+=sign*coef*(4.*a-b)
	
		while abs(new-old)<0.1:
			n+=1
			PI+=[int(new)]
			new-=int(new)
			new*=10.
			old-=int(old)
			old*=10.
			a*=10.
			b*=10.
	return n

#compute_pi()


	
def get_digit(i):
	return PI[i]


