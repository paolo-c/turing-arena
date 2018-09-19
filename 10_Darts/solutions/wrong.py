# evaluation_assert not data["goals"]["correct"]

def lists(N,depth,current):

	result=[]

	if N<0 or depth==3:
		return []
		
	for i in range(1,min(int(N/3)+1,21)):
		if i*3==N:
			result+=[["T "+str(i)]+current]
		else:
			result+=lists(N-i*3,depth+1,["T "+str(i)]+current)

	
	Range=list(range(1,min(int(N/2)+1,21)))
	if N>=50:
		Range+=[25]
	for i in Range: 
		if i*2==N:
			result+=[["D "+str(i)]+current]
		else:
			result+=lists(N-i*2,depth+1,["D "+str(i)]+current)


	Range=list(range(1,min(int(N)+1,21)))
	if N>=25:
		Range+=[25]
	for i in Range:
		if i==N:
			result+=[["S "+str(i)]+current]
		else:
			result+=lists(N-i,depth+1,["S "+str(i)]+current)
		
	return result
	


def lists_checkouts(N):
	result=[]

	Range=list(range(1,min(int(N/2)+1,21)))
	if N>=50:
		Range+=[25]

	for i in Range:
		if i*2==N:
			result=[["D "+str(i)]]+result
		else:
			result=lists(N-i*2,1,["D "+str(i)])+result
			
	return result


def count_checkouts(N):
	return len(lists_checkouts(N))
