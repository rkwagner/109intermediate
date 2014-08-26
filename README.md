Author
------
Ryan Wagner
rkwagner@ucsd.edu
http://github.com/rkwagner
August 26, 2014

Description
-----------
A palindrome is a string of characters that are read the same way both 
ways (forward and backwards). Given two range of integers 
(a_start, a_end and b_start, b_end), if at least one of the products 
between the two ranges is a palindrome, print the integer-pair.

For example, if the first range of integers is [90,99] and the second 
is [90,99], there is at least one palindrome because 91 x 99 = 9009, 
which is read the same forward and backward. Thus, "91, 99" should be 
printed.

Input/Output
------------
Input Description:
Integer a_start - The starting range of the integer a
Integer a_end - The ending range of the integer a
Integer b_start - The starting range of the integer b
Integer b_end - The ending range of the integer b

Output Description:
Print an integer pair if their product is a palindrome.

Notes
-----
This problem is of an easy-intermediate difficulty level; 
a brute-force solution works well enough, but think of what happens 
when given a large range of numbers. What is the computational 
complexity? What can you do to optimize palindrome verification?
