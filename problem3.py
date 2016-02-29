import time
import math
start_time = time.clock()

def isprime(n):
	if n == 0 or n == 1:
		return False
	elif n == 2:
		return True
	else:
		if n%2 == 0:
			return False
		else:
			for i in xrange (2,int(math.sqrt(n)+1)):
				if n%i == 0:
					return False
			return True

for i in xrange(1,771547):
	if isprime(i):
		if 600851475143%i == 0:
			maxfactor = i
	
print maxfactor
print "Running time:", time.clock() - start_time, "seconds"