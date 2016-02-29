import time
import math
start_time = time.clock()

sumofsquare = 0
sum = 0
for i in xrange(1,101):
	sum += i
	sumofsquare += i**2

print sum**2-sumofsquare
print "Running time:", time.clock() - start_time, "seconds"