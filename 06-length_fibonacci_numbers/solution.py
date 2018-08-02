#The number of digits in a number can be calculated as follows:
#Digits = int(math.log10(number)) + 1

import math


def num_digits(N):
	counter = 0
	a, b = 0, 1

	while int(math.log10(b)) + 1 <= N:
		a,b = b, a+b
		counter += 1
		if int(math.log10(a)) + 1 == N:
			return int(counter)
