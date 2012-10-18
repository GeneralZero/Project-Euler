#!/usr/bin/env python
from time import time
import re
from decimal import *
getcontext().prec = 10000

def dec_len(num):
	dec_str = str(num)[2:20]
	ret = re.findall(r'(\d+?)\1', dec_str)
	if not ret:
		return 0
	else:
		return len(max(ret, key=len))


def run(limit):
	max =[0.5, 1]
	for x in range(3, limit + 1):
		dec = Decimal(1.00/x)
		if max[1] < dec_len(dec):
			print dec, dec_len(dec), "Number: ", x
			max = [dec, dec_len(dec)]


if __name__ =="__main__":
	start = time()


	print "Answer to Problem 26: ", run(1000)
	print "Completed in: %f seconds" % (time() - start)