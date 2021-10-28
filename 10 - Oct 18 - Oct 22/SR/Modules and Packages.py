## namespace - the place where there are not two different objects of the same name
##	names must be unique
##	
## How you import makes a difference
##  
##
##	import - all the names defined in the module become known, 
##	            but they don’t enter your code’s namespace.
##	            - I could have my OWN pi or sin() function
##	            - Have to use the module name if  you import as above

import math	            
print(math.sin(math.pi/2))
	            
# -do example with self defined pi

import math

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

	            
##	Second Method:
##		from math import sin, pi
##		
##		-names don't need qualification
##		-redo above code without module name
##		--do with self defined pi and sin (changes the value instead of making a 'new' pi

from math import sin, pi
print(sin(pi/2))

	
##	Third method
##		from math import *
##		
##		-All elements become part of the namespace
##		-Be sure you don't have conflicts
##		-Not really safe, use sparingly if at all
		

##	Using an alias
##		import math as M
##			(Didn't we do this on the GPIO project?)
##			can't use the real module name - must use alias

import math as m
print(m.sin(m.pi/2))



----------------
Standard Modules

#dir(math) - Not the same as windows dir

import math
	
	
for name in dir(math):
    print(name)
		
#	trig function use radians!!!
	
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)


	
##	ceil(x)→ the ceiling of x (the smallest integer greater than or equal to x)
##	floor(x)→ the floor of x (the largest integer less than or equal to x)
##	trunc(x)→ the value of x truncated to an integer (be careful – it’s not an equivalent either of ceil or floor)
##	factorial(x)→ returns x! (x has to be an integral and not a negative)
##	hypot(x,y)→ returns the length of the hypotenuse of a right-angle triangle with the leg lengths equal to x and y (the same as sqrt(pow(x,2)+pow(y,2)) but more precise)
	
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))


## random
##	A random number generator takes a value called a seed, treats it as an input value, calculates a “random” number based on it
##	-sooner or later it WILL repeat
##	-sometime we seed with time
##	-python does it automatically on import
	
from random import random
for i in range(5)
    print (random())
		
		- add seed(0) before the loop
		
		-better??
		randrange(end)
		randrange(beg,end)
		randrange(beg, end, step)
		randint(left, right)
		
		Picking items at random
		
			from random import choice, sample
			lst = [1,2,3,4,5,6,7,8,9,10]
			print(choice(lst))
			print(sample(lst, 5))
			print(sample(lst, 10))
			
# platform module

from platform import platform
	print(platform())
	print(platform(1))
	print(platform(0,1))
	print(machine())
	print(processor())
	print(system())
	print(version())


______


Packages - Holds a bunch of modules
	
	Make two files
		mymodule.py
		main.py (imports mymodule)
		
	Run main.py
		look in the folder
		 __pychache__    (What's inside?)
		 name of the file is the same as your module name
		 numbers are python version
		  - it is semi-complied code ready for the interpreter
		  	-doesn't need a lot of chcks before starting
		  	
		do 5.1.3.1 to 5.1.3.10
		 
