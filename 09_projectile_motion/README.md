#                          PROJECTILE MOTION                             
#                             11/09/2018                                    



Suppose to have a projectile at a certain height **h** from the ground,
let him have a certain velocity **v** in a certain direction **theta**; 
when it lands, what is the horizontal distance from the starting point?

This is a classical problem that can be easily solved without computer's help.
However it is educative to solve it using integration methods such as euler's or runge-kutta's.
If you are not familiar with integration methods for differential equations, you may want to look at:
https://en.wikipedia.org/wiki/Euler_method


You will receive **h**, **v** and **theta** as input:
* **h** takes integer values from  0 to 70
* **v** takes integer values from 10 to 25
* **theta** is given in degrees, is an integer and it varies from -90 to 90

**HINT:** The choose of the size of the integration step is crucial, take it too small  and 
either you have numerical errors or the program takes too much time; take it too big and the
approximation of your integration methods does not hold.



