"""
Task 
You are given a 1-D array, . Your task is to print the ,  and  of all the elements of .

Input Format

A single line of input containing the space separated elements of array .

Output Format

On the first line, print the floor  of A. 
On the second line, print the ceil of A. 
On the third line, print the rint of A.

Sample Input

1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
Sample Output

[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
"""
#================================================================================================#

PYTHON CODE:

import numpy
numpy.set_printoptions(sign=' ')
arr=numpy.array(input().split( ),float)
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
