import time
from fractions import gcd
start_time = time.clock()

# center
totalsum = 1

# top right
for n in xrange(3,1003,2):
	totalsum += n**2
	
# bottom right
for n in xrange(3,1003,2):
	totalsum += n**2 - 3*n + 3
	
# top left
for n in xrange(3,1003,2):
	totalsum += n**2 - n + 1

# top right
for n in xrange(3,1003,2):
	totalsum += n**2 - 2*n + 2
	
# total
print totalsum
print "Running time:", time.clock() - start_time, "seconds"