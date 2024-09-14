import numpy as np

#Join
#1-D
var = np.array([1,2,3,4])
var2 = np.array([5,6,7,8])

new_ar = np.concatenate((var,var2))
print(new_ar)
print()

#2-D

var3 = np.array([[1,2],[3,4]])
var4 = np.array([[5,6],[7,8]])

new_ar1 = np.concatenate((var3,var4),axis = 1)
print(new_ar1)
print()
#Using Stack

var5 = np.array([1,2,3,4])
var6 = np.array([5,6,7,8])

new_ar2 = np.stack((var5,var6),axis = 0)    #using axis 0 = column,1 = row
print(new_ar2)
print()
new_ar2 = np.hstack((var5,var6))    #along row
print(new_ar2)
print()
new_ar2 = np.vstack((var5,var6))    #along column
print(new_ar2)
print()
new_ar2 = np.dstack((var5,var6))    #along height
print(new_ar2)

