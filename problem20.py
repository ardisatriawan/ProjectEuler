import time
import math
start_time = time.clock()

def sumofdigits(n):
	return sum(map(int,str(n)))
	
print sumofdigits(math.factorial(100))
print "Running time:", time.clock() - start_time, "seconds"