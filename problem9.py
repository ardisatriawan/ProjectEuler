import time
import math
start_time = time.clock()
for b in xrange(1,1000):
	for a in xrange(1,b):
		if a*(1000-b) + 1000*b == 500000:
			mul = a*b*(1000-a-b)
print mul
print "Running time:", time.clock() - start_time, "seconds"