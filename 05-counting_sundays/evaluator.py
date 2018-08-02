from turingarena import *

all_passed = True
D=[24,31,5]
M=[3,12,10]
Y=[1988,2000,2121]
ans=[32225,36890,80998]
ansS=[38,171,315]


for I in range(0,len(ans)):
	try:
		with run_algorithm(submission.source) as process:
			c = process.functions.num_days(D[I],M[I],Y[I])
			s = process.functions.num_sundays(D[I],M[I],Y[I])
		if c == ans[I]:
			print(f"    num_days({D[I]},{M[I]},{Y[I]}) --> {c} (Correct)")
		else:
			print(f"    num_days({D[I]},{M[I]},{Y[I]}) --> {c} (Wrong!)")
			all_passed = False
		if s == ansS[I]:
			print(f" num_sundays({D[I]},{M[I]},{Y[I]}) --> {s} (Correct)")
		else:
			print(f" num_sundays({D[I]},{M[I]},{Y[I]}) --> {s} (Wrong!)")
			all_passed = False
	except AlgorithmError as e:
		print("error")
		all_passed = False

	print("")



evaluation.data(dict(goals=dict(correct=all_passed)))
