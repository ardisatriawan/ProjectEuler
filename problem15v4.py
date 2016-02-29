import time
import math
start_time = time.clock()

def NumberOfPath(x,y):
	return math.factorial(x+y) / (math.factorial(x) * math.factorial(y))

print NumberOfPath(20,20)
print "Running time:", time.clock() - start_time, "seconds"