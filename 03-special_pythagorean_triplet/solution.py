def Find(N):
	global V
	V=[-1,-1,-1]
	for a in range(1,N):
		for b in range(a,N):
			c=N-a-b
			if c<=0:
				break

			if a*a+b*b==c*c:
				V=[a,b,c]

def get_element(i):
    return V[i]
