'''
Task

You are given a 2-D array with dimensions X. 
Your task is to perform the  tool over axis  and then find the  of that result.

Input Format

The first line of input contains space separated values of  and . 
The next  lines contains  space separated integers.

Output Format

Compute the sum along axis . Then, print the product of that sum.

'''

import numpy as np
N,M = list(map(int,input().split()))
A=list()
B=list()
for _ in range(N):
    A.append(list(map(int,input().split())))
A = np.array(A)
print(np.prod(np.sum(A,axis=0),axis=0))
