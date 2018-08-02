from turingarena import *

all_passed = True
N=[12,40,90,516,1000]
for n in N:
	try:
		with run_algorithm(submission.source) as process:
			process.procedures.Find(n)
			V = [process.functions.get_element(i) for i in range(3)]
	except AlgorithmError as e:
		print(e)
		all_passed = False

	print(f"Find({n})=({V[0]}, {V[1]}, {V[2]})   ",end='')
	if sum(V)==n and V[0]**2+V[1]**2==V[2]**2:
		print("Correct!")
	else:
		print("WRONG!")
		all_passed = False

N=[3,523]
for n in N:
	try:
		with run_algorithm(submission.source) as process:
			process.procedures.Find(n)
			V = [process.functions.get_element(i) for i in range(3)]
	except AlgorithmError as e:
		print(e)
		all_passed = False

	print(f"Find({n})=({V[0]}, {V[1]}, {V[2]})   ",end='')
	if V==[-1,-1,-1]:
		print("Correct!")
	else:
		print("WRONG!")
		all_passed = False



evaluation.data(dict(goals=dict(correct=all_passed)))
