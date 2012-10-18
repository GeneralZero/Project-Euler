#!/usr/bin/env python
from time import time

abund_nums = None

def factors(num):    # Stole from Stack Overflow
	return set(reduce(list.__add__, 
				([i, num/i] for i in range(1, int(num**0.5) + 1) if num % i == 0 )))

def sum_of_abundents(number): 
	return any(number-a in abund_nums for a in abund_nums) # Found this nifty python function any()

def abundants(limit):
	abund = []
	for x in range(1, limit+1):
		if sum(factors(x)) - x > x:
			abund.append(x)
	return set(abund) #returning the set decreaces the runtime


if __name__ =="__main__":
	start = time()

	abund_nums = abundants(28124)

	print "Answer to Problem time: ", sum(i for i in range(1,28124) if not sum_of_abundents(i))
	print "Completed in: %f seconds" % (time() - start)