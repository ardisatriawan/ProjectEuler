import time
start_time = time.clock()

lengthmap = {}

def next(n):
	# return next number after n in collatz sequence
	if n%2 == 0:
		return n/2
	else:
		return 3*n+1

def length(n):
	# length of collatz sequence
	init = n
	length = 1
	while n>1:
		# jika n ada di cache
		if n in lengthmap:
			# masukkan ke dalam cache:
			lengthmap[init] = length + lengthmap[n] - 1
			# return panjangnya
			return length + lengthmap[n] - 1
		else:
			length += 1
			n = next(n)
	
	# masukkan ke dalam cache:
	lengthmap[init] = length
	# return
	return length

max = 0
startingmax = 0
for i in xrange(2,1000000):
	if length(i)>max:
		max = length(i)
		startingmax = i
print startingmax
print "Running time:", time.clock() - start_time, "seconds"