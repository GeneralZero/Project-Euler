#!/usr/bin/env python
from time import time

def changes(amount, coins):
	ways = [0] * (amount + 1)
	ways[0] = 1
	for coin in coins:
		for j in xrange(coin, amount + 1):
			ways[j] += ways[j - coin]
	return ways[amount]
 
print 


if __name__ =="__main__":
	start = time()


	print "Answer to Problem 31: ", changes(200, [1, 2, 5, 10, 20, 50, 100, 200])
	print "Completed in: %f seconds" % (time() - start)