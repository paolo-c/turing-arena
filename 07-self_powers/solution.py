last=10

def power(N):
	if N==1:
		return 1
	p=1
	for i in range(0,N):
		p*=N
		p=p%(10**last)
	return p
		

def S_n(N):
	s=0
	for n in range(1,N+1):
		s+=power(n)
		s=s%(10**last)
	return s

