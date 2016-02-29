import time
import math
start_time = time.clock()

def gcd(a,b):
	if b == 0:
		return a
	else:
		return gcd(b, a%b)
		
def lcm(a,b):
	return a*b/gcd(a,b)
	
def lcmm(*args):
	return reduce(lcm,args)

print lcmm(*range(1,21))	
print "Running time:", time.clock() - start_time, "seconds"