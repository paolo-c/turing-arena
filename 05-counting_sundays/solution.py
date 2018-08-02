def isleap(a):
	if a%400==0:
		return 1
	if a%100==0:
		return 0
	if a%4==0:
		return 1
	return 0
def num_days(g,m,a):
	month=[31,28,31,30,31,30,31,31,30,31,30,31]
	nleap=int((a-1-1900)/4.)
	g+=sum(month[:m-1])
	g+=(a-1900)*365+nleap
	if m>2 and isleap(a)==1:
		g+=1
	return int(g)


def num_sundays(D,M,Y):
	n=0
	for a in range(1901,Y+1):
		for m in range(1,M+1):
			if num_days(1,m,a)%7==0:
				n+=1
	return int(n)
	
