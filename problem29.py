import time
start_time = time.clock()

results = []
for a in xrange(2,101):
	for b in xrange (2,101):
		c = a**b
		if c not in results:
			results.append(c)
print len(results)
print "Running time:", time.clock() - start_time, "seconds"