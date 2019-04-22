import numpy as np
N,M,P = map(int,input().split()) 

l1=list()
l2=list()

for each in range(N):
    l1.append(input().split())

for each in range(M):
    l2.append(input().split())
array1 = np.reshape(np.array(l1, int), (N, P))
array2 = np.reshape(np.array(l2, int), (M, P))

print(np.concatenate((array1, array2),axis=0))
