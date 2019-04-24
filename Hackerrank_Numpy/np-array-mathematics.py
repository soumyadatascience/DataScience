import numpy as np
N,M=map(int,input().split())
A=list()
B=list()
for _ in range(N):
    A.append(list(map(int,input().split())))
A = np.array(A)
for _ in range(N):
    B.append(list(map(int,input().split())))
B = np.array(B)
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
print(A**B)
