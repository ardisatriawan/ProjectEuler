import time
import math
start_time = time.clock()

MAX = 200000
isPrime = [False,False]

#fill with Trues
for i in xrange(2,MAX+1):
	isPrime.append(True)

#begin sieving
j = 2
for j in xrange(2,MAX+1):
	if isPrime[j] == True:
		k = j
		for k in xrange (2*k,MAX+1,k):
			isPrime[k] = False

i = 0	
count = 0		
while count<10001:
	if isPrime[i]:
		count += 1
	i += 1

print i-1
print "Running time:", time.clock() - start_time, "seconds"