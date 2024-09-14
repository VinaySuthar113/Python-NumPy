import numpy as np

#Indexing in array

#1-D
var = np.array([9,8,7,6])
print(var[1])
print(var[-3])

#2-D
var2 = np.array([[1,2,3],[4,5,6]])
print(var2[0,2])

#3-D
var3 = np.array([[[1,2,3],[4,5,6],[8,9,10]]])
print(var3[0,1,1])

#Slicing in Array

x = np.array([1,2,3,4,5,6,7,8])
print(x[1:8:2])

y = np.array([[1,2,3,4],[5,6,7,8]])
print(y[1,1:])