#!/usr/bin/env python
from time import time

Months = [31,28,31,30,31,30,31,31,30,31,30,31]
def run(limit):
	total = 0
	day = 0
	for year in range(1900,limit):
		for x in Months:
			if (year % 4 == 0) and x == 2:
				day = (day+29)% 7
			else:
				day = (day+x)% 7
			if day == 0:
				total+=1
	return total

if __name__ =="__main__":
	start = time()

	print "Answer to Problem 19:", run(2000)
	print "Completed in: %f seconds" % (time() - start)