import time
start_time = time.clock()

def ispalindrome(n):
	return str(n) == str(n)[::-1]

maxpalindrome = 0
for i in xrange(110,1000,11):
	for j in xrange(101,1000):
		if ispalindrome(i*j):
			if i*j>maxpalindrome:
				maxpalindrome = i*j

print maxpalindrome
print "Running time:", time.clock() - start_time, "seconds"