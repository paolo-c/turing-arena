#The Indian mathematician and astronomer Aryabhata in the 5th century gave the approximation of pi = 62832/20000 = 3.1416
#score expected 4

def compute_pi():
	pi=str(62832./20000.)
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
