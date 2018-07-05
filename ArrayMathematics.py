"""
Task

You are given two integer arrays,  and  of dimensions X. 
Your task is to perform the following operations:

Add ( + )
Subtract ( - )
Multiply ( * )
Integer Division ( / )
Mod ( % )
Power ( ** )
Input Format

The first line contains two space separated integers,  and . 
The next  lines contains  space separated integers of array . 
The following  lines contains  space separated integers of array .

Output Format

Print the result of each operation in the given order under Task.

Sample Input

1 4
1 2 3 4
5 6 7 8
Sample Output

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 
Use // for division in Python 3.
"""
#===========================================================================================================#
PYTHON CODE:

import numpy
n,m=map(int,input().split())
a=numpy.array([input().split() for i in range(n)],int)
b=numpy.array([input().split() for i in range(n)],int)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(a//b)
print(numpy.mod(a,b))
print(numpy.power(a,b))
