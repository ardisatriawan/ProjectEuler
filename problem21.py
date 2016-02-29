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
	
def IsAmicable(n):
	return n == SumOfDivisor(SumOfDivisor(n)) and n != SumOfDivisor(n)

AmicableSum = 0
for i in xrange(1,10000):
	if IsAmicable(i):
		AmicableSum += i

print AmicableSum
print "Running time:", time.clock() - start_time, "seconds"