#score expected 2
def compute_pi():
	pi=str(25./8.)
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
