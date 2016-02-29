import time
start_time = time.clock()

def sumofdigits(n):
	return sum(map(int,str(n)))
	
print sumofdigits(2**1000)
print "Running time:", time.clock() - start_time, "seconds"