'''
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
'''

import numpy as np
N,M = map(int,input().split())
A=list()
for _ in range(N):
    A.append(list(map(int,input().split())))
A=np.array(A)
np.set_printoptions(legacy='1.13')
print(np.mean(A,axis=1))
print(np.var(A,axis=0))
print(np.std(A,axis=None))
