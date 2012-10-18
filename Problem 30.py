#!/usr/bin/env python
from time import time

to_power = 5

def power(base, exp):
	ret = 1
	for x in range(exp):
		ret *= base
	return ret

def run(limit):
	total_sum =0
	for nums in range(2,limit):
		sum =0
		for digits in str(nums):
			sum += power(int(digits), to_power)
		if sum == nums:
			#print nums
			total_sum += nums

	return total_sum

if __name__ =="__main__":
	start = time()


	print "Answer to Problem 30: ", run(500000)
	print "Completed in: %f seconds" % (time() - start)



