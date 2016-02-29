import time
start_time = time.clock()

count = 1 #200 penny by itself
for a in xrange(0,101):
	for b in xrange(0,41):
		for c in xrange(0,21):
			for d in xrange(0,11):
				for e in xrange(0,5):
					for f in xrange(0,3):
						if a*2 + b*5 + c*10 + d*20 + e*50 + f*100 <= 200:
							count += 1

print count
print "Running time:", time.clock() - start_time, "seconds"