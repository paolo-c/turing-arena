def sum(N):
	assert N>0
	t=0
	for i in range(1,N):
		if i%3==0 or i%5==0:
			t+=i
		
	return t
