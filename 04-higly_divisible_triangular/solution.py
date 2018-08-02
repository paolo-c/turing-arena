#w/o prime table
def tri(n):
	return int(n*(n+1)/2)


def add(v,n):
	for i in v:
		if n==i:
			return v
	v+=[n]
	return v

def num_div(N,d=None):

	if d is None:
		d=[1]	
	if N==1:
		return len(d)
		
	new=2
	while N%new!=0:
		new+=1
	
	newd=[]
	for i in d:
		newd+=[i]
	for i in d:
		add(newd,i*new)
	
	return 	num_div(N/new,newd)	

def num(Nd):

	d=0
	n=1
	while d<Nd:
		d=num_div(tri(n))
		n+=1

	return tri(n-1)
