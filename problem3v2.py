import time
import math
start_time = time.clock()

MAX = 771546
isprime = [False,False]

#fill with Trues
for i in xrange(2,MAX+1):
	isprime.append(True)

#begin sieving
j = 2
for j in xrange(2,MAX+1):
	if isprime[j] == True:
		k = j
		for k in xrange (2*k,MAX+1,k):
			isprime[k] = False

for i in xrange(1,MAX+1):
	if isprime[i]:
		if 600851475143%i == 0:
			maxfactor = i
	
print maxfactor
print "Running time:", time.clock() - start_time, "seconds"