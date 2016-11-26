from gmpy2 import is_prime
from gmpy2 import next_prime
from time import clock

start_time = clock()

def isTruncatable(n):
	nleft = str(n)
	nright = str(n)
	
	# check from left
	while len(nleft) > 0:
		if not is_prime(int(nleft)):
			return False
		nleft = nleft[:-1]
	
	# check from right
	while len(nright) > 0:
		if not is_prime(int(nright)):
			return False
		nright = nright[1:]
	
	return True
	
# according to the problem description, there are 11 truncatable primes
# just count and sum them until 11, start from 23
count = 0
sum = 0
prime = 23
while count != 11:
	if isTruncatable(prime):
		sum += prime
		count += 1
	prime = next_prime(prime)

print sum
print "Running time:", clock() - start_time, "seconds"