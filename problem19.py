import time
start_time = time.clock()

# 1 Jan 1901: Tuesday
sunday = 0
day = 2
for i in xrange(1901,2001):
	
	# January
	day += 31
	if day%7 == 0:
		sunday += 1
	
	# February, between 1901 - 2000 there is no century year
	# so just checking mod 4 is fine
	if i%4 == 0:
		day += 29
		if day%7 == 0:
			sunday += 1
	else:
		day += 28
		if day%7 == 0:
			sunday += 1
	
	# March
	day += 31
	if day%7 == 0:
		sunday += 1
	
	# April
	day += 30
	if day%7 == 0:
		sunday += 1
	
	# May
	day += 31
	if day%7 == 0:
		sunday += 1
		
	# June
	day += 30
	if day%7 == 0:
		sunday += 1
		
	# July
	day += 31
	if day%7 == 0:
		sunday += 1
		
	# August
	day += 31
	if day%7 == 0:
		sunday += 1
	
	# September
	day += 30
	if day%7 == 0:
		sunday += 1
	
	# October
	day += 31
	if day%7 == 0:
		sunday += 1
	
	# November
	day += 30
	if day%7 == 0:
		sunday += 1
		
	# December
	day += 30
	if day%7 == 0:
		sunday += 1

print sunday
print "Running time:", time.clock() - start_time, "seconds"