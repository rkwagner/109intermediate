'''
Author:		Ryan Wagner
		rkwagner@ucsd.edu
		http://github.com/rkwagner
Date:		August 26, 2014
Description:	Given two input integer ranges, determines any palindromes
		formed by the multiplication of two integers in those
		ranges.
Input:		Integer Range 1, Integer range 2
Output:		List if valid palindrome combinations, else "None found."
'''

import sys

#Find possible palindromes in the input integer/string.
def palindrome( in_string ):
	for x in range( in_string[ 0 ] , in_string[ 1 ] + 1 ):
		for y in range( in_string[ 2 ] , in_string[ 3 ] + 1 ):
			if str( x * y ) == str( x * y )[ : : -1]:
				print "{", x, ",", y, "}",
	print ""

try:
	in_string = [ int( i ) for i in sys.argv[ 1 : ] ]
	if len ( in_string ) != 4:
		print 'Invalid Arg Length...'
	else:
		palindrome( in_string )
except ValueError:
	print'Invalid Args...'
