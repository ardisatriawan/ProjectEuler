import time

start_time = time.clock()
def isDBPalindrome(A):
	# check whether A is a palindrome in base 2 and base 10
	return str(A) == str(A)[::-1] and bin(A)[2:] == bin(A)[2:][::-1]

sum = 0
for i in xrange(1,1000000,2):
	if isDBPalindrome(i):
		sum += i

print sum
print "Running time:", time.clock() - start_time, "seconds"