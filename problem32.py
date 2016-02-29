import time
start_time = time.clock()

def is9Pandigital(n):
	a = map(int,str(n))
	
	if len(a)!=9:
		return False
	
	for i in xrange(1,10):
		if i not in a:
			return False
	return True

pandigital_num = []	

#1 digit dikali 4 digit
for a in xrange(1,10):
	for b in xrange(1000,10000):
		c = a*b
		if is9Pandigital(str(a)+str(b)+str(c)):
			if c not in pandigital_num:
				#print a,"*",b,"=",c
				pandigital_num.append(c)

#2 digit dikali 3 digit				
for a in xrange(10,100):
	for b in xrange(100,1000):
		c = a*b
		if is9Pandigital(str(a)+str(b)+str(c)):
			if c not in pandigital_num:
				#print a,"*",b,"=",c
				pandigital_num.append(c)

print sum(pandigital_num)
print "Running time:", time.clock() - start_time, "seconds"