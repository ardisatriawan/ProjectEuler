import time
start_time = time.clock()

def sumoffifthpowerdigits(n):
	powof5 = [0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049]
	num = str(n)
	sum = 0
	for i in xrange(0,len(num)):
		sum += powof5[int(num[i])]
	return sum
	
totalsum = 0	
for i in xrange(2,354295):
	if i == sumoffifthpowerdigits(i):
		totalsum += i
print totalsum
print "Running time:", time.clock() - start_time, "seconds"