from turingarena import *

def sol(N):
	V=[-1,-1,-1]
	for a in range(1,N):
		for b in range(a,N):
			c=N-a-b
			if c<=0:
				break

			if a*a+b*b==c*c:
				V=[a,b,c]
	return V			


all_passed = True
N=[3,12,40,90,516,523,1000]
for n in N:
	try:
		with run_algorithm(submission.source) as process:
			process.procedures.Find(n)
			V = [process.functions.get_element(i) for i in range(3)]
	except AlgorithmError as e:
		print(e)
		all_passed = False

	print(f"Find({n})=({V[0]}, {V[1]}, {V[2]})   ",end='')
#	if sum(V)==n and V[0]**2+V[1]**2==V[2]**2:
	if sol(n)==V:
		print("Correct!")
	else:
		print("WRONG!")
		all_passed = False



evaluation.data(dict(goals=dict(correct=all_passed)))
