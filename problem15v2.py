import time
import math
start_time = time.clock()

def NumberOfPath(x,y):
	if x == 0 or y == 0:
		return 1
	else:
		return NumberOfPath(x-1,y) + NumberOfPath(x,y-1)
		
print NumberOfPath(20,20)
print "Running time:", time.clock() - start_time, "seconds"