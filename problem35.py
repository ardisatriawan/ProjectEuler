import time
start_time = time.clock()

# generating primes function
# source: http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
def get_primes(n):
	numbers = set(range(n, 1, -1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n+1, p)))
	return primes
	
def is_circular(n, primes):
	#check if n is a circular prime
	n = str(n)
	for i in xrange(len(str(n)),0,-1):
		num = n[i:]+n[:i]
		if int(num) not in primes:
			return False
	return True
	
#generate all the primes
primes = get_primes(1000000)
count = 0
for n in primes:
	#print n
	if is_circular(n,primes):
		count += 1

print count

print "Running time:", time.clock() - start_time, "seconds"
