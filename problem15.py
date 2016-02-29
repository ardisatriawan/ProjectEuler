import time
import math
start_time = time.clock()

# After some drawing I got: 
# for 0x0 grid: obviously 1
# for 1x1 grid: 2 (1 right-bottom + 1 bottom right)
# for 2x2 grid: 6 (example)
# for 3x3 grid: 20 paths

# now that I got 1,2,6,20 -> enter that into The Online Encyclopedia of Integer Sequence (http://oeis.org)
# got this: https://oeis.org/A000984 : C(2*n,n) = (2*n)!/(n!)^2 now let's implement that for n = 20

#              40!      40 x 39 x 38 x 37 x 36 x 35 x 34 x 33 x 32 x 31 x 30 x 29 x 28 x 27 x 26 x 25 x 24 x 23 x 22 x 21 x 20!
# C(40,20) = -------- = -------------------------------------------------------------------------------------------------------
#             20!20!    20 x 19 x 18 x 17 x 16 x 15 x 14 x 13 x 12 x 11 x 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 x 20!

print (40*39*38*37*36*35*34*33*32*31*30*29*28*27*26*25*24*23*22*21)/(20*19*18*17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2*1)
print "Running time:", time.clock() - start_time, "seconds"
