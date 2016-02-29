import time
start_time = time.clock()

def poweroffive(n):
	return int(n)**5

def sumoffifthpowerdigits(n):
	return sum(map(poweroffive,str(n)))

totalsum = 0	
for i in xrange(2,354295):
	if i == sumoffifthpowerdigits(i):
		totalsum += i
print totalsum
print "Running time:", time.clock() - start_time, "seconds"