#!/usr/bin/env python
from time import time

		
def factors(num):    # Stole from Stack Overflow
	return reduce(list.__add__, 
				([i, num/i] for i in range(1, int(num**0.5) + 1) if num % i == 0 ))

def run(limit):
	sums=0
	x=1
	while x <= limit:
		functionD = sum(factors(x)) - x						# Remove the number from the sum 
		functionDD = sum(factors(functionD)) - functionD	# Remove the number from the sum 
		if functionDD == x and x!= functionD:
			sums += functionD + functionDD 
			x = max(functionD, functionDD)+1 				
			#print functionD, functionDD
		else:
			x +=1
	return sums

if __name__ =="__main__":
	start = time()


	print "Answer to Problem 21: ", run(10000)
	print "Completed in: %f seconds" % (time() - start)