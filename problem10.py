import time
import math
start_time = time.clock()

MAX = 2000000
#fill with Trues
isPrime = [True]*(MAX+1)
isPrime[0] = False
isPrime[1] = False

#begin sieving
for j in xrange(2,MAX+1):
	if isPrime[j] == True:
		k = j
		for k in xrange (2*k,MAX+1,k):
			isPrime[k] = False
print "Sieving time:", time.clock() - start_time, "seconds"
			
sumofprimes = 0
for i in xrange(2,2000000):
	if isPrime[i]:
		sumofprimes += i
		
print sumofprimes
print "Running time:", time.clock() - start_time, "seconds"