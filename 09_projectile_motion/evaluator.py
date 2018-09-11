from turingarena import *

import math
import random


def theoric(h,v,theta):
	g=9.8
	vy=v*math.sin(theta/180*math.pi)
	t=(vy+math.sqrt(vy**2 + 2*g*h))/g
	return v*math.cos(theta/180*math.pi)*t
	


all_passed = True
for _ in range(10):
	h=int(random.random()*70.)
	v=10+int(random.random()*15.)
	theta=int(180*(random.random()-0.5))
	if _ == 0:
		theta=45
		h=70
		v=25
	if _ == 1:
		theta=-90
		v=25
	if _ == 2:
		theta=0
		h=1
		v=25
	if _ == 3:
		theta=85
		h=70
		v=25
	if h==0 and theta<=0:
		h=10
		
		
	print(f"h = {h}, v = {v}, theta = {theta}")
	try:
		with run_algorithm(submission.source) as process:
			process.procedures.set_initial_values(h,v,theta)
			while True:
				process.procedures.go_forward()
				landed=process.functions.is_landed()
				if landed == 1:
					break		
			gittata=process.functions.get_x()
			teo=theoric(h,v,theta)
			print(gittata, end='')
			if abs(gittata-teo)/teo>1:
				all_passed = False
				print(f" ---> Wrong!, correct value {teo}")
			else:
				print(" ---> Ok")
	except AlgorithmError as e:
		print(e)
		all_passed = False




evaluation.data(dict(goals=dict(correct=all_passed)))

