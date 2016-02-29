import itertools
import time
start_time = time.clock()

A = '0123456789'
Aperm = list(map("".join,itertools.permutations(A)))
print Aperm[999999]
print "Running time:", time.clock() - start_time, "seconds"