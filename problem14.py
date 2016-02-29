import time
start_time = time.clock()
def CollatzLength(n):
	len = 1
	while n>1:
		if n%2==0:
			n /= 2
		else:
			n = 3*n+1
		len+=1
	return len

# print CollatzLength(3)
max = 0
startingmax = 0
for i in xrange(2,1000000):
	if CollatzLength(i)>max:
		max = CollatzLength(i)
		startingmax = i
print startingmax
print "Running time:", time.clock() - start_time, "seconds"