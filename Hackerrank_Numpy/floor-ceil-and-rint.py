import numpy as np
A =np.array(list(map(float,input().split())))
np.set_printoptions(legacy='1.13')
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))
