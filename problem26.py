import time
start_time = time.clock()

def RecurrenceLength(n):
	remainder = []
	i = 10%n
	while i not in remainder:
		if i == 0:
			return 0
		remainder.append(i)
		i = (i*10)%n
	return len(remainder) - remainder.index(i)
	
longest = 0;
for d in xrange(1,1001):
	if RecurrenceLength(d) > longest:
		longest = RecurrenceLength(d)
		longest_den = d

print longest_den
print "Running time:", time.clock() - start_time, "seconds"