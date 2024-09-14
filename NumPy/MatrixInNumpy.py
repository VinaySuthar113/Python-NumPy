import numpy as np

#MATRIX

var = np.matrix([[1,2],[4,5]])
var2= np.matrix([[1,2],[4,6]])
print(var)
print(type(var))
print()
print(var + var2)
print()
print(var.dot(var2))
print()
var1 = np.array([[1,2,3],[4,5,6]])
print(var1)
print(type(var1))