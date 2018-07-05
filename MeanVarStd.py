"""
Task

You are given a 2-D array of size X. 
Your task is to find:

The mean along axis 
The var along axis 
The std along axis 
Input Format

The first line contains the space separated values of  and . 
The next  lines contains  space separated integers.

Output Format

First, print the mean. 
Second, print the var. 
Third, print the std.

Sample Input

2 2
1 2
3 4
Sample Output

[ 1.5  3.5]
[ 1.  1.]
1.11803398875
"""
#====================================================================================================================#

PYTHON CODE:

import numpy
numpy.set_printoptions(legacy='1.13')
n,m=map(int,input().split())
arr=numpy.array([input().split() for i in range(n)],int)
print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
print(numpy.std(arr))
