import math
import time
start_time = time.clock()

def fibo(n):
		if (n==1):
		return 1
	elif (n==2):
		return 2
	else:
		a = 1
		b = 2
		
		i = 3
		while i<=n:
			c = a + b
			a = b
			b = c
			i += 1
		return c

def NumOfDigits(n):
	return int(math.log10(n))+1

i = 1
while NumOfDigits(fibo(i)) != 1000:
	i+=1
	print i

print i
print "Running time:", time.clock() - start_time, "seconds"