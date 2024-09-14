import numpy as np

#MAtrix Functions

#Transpose

var = np.matrix([[1,2,3],[4,5,6]])
print(var)
print()
print(var.T)    #print(np.transpose(var))

#SwapAxes

print()
print(np.swapaxes(var,0,1))
print()
var2 = np.matrix([[1,2],[3,4]])
print(np.swapaxes(var2,0,1))

#Inverses
var3 = np.matrix([[1,2],[3,4]])
print(var3)
print()
print(np.linalg.inv(var3))

#Power
var4 = np.matrix([[1,2],[3,4]])
print(var4)
print()
print(np.linalg.matrix_power(var4,2))
print()
print(np.linalg.matrix_power(var4,0))
print()
print(np.linalg.matrix_power(var4,-3))

#Deteminate

var5 = np.matrix([[1,-6,3],[4,-3,6],[7,3,9]])
print(var5)
print()
print(round(np.linalg.det(var5),2))