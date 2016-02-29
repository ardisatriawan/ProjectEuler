import time
import math
start_time = time.clock()

def SumOfDivisor(n):
	divisor = [1]
	for i in xrange(2,int(math.sqrt(n))+1):
		if n%i==0:
			divisor.append(i)
			if i!=n/i:
				divisor.append(n/i)
	return sum(divisor)
	
# create list of all abundant numbers
abundant = []
for i in xrange(12,28124):
	if SumOfDivisor(i)>i:
		abundant.append(i)

# create list of numbers, "False" = can't be written as 2 abundant sum
# "True" = can be written as 2 abundant sum
canbewritten = [False]*28124
for i in abundant:
	for j in abundant:
		if (i+j <= 28123):
			canbewritten[i+j] = True
		
# sum all the false:
sumcannot = 0
for i in xrange(0,28124):
	if not canbewritten[i]:
		sumcannot += i

# print items
print sumcannot
print "Running time:", time.clock() - start_time, "seconds"