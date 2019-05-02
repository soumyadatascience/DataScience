'''
Task

You are given two arrays  and . Both have dimensions of X. 
Your task is to compute their matrix product.

Input Format

The first line contains the integer . 
The next  lines contains  space separated integers of array . 
The following  lines contains  space separated integers of array .

Output Format

Print the matrix multiplication of  and .
'''

import numpy as np
N = int(input())
A=list()
B=list()
for _ in range(N):
    A.append(list(map(int,input().split())))
for _ in range(N):
    B.append(list(map(int,input().split())))
A=np.array(A)
B=np.array(B)
print (np.dot(A, B))
