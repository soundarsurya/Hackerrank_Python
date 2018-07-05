"""
Task

You are given a 2-D array with dimensions X. 
Your task is to perform the  tool over axis  and then find the  of that result.

Input Format

The first line of input contains space separated values of  and . 
The next  lines contains  space separated integers.

Output Format

Compute the sum along axis . Then, print the product of that sum.

Sample Input

2 2
1 2
3 4
Sample Output

24
"""
#=============================================================================================#
PYTHON CODE:

import numpy
n,m=map(int,input().split())
arr=numpy.array([input().split() for i in range(n)],int)
print(numpy.prod(numpy.sum(arr,axis=0),axis=0))
