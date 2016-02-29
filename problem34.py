import time
start_time = time.clock()

def factorial19(n):
	if n=="0":
		return 1
	elif n=="1":
		return 1
	elif n=="2":
		return 2
	elif n=="3":
		return 6
	elif n=="4":
		return 24
	elif n=="5":
		return 120
	elif n=="6":
		return 720
	elif n=="7":
		return 5040
	elif n=="8":
		return 40320
	else: #n=="9"
		return 362880

def sumoffact(n):
	return sum(map(factorial19,str(n)))

totalsum = 0	
for i in xrange(10,2540161):
	if i == sumoffact(i):
		totalsum += i
print totalsum
print "Running time:", time.clock() - start_time, "seconds"