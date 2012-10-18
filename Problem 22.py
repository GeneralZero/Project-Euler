#!/usr/bin/env python
from time import time

def nameToNum(string1):
	sum=0
	i=0
	while(i<len(string1)):
		sum=sum+lettersToNumbers(string1[i])
		i=i+1
	return int(sum)
	
def lettersToNumbers(char):
	if(char >= "A") or (char <= "Z"):
		return ord(char) -64
	else:
		return 0
	
def sortlist(filename):
	namefile = open(filename)
	lists= namefile.readline().replace('\"','').split(',')
	sortedlist = sorted(lists,key=str.upper)
	return sortedlist

def run(file_name):
	lists = sortlist(file_name)
	i=1
	sum=0
	for name in lists:
		a=i*nameToNum(name)
		sum=sum+a
		#print nameToNum(name), i, name,a
		i=i+1
	return sum

if __name__ =="__main__":
	start = time()


	print "Answer to Problem 22: ", run("Problem 22.txt")
	print "Completed in: %f seconds" % (time() - start)


	

