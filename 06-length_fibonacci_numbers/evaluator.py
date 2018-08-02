from turingarena import *

all_passed = True
N=[3,1000,10000,30000]
ans=[12,4782,47847,143547]


for I in range(0,len(ans)):
	try:
		with run_algorithm(submission.source) as process:
			c = process.functions.num_digits(N[I])
		if c == ans[I]:
			print(f"    num_digits({N[I]}) --> {c} (Correct)")
		else:
			print(f"    num_digits({N[I]}) --> {c} (Wrong!)")
			all_passed = False
		
	except AlgorithmError as e:
		print("error")
		all_passed = False




evaluation.data(dict(goals=dict(correct=all_passed)))
