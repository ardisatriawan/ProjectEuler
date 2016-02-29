import time
import math
import numpy
start_time = time.clock()

def NumberOfPath(x,y):
	grid = numpy.ones((x+1,y+1))
	for i in xrange (1,x+1):
		for j in xrange (1,y+1):
			grid[i][j] = grid[i-1][j] + grid[i][j-1]
	return int(grid[x][y])

print NumberOfPath(20,20)
print "Running time:", time.clock() - start_time, "seconds"