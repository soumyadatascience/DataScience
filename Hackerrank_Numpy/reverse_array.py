import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr,float)
    return numpy.flip(arr,axis=0)

arr = input().strip().split(' ')
