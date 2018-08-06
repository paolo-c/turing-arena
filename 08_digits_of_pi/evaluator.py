from turingarena import *
import math

pi=str(math.pi)

max_n=0
ANS=[]
for c in pi:
	if c!=".":
		ANS+=[int(c)]
		max_n+=1

print(f"Max score {max_n}")
score=0

all_passed = True
try:
	with run_algorithm(submission.source) as process:
		n=process.functions.compute_pi()
		V = [process.functions.get_digit(i) for i in range(n)]
except AlgorithmError as e:
	print(e)
	all_passed = False


your_pi=0
while score<min(max_n,n) and V[score]==ANS[score]:
	your_pi+=V[score]*10.**(-score)
	score+=1
print(f"Your score is {score}")
print(your_pi)

evaluation.data(dict(goals=dict(correct=all_passed)))
