import time
import math
start_time = time.clock()

def NumOfDivisor(n):
	divisor = [1,n]
	for i in xrange(2,int(math.sqrt(n))+1):
		if n%i==0:
			divisor.append(i)
			if i!=n/i:
				divisor.append(n/i)
	return len(divisor)

def triangle(n):
	return (n**2+n)/2

i = 8
while NumOfDivisor(triangle(i))<500:
	i+=1

print triangle(i)
print "Running time:", time.clock() - start_time, "seconds"