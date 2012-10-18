#!/usr/bin/env python
from time import time

def nextFib(curentfib,prevfib):
	return curentfib+prevfib

def run(str_length):
	fib1=1
	fib2=1
	fib3=0
	i=2
	while(len(str(fib1))<str_length):
		fib3=fib2
		fib2=fib1
		fib1=nextFib(fib2,fib3)
		i=i+1
	return	[i, fib1]

if __name__ =="__main__":
	start = time()

	print "Answer to Problem 25: ",  run(1000)[0]
	print "Completed in: %f seconds" % (time() - start)