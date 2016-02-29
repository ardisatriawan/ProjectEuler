import time
start_time = time.clock()

def ways(target,avc):
	coins = [1,2,5,10,20,50,100,200]
	if avc <= 0:
		return 1
	res = 0
	while target >= 0:
		res = res + ways ( target , avc -1)
		target = target - coins [avc]
	return res

print ways(200,7)
print "Running time:", time.clock() - start_time, "seconds"