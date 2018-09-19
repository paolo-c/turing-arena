#                       	 Darts                             
#                       19/09/2018    


In the classic pub game of darts, at each round, players throw 3 darts 
at a dartboard, each region of the dartboard has a score.
Players usually starts from 301 or 501, and the goal is to reach the exact zero.

This problem is the 109th of the project euler, you have to read before proceeding with the problem
https://projecteuler.net/problem=109

We want to write a function *count_checkouts(N)* that tells how many possible
chekouts exits if your current score is *N*

As in the euler problem, we consider two checkouts to be equal if they end on 
the same double and the first two darts differs only on the order.
For instance the checkouts 
		S1 S2 D2  is equal to S2 S1 D2

while 
		S1 D3 D2  differs from  S1 D2 D3
