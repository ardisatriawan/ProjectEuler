import time
start_time = time.clock()

def sumoffifthpowerdigits(n):
	num = str(n)
    sum = 0
    for i in xrange(0,len(num)):
        sum += int(num[i])**5
    return sum
	
totalsum = 0	
for i in xrange(2,354295):
	if i == sumoffifthpowerdigits(i):
		totalsum += i
print totalsum
print "Running time:", time.clock() - start_time, "seconds"