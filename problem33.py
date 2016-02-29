import time
from fractions import gcd
start_time = time.clock()

def simplifydenum(a,b):
	# fungsi untuk menyederhanakan pecahan a/b
	# yang direturn cuma penyebut
	return b/gcd(a,b)

num = 1
denum = 1
for a in xrange(1,10):
	for b in xrange(1,10):
		for x in xrange(1,10):
			if ((10*a-b)*x == 9*a*b) and (9*x > (10*a-b)):
				num *= a
				denum *= b
print simplifydenum(num,denum)
print "Running time:", time.clock() - start_time, "seconds"