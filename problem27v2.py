import time
start_time = time.clock()

########### Sieve of eratosthenes ################
MAX = 100**2 + 1000*100 + 1000
#fill with Trues
isPrime = [True]*(MAX+1)
isPrime[0] = False
isPrime[1] = False

#begin sieving
for j in xrange(2,MAX+1):
	if isPrime[j] == True:
		k = j
		if k*k<MAX+1:
			for k in xrange (k*k,MAX+1,k):
				isPrime[k] = False
print "Sieving time:", time.clock() - start_time, "seconds"
################### End sieve ##################

# Function to calculate length
def length(a,b):
	# a, b -> coefficient of n**2 + a*n + b
	n = 0
	while (isPrime[n**2 + a*n +b]):
		n += 1
	return n
	
# Now generate the longest chain:
longest = 0
for a in xrange(-1000,1000):
	for b in xrange(2,1000):
		if length(a,b) > longest:
			longest = length(a,b)
			answer = a*b

print answer
print "Running time:", time.clock() - start_time, "seconds"