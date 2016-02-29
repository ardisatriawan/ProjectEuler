import time
import string
start_time = time.clock()

def score(n):
	# get 'abcdefghijklmnopqrstuvwxyz'
	alphabet = string.lowercase
	
	#lowering the case of n
	n = n.lower()
	
	# remove the quotation marks
	n = n[1:-1]
	
	# calculatescore
	wordscore = 0;
	for i in n:
		wordscore += alphabet.index(i)+1
		
	return wordscore

# this part is for opening and closing file
fo = open("problem22_names.txt","r")
names = fo.readlines()
fo.close()

# convert it into list and sort it
names = names[0].split(',')
list.sort(names)

# calculate total score
totalscore = 0
for i in xrange (0,len(names)):
	totalscore += (i+1)*score(names[i])

# print it
print totalscore
print "Running time:", time.clock() - start_time, "seconds"