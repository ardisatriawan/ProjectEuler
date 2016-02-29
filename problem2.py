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

sum = 0
n = 1
while fibo(n)<=4000000:
	if fibo(n)%2==0:
		sum += fibo(n)
	n += 1
print sum
print "Running time:", time.clock() - start_time, "seconds"