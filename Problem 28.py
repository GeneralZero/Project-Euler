!/usr/bin/env python

def sum_corners(length): #length is oddnumbers
	if length == 1:
		return 1
	top_right = length*length
	top_left  = top_right - length + 1
	bottom_left  = top_left - length + 1
	bottom_right  =  bottom_left - length + 1
	return  top_right + top_left + bottom_left + bottom_right

num=0
for x in range(1, 1002, 2):
	print x, sum_corners(x)
	num += sum_corners(x)
print num