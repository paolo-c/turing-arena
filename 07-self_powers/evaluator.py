from turingarena import *

all_passed = True
N=[10,300,1000]
ans=[405071317,5028546760,9110846700]


for I in range(0,len(ans)):
	try:
		with run_algorithm(submission.source) as process:
			c = process.functions.S_n(N[I])
		if c == ans[I]:
			print(f"    last digits of S_{N[I]} --> {c} (Correct)")
		else:
			print(f"    last digits of S_{N[I]} --> {c} (Wrong!)")
			all_passed = False
		
	except AlgorithmError as e:
		print("error")
		all_passed = False




evaluation.data(dict(goals=dict(correct=all_passed)))
