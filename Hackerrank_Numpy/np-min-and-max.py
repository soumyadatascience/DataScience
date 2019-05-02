'''
Task

You are given a 2-D array with dimensions X. 
Your task is to perform the min function over axis  and then find the max of that.

Input Format

The first line of input contains the space separated values of  and . 
The next  lines contains  space separated integers.

Output Format

Compute the min along axis  and then print the max of that result.
'''

import numpy as np
N,M = list(map(int,input().split()))
A=list()
for _ in range(N):
    A.append(list(map(int,input().split())))
A = np.array(A)
print(np.max(np.min(A,axis=1),axis=0))

