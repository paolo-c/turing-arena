from turingarena import *

all_passed = True
N  =[3,4 ,6 ,56,101,169,170,190]
ans=[1,4,11,728,207, 0  ,1  ,0]


for I in range(len(ans)):
	try:
		with run_algorithm(submission.source) as process:
			c = process.functions.count_checkouts(N[I])
		if c == ans[I]:
			print(f"    count_checkouts({N[I]})={c} --> {ans[I]} (Correct)")
		else:
			print(f"    count_checkouts({N[I]})={c} --> {ans[I]} (Wrong!)")
			all_passed = False
		
	except AlgorithmError as e:
		print("error")
		all_passed = False




evaluation.data(dict(goals=dict(correct=all_passed)))
