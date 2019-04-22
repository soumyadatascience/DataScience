import numpy as np
N,M = map(int,input().split())
elements=list()
for each in range(N):
    elements.append(input().split())
matrix = np.reshape(np.array(elements, int), (N, M))
print (np.transpose(matrix))
print (matrix.flatten())
