import time
start_time = time.clock()

def poweroffive(n):
	powof5 = [0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049]
	return powof5[int(n)]

def sumoffifthpowerdigits(n):
	return sum(map(poweroffive,str(n)))

totalsum = 0	
for i in xrange(2,354295):
	if i == sumoffifthpowerdigits(i):
		totalsum += i
print totalsum
print "Running time:", time.clock() - start_time, "seconds"